# Quick Commands

## 1. Fix Localhost Issue (Use Your IP Instead)

The server runs on `0.0.0.0:5000` which means you CAN'T use `localhost` or `127.0.0.1` from your iPhone.

**Get your laptop's IP address:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

Look for something like `192.168.1.XXX` or `10.0.0.XXX`

**On iPhone, use:** `http://YOUR_IP:5000` (NOT localhost!)

---

## 2. Push to GitHub

### Option A: New Repository

```bash
cd "/Users/danielmacwilliams/gold claude"
git init
git add .
git commit -m "Golf ball tracker with real-time web interface"
```

Then create a repo on GitHub.com and:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### Option B: Existing Repository

If you already have a GitHub repo:
```bash
cd "/Users/danielmacwilliams/gold claude"
git init
git add .
git commit -m "Golf ball tracker with real-time web interface"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## 3. Start Server (After GitHub Push)

```bash
cd "/Users/danielmacwilliams/gold claude/golf_tracker"
python3 web_server.py
```

Then use your IP address (not localhost) on iPhone!
