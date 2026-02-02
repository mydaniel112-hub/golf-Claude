"""Render ball trail overlay on video"""
import cv2
import numpy as np
from config import Config

class OverlayRenderer:
    def __init__(self):
        self.trail_color = Config.TRAIL_COLOR
        self.trail_thickness = Config.TRAIL_THICKNESS
        
    def draw_trajectory(self, frame, trajectory, current_pos=None):
        """Draw ball trajectory trail"""
        if len(trajectory) < 2:
            return frame
        
        overlay = frame.copy()
        
        # Draw trajectory line
        points = np.array(trajectory, dtype=np.int32)
        
        for i in range(len(points) - 1):
            # Fade effect - older points are more transparent
            alpha = i / len(points)
            color = tuple([int(c * alpha) for c in self.trail_color])
            thickness = max(1, int(self.trail_thickness * alpha))
            
            cv2.line(overlay, tuple(points[i]), tuple(points[i + 1]), 
                    color, thickness, cv2.LINE_AA)
        
        # Draw current position
        if current_pos is not None:
            cv2.circle(overlay, current_pos, 8, (0, 255, 0), -1)
            cv2.circle(overlay, current_pos, 10, (255, 255, 255), 2)
        
        # Blend with original
        frame = cv2.addWeighted(frame, 0.7, overlay, 0.3, 0)
        
        return frame
    
    def draw_stats(self, frame, stats):
        """Draw tracking statistics"""
        y_offset = 30
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        for key, value in stats.items():
            text = f"{key}: {value}"
            cv2.putText(frame, text, (10, y_offset), font, 0.6, 
                       (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, text, (10, y_offset), font, 0.6, 
                       (0, 0, 0), 1, cv2.LINE_AA)
            y_offset += 25
        
        return frame
    
    def draw_predicted_path(self, frame, current_trajectory, prediction_points):
        """Draw predicted ball path"""
        if prediction_points is None or len(prediction_points) < 2:
            return frame
        
        points = np.array(prediction_points, dtype=np.int32)
        
        # Draw dashed line for prediction
        for i in range(0, len(points) - 1, 2):
            cv2.line(frame, tuple(points[i]), tuple(points[min(i + 1, len(points) - 1)]), 
                    (255, 0, 0), 2, cv2.LINE_AA)
        
        # Draw landing point
        if len(points) > 0:
            landing = tuple(points[-1])
            cv2.circle(frame, landing, 15, (0, 0, 255), 2)
            cv2.putText(frame, "Landing", (landing[0] + 20, landing[1]), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        return frame
