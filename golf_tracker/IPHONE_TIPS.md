# iPhone Golf Ball Tracker - Usage Tips

## How It Will Perform

### ✅ **What Should Work Well:**
- **Kalman filter tracking** - Will help maintain track even with brief occlusions
- **Motion + color detection** - Dual detection method improves reliability
- **Adaptive FPS handling** - Now automatically adjusts to your iPhone's actual frame rate

### ⚠️ **Challenges You May Face:**

1. **Ball Size at Distance**
   - At 100+ yards, the ball may be only 1-2 pixels
   - The system now accepts smaller detections, but may still struggle at extreme distances
   - **Tip**: Try to record from closer if possible, or use iPhone's zoom feature

2. **Bright Outdoor Conditions**
   - White clouds, bright grass, and overexposed areas can cause false positives
   - Improved color detection should help, but may still detect other white objects
   - **Tip**: Try to frame shots with darker backgrounds (trees, sky) when possible

3. **Camera Shake**
   - Handheld recording will cause jitter
   - Motion detection is improved but may still be affected
   - **Tip**: Use a tripod or stabilize your phone if possible

4. **Frame Rate**
   - Standard iPhone video: 30 FPS (will work but less accurate)
   - Slow-motion mode: 120/240 FPS (much better for tracking)
   - **Tip**: Use slow-motion mode if your iPhone supports it!

## Best Practices for Today

### Before Recording:
1. **Use Slow-Motion Mode** (if available)
   - iPhone 6s+: 240 FPS at 720p
   - iPhone 13+: 240 FPS at 1080p
   - This dramatically improves tracking accuracy

2. **Camera Settings**
   - Lock focus on the ball area before recording
   - Use manual exposure if possible (avoid overexposure)
   - Record in landscape mode for better field of view

3. **Positioning**
   - Stand behind/beside the golfer, not in front
   - Keep camera as steady as possible
   - Frame the shot to include expected ball path

### During Recording:
1. **Start tracking before the swing** - Press 's' when ready
2. **Watch for false detections** - Yellow circles show all candidates
3. **Reset if needed** - Press 'r' to restart tracking

### After Recording:
- The system will save `output_tracked.mp4` with the overlay
- Review the video to see trajectory trail
- Adjust config.py parameters if needed for your specific conditions

## Quick Adjustments if Needed

If you're getting too many false positives:
- Edit `config.py` → Increase `MIN_BALL_RADIUS` to 2 or 3
- Edit `ball_detector.py` → Tighten color thresholds

If ball is not being detected:
- Edit `config.py` → Decrease `MIN_BALL_RADIUS` to 1
- Edit `config.py` → Increase `MAX_DISTANCE` to 200

## Expected Performance

**Realistic Expectations:**
- ✅ Should work well for shots within 50-100 yards
- ⚠️ May struggle with very long shots (150+ yards)
- ⚠️ May have false positives in bright conditions
- ✅ Kalman filter will help maintain track through brief occlusions

**Best Case:** Slow-motion mode, steady camera, good lighting
**Worst Case:** Standard 30 FPS, handheld, very bright/overexposed conditions

Good luck on the course! 🏌️⛳
