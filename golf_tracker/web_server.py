"""Flask web server for real-time golf ball tracking from iPhone"""
from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np
import base64
import io
from PIL import Image
from video_processor import VideoProcessor
from ball_tracker import BallTracker
import threading
import time

app = Flask(__name__)

# Global processor instance
processor = None
processing_lock = threading.Lock()

def init_processor():
    """Initialize video processor"""
    global processor
    processor = VideoProcessor("")
    processor.fps = 30  # Default for web streaming
    processor.tracker = BallTracker(fps=30)
    processor.current_frame = None  # Initialize frame storage

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """MJPEG video stream endpoint"""
    return Response(generate_frames(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_frames():
    """Generate frames for MJPEG stream"""
    global processor
    if processor is None:
        init_processor()
    
    while True:
        # This will be populated by frames from iPhone
        with processing_lock:
            if hasattr(processor, 'current_frame') and processor.current_frame is not None:
                frame = processor.current_frame.copy()
                # Encode frame
                ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
                if ret:
                    frame_bytes = buffer.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.033)  # ~30 FPS

@app.route('/process_frame', methods=['POST'])
def process_frame():
    """Receive frame from iPhone and process it"""
    global processor
    if processor is None:
        init_processor()
    
    try:
        # Get frame data from request
        data = request.json
        if 'frame' not in data:
            return jsonify({'error': 'No frame data'}), 400
        
        # Decode base64 image
        frame_data = data['frame'].split(',')[1]  # Remove data:image/jpeg;base64,
        frame_bytes = base64.b64decode(frame_data)
        
        # Convert to numpy array
        nparr = np.frombuffer(frame_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if frame is None:
            return jsonify({'error': 'Failed to decode frame'}), 400
        
        # Process frame
        with processing_lock:
            processed_frame = processor.process_frame(frame)
            processor.current_frame = processed_frame
            processor.frame_count += 1
        
        # Encode processed frame
        ret, buffer = cv2.imencode('.jpg', processed_frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
        if ret:
            frame_bytes = buffer.tobytes()
            frame_b64 = base64.b64encode(frame_bytes).decode('utf-8')
            
            # Get tracking stats
            stats = {
                'frame': processor.frame_count,
                'tracking': 'Active' if processor.tracker.is_tracking else 'Inactive',
                'trajectory_length': len(processor.tracker.get_trajectory())
            }
            
            return jsonify({
                'frame': f'data:image/jpeg;base64,{frame_b64}',
                'stats': stats
            })
        
        return jsonify({'error': 'Failed to encode frame'}), 500
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start_tracking', methods=['POST'])
def start_tracking():
    """Start ball tracking"""
    global processor
    if processor is None:
        init_processor()
    
    processor.detection_active = True
    return jsonify({'status': 'Tracking started'})

@app.route('/reset_tracking', methods=['POST'])
def reset_tracking():
    """Reset ball tracking"""
    global processor
    if processor is None:
        init_processor()
    
    from ball_tracker import BallTracker
    processor.tracker = BallTracker(fps=processor.fps)
    processor.detection_active = False
    return jsonify({'status': 'Tracking reset'})

@app.route('/status', methods=['GET'])
def status():
    """Get current tracking status"""
    global processor
    if processor is None:
        return jsonify({'status': 'not_initialized'})
    
    return jsonify({
        'tracking': processor.tracker.is_tracking,
        'active': processor.detection_active,
        'frame_count': processor.frame_count
    })

if __name__ == '__main__':
    init_processor()
    # Run on all interfaces so iPhone can connect
    # Find your laptop's IP: ifconfig (Mac/Linux) or ipconfig (Windows)
    print("\n" + "="*60)
    print("Golf Ball Tracker - Web Server")
    print("="*60)
    print("\nTo access from iPhone:")
    print("1. Make sure iPhone and laptop are on same WiFi")
    print("2. Find your laptop IP address:")
    print("   Mac/Linux: ifconfig | grep 'inet '")
    print("   Windows: ipconfig | findstr IPv4")
    print("3. Open Safari on iPhone and go to: http://YOUR_IP:5000")
    print("\nStarting server...")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
