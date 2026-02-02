"""Main video processing pipeline"""
import cv2
import numpy as np
from ball_detector import BallDetector
from ball_tracker import BallTracker
from trajectory_builder import TrajectoryBuilder
from overlay_renderer import OverlayRenderer
from calibration import CameraCalibration
from config import Config

class VideoProcessor:
    def __init__(self, video_path):
        self.video_path = video_path
        # Only open video file if path is provided (not empty string for live mode)
        if video_path:
            self.cap = cv2.VideoCapture(video_path)
            # Check FPS
            fps = self.cap.get(cv2.CAP_PROP_FPS)
            if fps < Config.MIN_FPS:
                print(f"Warning: Video FPS ({fps}) is below recommended {Config.MIN_FPS}")
        else:
            self.cap = None
        
        self.detector = BallDetector()
        # Get FPS for tracker initialization
        if video_path and self.cap:
            self.fps = self.cap.get(cv2.CAP_PROP_FPS) or 30  # Default to 30 if unknown
        else:
            self.fps = 30  # Default for live mode
        self.tracker = BallTracker(fps=self.fps)
        self.calibration = CameraCalibration()
        self.trajectory_builder = TrajectoryBuilder(self.calibration)
        self.renderer = OverlayRenderer()
        
        self.frame_count = 0
        self.detection_active = False
        
    def process_video(self, output_path='output_tracked.mp4', start_frame=0):
        """Process entire video and add ball tracking overlay"""
        # Get video properties
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = self.cap.get(cv2.CAP_PROP_FPS) or 30
        
        # Update tracker with actual FPS
        if fps != self.fps:
            self.fps = fps
            self.tracker = BallTracker(fps=fps)
        
        # Setup output video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        # Skip to start frame
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        
        print(f"Processing video at {fps} FPS...")
        print("Press 'q' to quit, 's' to start tracking, 'r' to reset")
        
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            
            self.frame_count += 1
            
            # Process frame
            processed_frame = self.process_frame(frame)
            
            # Write output
            out.write(processed_frame)
            
            # Display
            display_frame = cv2.resize(processed_frame, (1280, 720))
            cv2.imshow('Golf Ball Tracker', display_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                self.detection_active = True
                print("Tracking started")
            elif key == ord('r'):
                self.tracker = BallTracker(fps=self.fps)
                self.detection_active = False
                print("Tracker reset")
            
            if self.frame_count % 30 == 0:
                print(f"Processed {self.frame_count} frames...")
        
        self.cap.release()
        out.release()
        cv2.destroyAllWindows()
        print(f"Output saved to {output_path}")
    
    def process_frame(self, frame):
        """Process single frame"""
        # Detect ball candidates
        candidates = self.detector.find_ball_candidates(frame)
        
        # Select best candidate
        previous_pos = None
        if self.tracker.is_tracking:
            trajectory = self.tracker.get_trajectory()
            if trajectory:
                previous_pos = trajectory[-1]
        
        detection = self.detector.select_best_candidate(candidates, previous_pos)
        
        # Update tracker
        if self.detection_active:
            if detection is not None:
                if not self.tracker.is_tracking:
                    self.tracker.initialize(detection['center'])
                else:
                    self.tracker.predict()
                    self.tracker.update(detection['center'])
            else:
                if self.tracker.is_tracking:
                    self.tracker.predict()
                    self.tracker.update(None)
        
        # Get trajectory
        trajectory = self.tracker.get_trajectory()
        
        # Smooth trajectory
        if len(trajectory) > 5:
            trajectory = self.trajectory_builder.smooth_trajectory(trajectory)
        
        # Draw overlay
        current_pos = trajectory[-1] if trajectory else None
        frame = self.renderer.draw_trajectory(frame, trajectory, current_pos)
        
        # Draw stats
        stats = {
            'Frame': self.frame_count,
            'Tracking': 'Active' if self.tracker.is_tracking else 'Inactive',
            'Detections': len(candidates)
        }
        
        if self.tracker.is_tracking:
            velocity = self.tracker.get_velocity()
            speed = np.linalg.norm(velocity)
            stats['Speed (px/frame)'] = f"{speed:.1f}"
        
        frame = self.renderer.draw_stats(frame, stats)
        
        # Draw detection candidates (for debugging)
        for candidate in candidates:
            cv2.circle(frame, candidate['center'], candidate['radius'], 
                      (0, 255, 255), 1)
        
        return frame
    
    def process_live(self, camera_id=0):
        """Process live camera feed"""
        self.cap = cv2.VideoCapture(camera_id)
        # Get actual FPS (iPhone cameras vary)
        actual_fps = self.cap.get(cv2.CAP_PROP_FPS) or 30
        if actual_fps != self.fps:
            self.fps = actual_fps
            self.tracker = BallTracker(fps=actual_fps)
        print(f"Camera FPS: {actual_fps}")
        
        print("Live processing started. Press 's' to start tracking, 'r' to reset, 'q' to quit")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            processed_frame = self.process_frame(frame)
            
            cv2.imshow('Golf Ball Tracker - Live', processed_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                self.detection_active = True
            elif key == ord('r'):
                self.tracker = BallTracker(fps=self.fps)
                self.detection_active = False
        
        self.cap.release()
        cv2.destroyAllWindows()
