#!/bin/bash
# Quick start script for real-time golf ball tracker

echo "=========================================="
echo "Golf Ball Tracker - Real-Time Server"
echo "=========================================="
echo ""

# Check if Flask is installed
python3 -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing Flask..."
    pip3 install flask
fi

# Get IP address
echo "Your IP addresses:"
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print "  " $2}'
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    hostname -I | awk '{for(i=1;i<=NF;i++) print "  " $i}'
else
    echo "  Please find your IP manually (ipconfig on Windows)"
fi

echo ""
echo "Starting server..."
echo "Access from iPhone: http://YOUR_IP:5000"
echo ""
echo "Press Ctrl+C to stop"
echo "=========================================="
echo ""

python3 web_server.py
