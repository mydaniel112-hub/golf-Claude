# Deployment Options for Golf Ball Tracker

## ⚠️ Important: Vercel Limitations

**Vercel cannot run this application** because:
- OpenCV (cv2) requires native C++ libraries
- Real-time video processing needs persistent server processes
- Vercel is serverless and doesn't support long-running processes

## ✅ Better Alternatives

### Option 1: Railway (Recommended - Easiest)
Railway supports Python with native dependencies.

**Steps:**
1. Push to GitHub (see commands below)
2. Go to https://railway.app
3. Click "New Project" → "Deploy from GitHub"
4. Select your repository
5. Railway auto-detects Python and installs dependencies
6. Your app will be live at `https://your-app.railway.app`

**Cost:** Free tier available, then ~$5/month

---

### Option 2: Render
Similar to Railway, good for Python apps.

**Steps:**
1. Push to GitHub
2. Go to https://render.com
3. Create new "Web Service"
4. Connect GitHub repo
5. Set:
   - Build Command: `pip install -r golf_tracker/requirements.txt`
   - Start Command: `cd golf_tracker && python3 web_server.py`
6. Deploy!

**Cost:** Free tier available

---

### Option 3: Fly.io
Great for real-time apps.

**Steps:**
1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Run: `fly launch` in your project
3. Follow prompts
4. Deploy: `fly deploy`

**Cost:** Free tier available

---

### Option 4: Simplified Vercel Version (Limited)
If you MUST use Vercel, we'd need to:
- Remove OpenCV dependency
- Use browser-based processing only
- Much less accurate tracking

**Not recommended for golf ball tracking.**

---

## Recommended: Railway

Railway is the easiest and best fit for this app. It handles OpenCV automatically.
