"""Camera calibration utilities"""
import numpy as np
import cv2

class CameraCalibration:
    def __init__(self):
        # Camera intrinsic parameters (you need to calibrate these)
        self.camera_matrix = None
        self.dist_coeffs = None
        self.rotation_matrix = None
        self.translation_vector = None
        
    def calibrate_from_checkerboard(self, images, checkerboard_size=(9, 6)):
        """Calibrate camera using checkerboard images"""
        # Prepare object points
        objp = np.zeros((checkerboard_size[0] * checkerboard_size[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:checkerboard_size[0], 
                               0:checkerboard_size[1]].T.reshape(-1, 2)
        
        obj_points = []
        img_points = []
        
        for img in images:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, checkerboard_size, None)
            
            if ret:
                obj_points.append(objp)
                img_points.append(corners)
        
        if len(obj_points) > 0:
            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
                obj_points, img_points, gray.shape[::-1], None, None
            )
            self.camera_matrix = mtx
            self.dist_coeffs = dist
            return True
        
        return False
    
    def set_manual_calibration(self, focal_length, sensor_size, resolution):
        """Set calibration manually if you know camera specs"""
        fx = focal_length * resolution[0] / sensor_size[0]
        fy = focal_length * resolution[1] / sensor_size[1]
        cx = resolution[0] / 2
        cy = resolution[1] / 2
        
        self.camera_matrix = np.array([
            [fx, 0, cx],
            [0, fy, cy],
            [0, 0, 1]
        ])
        
        self.dist_coeffs = np.zeros(5)
    
    def undistort_frame(self, frame):
        """Remove lens distortion from frame"""
        if self.camera_matrix is None:
            return frame
        
        return cv2.undistort(frame, self.camera_matrix, self.dist_coeffs)
