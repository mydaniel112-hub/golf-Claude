# Golf Ball Tracker

Real-time golf ball tracking system using computer vision and Kalman filtering.

## Features

- Real-time ball detection using color and motion
- Kalman filter-based trajectory tracking
- 3D trajectory reconstruction
- Web interface for iPhone access
- Adaptive FPS handling for different video sources

## Setup

### Local Development

1. Install dependencies:
```bash
cd golf_tracker
pip install -r requirements.txt
```

2. Start the web server:
```bash
python3 web_server.py
```

3. Access from iPhone:
   - Get your IP: `ifconfig | grep "inet " | grep -v 127.0.0.1`
   - Open Safari on iPhone: `http://YOUR_IP:5000`

## Deployment

### Railway (Recommended)

1. Push to GitHub
2. Go to https://railway.app
3. New Project → Deploy from GitHub
4. Select repository
5. Railway auto-detects and deploys!

### Render

1. Push to GitHub
2. Create Web Service on Render.com
3. Connect GitHub repo
4. Build: `pip install -r golf_tracker/requirements.txt`
5. Start: `cd golf_tracker && python3 web_server.py`

## Requirements

- Python 3.9+
- OpenCV
- NumPy
- SciPy
- FilterPy
- Flask

## Usage

1. Open web interface on iPhone
2. Allow camera access
3. Press "Start" to begin tracking
4. Point camera at golf ball
5. Ball trajectory will be tracked in real-time

## License

MIT
