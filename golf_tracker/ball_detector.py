"""Ball detection using color and motion detection"""
import cv2
import numpy as np
from config import Config

class BallDetector:
    def __init__(self):
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=500, varThreshold=16, detectShadows=False
        )
        self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        
    def detect_by_color(self, frame):
        """Detect white golf ball by color - optimized for outdoor conditions"""
        # Convert to HSV for better color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # White detection in HSV - more lenient for bright outdoor conditions
        # Lower saturation threshold to catch overexposed white balls
        lower_white = np.array([0, 0, 180])  # Lowered from 200 for bright conditions
        upper_white = np.array([180, 50, 255])  # Increased saturation tolerance
        
        mask = cv2.inRange(hsv, lower_white, upper_white)
        
        # Also try BGR space for very bright/overexposed areas
        bgr_mask = cv2.inRange(frame, (200, 200, 200), (255, 255, 255))
        mask = cv2.bitwise_or(mask, bgr_mask)
        
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, self.kernel)
        
        return mask
    
    def detect_by_motion(self, frame):
        """Detect moving objects - improved for camera shake"""
        fg_mask = self.bg_subtractor.apply(frame)
        
        # Use larger kernel to reduce noise from camera shake
        larger_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, larger_kernel)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, larger_kernel)
        
        return fg_mask
    
    def find_ball_candidates(self, frame):
        """Find potential ball locations using multiple methods"""
        color_mask = self.detect_by_color(frame)
        motion_mask = self.detect_by_motion(frame)
        
        # Combine masks
        combined_mask = cv2.bitwise_and(color_mask, motion_mask)
        
        # Find contours
        contours, _ = cv2.findContours(
            combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        
        candidates = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < Config.MIN_MOTION_AREA:
                continue
            
            # Fit circle to contour
            ((x, y), radius) = cv2.minEnclosingCircle(contour)
            
            # Filter by size (more lenient for small distant balls)
            if Config.MIN_BALL_RADIUS <= radius <= Config.MAX_BALL_RADIUS:
                # Calculate circularity
                perimeter = cv2.arcLength(contour, True)
                if perimeter == 0:
                    continue
                circularity = 4 * np.pi * area / (perimeter ** 2)
                
                # Golf balls are circular - lower threshold for small balls
                # Small balls (radius < 5) might be less circular due to pixelation
                min_circularity = 0.5 if radius < 5 else 0.7
                if circularity > min_circularity:
                    candidates.append({
                        'center': (int(x), int(y)),
                        'radius': int(radius),
                        'circularity': circularity,
                        'area': area
                    })
        
        return candidates
    
    def select_best_candidate(self, candidates, previous_position=None):
        """Select most likely ball from candidates"""
        if not candidates:
            return None
        
        if previous_position is None:
            # First detection - choose most circular, medium-sized
            best = max(candidates, key=lambda c: c['circularity'])
            return best
        
        # Choose closest to previous position
        prev_x, prev_y = previous_position
        
        def distance_score(candidate):
            cx, cy = candidate['center']
            dist = np.sqrt((cx - prev_x)**2 + (cy - prev_y)**2)
            if dist > Config.MAX_DISTANCE:
                return float('inf')
            return dist
        
        closest = min(candidates, key=distance_score)
        if distance_score(closest) == float('inf'):
            return None
        
        return closest
