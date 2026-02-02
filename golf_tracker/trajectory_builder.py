"""3D trajectory reconstruction and physics modeling"""
import numpy as np
from scipy.optimize import least_squares
from config import Config

class TrajectoryBuilder:
    def __init__(self, camera_calibration):
        self.calibration = camera_calibration
        
    def pixel_to_world(self, pixel_coords, frame_height):
        """Convert pixel coordinates to approximate world coordinates"""
        x_px, y_px = pixel_coords
        
        # Simple perspective transformation
        # This is simplified - real version needs camera calibration matrix
        
        # Estimate distance based on y position (higher in frame = farther)
        distance_scale = (frame_height - y_px) / frame_height
        estimated_distance = 5 + distance_scale * 200  # 5-205 meters
        
        # Convert to meters (very approximate)
        scale = Config.PIXELS_PER_METER_AT_50M / (estimated_distance / 50)
        
        world_x = x_px / scale
        world_z = estimated_distance
        
        # Estimate height based on trajectory shape
        world_y = self._estimate_height(y_px, frame_height)
        
        return np.array([world_x, world_y, world_z])
    
    def _estimate_height(self, y_px, frame_height):
        """Estimate ball height from y pixel position"""
        # Ball at top of frame is high, bottom is on ground
        height_ratio = (frame_height - y_px) / frame_height
        max_height = 50  # assume max 50m height
        return height_ratio * max_height
    
    def fit_parabola(self, trajectory_2d):
        """Fit parabolic trajectory to 2D points"""
        if len(trajectory_2d) < 3:
            return None
        
        points = np.array(trajectory_2d)
        x = points[:, 0]
        y = points[:, 1]
        
        # Fit y = ax^2 + bx + c
        try:
            coeffs = np.polyfit(x, y, 2)
            return coeffs
        except:
            return None
    
    def predict_landing(self, trajectory_3d):
        """Predict where ball will land"""
        if len(trajectory_3d) < 5:
            return None
        
        points = np.array(trajectory_3d)
        
        # Fit trajectory to ballistic equation
        # x(t) = x0 + vx0*t
        # y(t) = y0 + vy0*t - 0.5*g*t^2
        # z(t) = z0 + vz0*t
        
        # Find when y = 0 (ground level)
        # This is simplified - real version uses drag equations
        
        try:
            # Estimate initial velocity from first few points
            if len(points) < 2:
                return None
            
            v0 = points[1] - points[0]
            p0 = points[0]
            
            # Solve for t when y = 0
            # 0 = y0 + vy0*t - 0.5*g*t^2
            a = -0.5 * Config.GRAVITY
            b = v0[1]
            c = p0[1]
            
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                return None
            
            t = (-b - np.sqrt(discriminant)) / (2*a)
            if t < 0:
                t = (-b + np.sqrt(discriminant)) / (2*a)
            
            if t < 0:
                return None
            
            # Calculate landing position
            landing = p0 + v0 * t
            landing[1] = 0  # on ground
            
            return landing
        except:
            return None
    
    def smooth_trajectory(self, trajectory):
        """Smooth trajectory using Savitzky-Golay filter"""
        from scipy.signal import savgol_filter
        
        if len(trajectory) < 5:
            return trajectory
        
        points = np.array(trajectory)
        
        try:
            # Apply smoothing to each dimension
            smoothed = np.column_stack([
                savgol_filter(points[:, 0], min(len(points), 5), 2),
                savgol_filter(points[:, 1], min(len(points), 5), 2)
            ])
            return smoothed.tolist()
        except:
            return trajectory
