# Quick Start - Terminal Commands

## Step 1: Navigate to the project
```bash
cd "golf_tracker"
```

## Step 2: Install Flask (if not already installed)
```bash
pip install flask
```

## Step 3: Find your laptop's IP address

**On Mac (you're on Mac):**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

Look for something like `192.168.1.XXX` or `10.0.0.XXX`

## Step 4: Start the server
```bash
python web_server.py
```

You should see:
```
Starting server...
 * Running on http://0.0.0.0:5000
```

## Step 5: On your iPhone
1. Make sure iPhone and laptop are on same WiFi
2. Open Safari
3. Go to: `http://YOUR_IP:5000` (use the IP from step 3)

That's it! The web page will open and ask for camera permission.

---

## All-in-One Commands (copy/paste):

```bash
cd "golf_tracker" && pip install flask && python web_server.py
```

Then find your IP:
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```
