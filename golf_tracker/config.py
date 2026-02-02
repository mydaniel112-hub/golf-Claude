"""Configuration settings for golf ball tracker"""

class Config:
    # Video settings
    MIN_FPS = 120  # Minimum recommended frame rate
    RESOLUTION = (1920, 1080)
    
    # Ball detection parameters
    BALL_COLOR_LOWER = (200, 200, 200)  # White ball lower bound (BGR)
    BALL_COLOR_UPPER = (255, 255, 255)  # White ball upper bound
    MIN_BALL_RADIUS = 1  # pixels (reduced for distance shots)
    MAX_BALL_RADIUS = 30  # pixels
    
    # Motion detection
    MOTION_THRESHOLD = 25
    MIN_MOTION_AREA = 10
    
    # Tracking parameters
    MAX_DISAPPEARED = 15  # frames before losing track (increased for lower FPS)
    MAX_DISTANCE = 150  # max pixel distance between frames (increased for lower FPS)
    
    # Physics parameters (real world)
    GRAVITY = 9.81  # m/s^2
    BALL_MASS = 0.0459  # kg (golf ball mass)
    BALL_DIAMETER = 0.0427  # meters
    AIR_DENSITY = 1.225  # kg/m^3
    DRAG_COEFFICIENT = 0.25  # golf ball drag
    
    # Calibration (you'll need to adjust these)
    CAMERA_HEIGHT = 1.5  # meters above ground
    CAMERA_ANGLE = 10  # degrees from horizontal
    PIXELS_PER_METER_AT_50M = 20  # calibration factor
    
    # Visualization
    TRAIL_LENGTH = 30  # number of points in trail
    TRAIL_COLOR = (0, 255, 255)  # yellow
    TRAIL_THICKNESS = 3
