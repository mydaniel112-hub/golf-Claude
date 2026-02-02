# App Failed to Respond - Check Logs

## The Issue
The app deployed but isn't responding. This usually means it's crashing on startup.

## Check Railway Logs

1. Go to https://railway.app
2. Click on your `golf-Claude` project
3. Click on the **"Deployments"** tab
4. Click on the latest deployment
5. Click **"View Logs"** or **"Logs"** tab

## What to Look For

Common errors:
- **Import errors**: Missing modules
- **OpenCV errors**: cv2 not found or can't load
- **Port errors**: PORT not set correctly
- **Path errors**: Can't find templates or files

## Share the Error

Copy the error message from the logs and share it. The logs will show exactly what's wrong.

## Quick Fixes to Try

### If OpenCV fails:
Railway might not support OpenCV. We may need to use a different platform like Render or Fly.io.

### If PORT error:
The PORT env var should be set automatically by Railway. Check if it's in the environment variables.

### If import errors:
Check that all dependencies are in `requirements.txt` and installed correctly.

---

**Next Step:** Check the Railway logs and share the error message!
