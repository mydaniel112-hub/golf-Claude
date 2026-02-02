# Real-Time iPhone Setup - Quick Start

## Setup (Do this before going to the course!)

### 1. Install Flask
```bash
cd golf_tracker
pip install flask
```

### 2. Find Your Laptop's IP Address

**On Mac/Linux:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

**On Windows:**
```bash
ipconfig
```
Look for "IPv4 Address" under your WiFi adapter.

You'll see something like: `192.168.1.XXX` or `10.0.0.XXX`

### 3. Start the Server
```bash
cd golf_tracker
python web_server.py
```

You should see:
```
Starting server...
 * Running on http://0.0.0.0:5000
```

### 4. Connect iPhone

1. **Make sure iPhone and laptop are on the SAME WiFi network**
2. Open Safari on iPhone (Chrome works too)
3. Go to: `http://YOUR_IP:5000`
   - Example: `http://192.168.1.100:5000`
4. Allow camera access when prompted

## Usage on the Course

1. **Point iPhone camera at the golf ball area**
2. **Press "Start"** when ready to track
3. **Press "Reset"** to restart tracking
4. **Press "Stop"** to stop camera

The processed video with ball tracking overlay will appear on your iPhone screen in real-time!

## Troubleshooting

### Can't connect from iPhone?
- Make sure both devices are on same WiFi
- Check firewall isn't blocking port 5000
- Try turning off VPN if you have one
- Make sure you're using the correct IP address

### Camera not working?
- Make sure you allowed camera access in Safari
- Try refreshing the page
- Check Safari settings → Camera permissions

### Slow/laggy?
- Lower the frame rate in `index.html` (change `33` to `66` for ~15 FPS)
- Make sure laptop is plugged in (not on battery saver)
- Close other apps on laptop

### Need to change IP?
- If your IP changes, just restart the server and use new IP
- Or set a static IP on your laptop

## Tips for Best Results

1. **Hold iPhone steady** - Use both hands or prop it up
2. **Start tracking before the swing** - Press "Start" when ready
3. **Frame the shot well** - Include the expected ball path
4. **Good lighting helps** - But it should work in most conditions

## Alternative: Use iPhone as Hotspot

If you can't use same WiFi:
1. Turn on iPhone Personal Hotspot
2. Connect laptop to iPhone's hotspot
3. Use iPhone's IP address (usually 172.20.10.X)
4. Connect iPhone to `http://172.20.10.1:5000` (or check hotspot settings)

Good luck! 🏌️⛳
