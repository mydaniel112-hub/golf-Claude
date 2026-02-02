"""Kalman filter-based ball tracking"""
import numpy as np
from filterpy.kalman import KalmanFilter
from collections import deque
from config import Config

class BallTracker:
    def __init__(self, fps=120):
        # State: [x, y, vx, vy]
        self.kf = KalmanFilter(dim_x=4, dim_z=2)
        self.fps = fps
        
        # State transition matrix (constant velocity model)
        dt = 1.0 / fps
        self.kf.F = np.array([
            [1, 0, dt, 0],
            [0, 1, 0, dt],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        
        # Measurement matrix (we only measure position)
        self.kf.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ])
        
        # Measurement noise
        self.kf.R *= 10
        
        # Process noise
        self.kf.Q *= 0.1
        
        # Initial state covariance
        self.kf.P *= 1000
        
        self.trajectory = deque(maxlen=Config.TRAIL_LENGTH * 3)
        self.disappeared = 0
        self.is_tracking = False
        
    def initialize(self, position):
        """Initialize tracker with first detection"""
        x, y = position
        self.kf.x = np.array([x, y, 0, 0])
        self.is_tracking = True
        self.disappeared = 0
        self.trajectory.clear()
        self.trajectory.append(position)
        
    def update(self, detection=None):
        """Update tracker with new detection or prediction"""
        if detection is not None:
            # Update with measurement
            self.kf.update(np.array(detection))
            self.disappeared = 0
            position = tuple(self.kf.x[:2].astype(int))
            self.trajectory.append(position)
            return position
        else:
            # Just predict
            self.disappeared += 1
            if self.disappeared > Config.MAX_DISAPPEARED:
                self.is_tracking = False
                return None
            
            # Use prediction
            position = tuple(self.kf.x[:2].astype(int))
            self.trajectory.append(position)
            return position
    
    def predict(self):
        """Predict next position"""
        self.kf.predict()
        return tuple(self.kf.x[:2].astype(int))
    
    def get_velocity(self):
        """Get current velocity estimate"""
        return self.kf.x[2:4]
    
    def get_trajectory(self):
        """Get trajectory points"""
        return list(self.trajectory)
