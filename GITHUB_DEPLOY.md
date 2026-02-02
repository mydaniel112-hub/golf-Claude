# Deploy to GitHub + Cloud Platform

## Step 1: Push to GitHub

```bash
cd "/Users/danielmacwilliams/gold claude"
git init
git add .
git commit -m "Golf ball tracker - ready for deployment"
```

**Create GitHub repository:**
1. Go to https://github.com/new
2. Create repository (name it something like `golf-ball-tracker`)
3. Don't initialize with README
4. Copy the repository URL

**Push to GitHub:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/golf-ball-tracker.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy to Railway (Easiest - Recommended)

### Why Railway?
- ✅ Supports OpenCV (native libraries)
- ✅ Free tier available
- ✅ Auto-detects Python
- ✅ One-click deploy from GitHub

### Steps:

1. **Go to Railway:**
   - Visit https://railway.app
   - Sign up with GitHub

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `golf-ball-tracker` repository

3. **Railway Auto-Configures:**
   - Detects Python automatically
   - Installs dependencies from `requirements.txt`
   - Runs the server

4. **Get Your URL:**
   - Railway gives you a URL like: `https://golf-ball-tracker.railway.app`
   - This is your live app!

5. **Access from iPhone:**
   - Open Safari
   - Go to: `https://your-app.railway.app`
   - Allow camera access

**That's it!** Your app is live and accessible from anywhere.

---

## Step 3: Alternative - Render.com

If Railway doesn't work:

1. Go to https://render.com
2. Sign up with GitHub
3. Create "Web Service"
4. Connect your GitHub repo
5. Settings:
   - **Build Command:** `pip install -r golf_tracker/requirements.txt`
   - **Start Command:** `cd golf_tracker && python3 web_server.py`
   - **Environment:** Python 3
6. Deploy!

---

## Step 4: Update for Production (Optional)

The server is already configured to use the `PORT` environment variable that cloud platforms provide.

If you need to customize, edit `golf_tracker/web_server.py` line 161.

---

## Troubleshooting

### Build fails?
- Check that all dependencies are in `requirements.txt`
- Make sure Python version is compatible (3.9+)

### App doesn't start?
- Check logs in Railway/Render dashboard
- Verify `web_server.py` is in `golf_tracker/` folder

### Camera not working?
- Make sure you're using HTTPS (required for camera access)
- Check browser permissions

---

## Cost

- **Railway:** Free tier (500 hours/month), then ~$5/month
- **Render:** Free tier available, then ~$7/month

Both are free to start!
