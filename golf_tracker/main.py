"""Main entry point for golf ball tracker"""
import sys
from video_processor import VideoProcessor

def main():
    print("=" * 50)
    print("Golf Ball Tracker")
    print("=" * 50)
    
    # Choose mode
    print("\nSelect mode:")
    print("1. Process video file")
    print("2. Live camera tracking")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        video_path = input("Enter video file path: ").strip()
        output_path = input("Enter output path (default: output_tracked.mp4): ").strip()
        if not output_path:
            output_path = 'output_tracked.mp4'
        
        processor = VideoProcessor(video_path)
        processor.process_video(output_path)
        
    elif choice == '2':
        camera_id = input("Enter camera ID (default: 0): ").strip()
        camera_id = int(camera_id) if camera_id else 0
        
        processor = VideoProcessor("")
        processor.process_live(camera_id)
    
    else:
        print("Invalid choice")
        return
    
    print("\nProcessing complete!")


if __name__ == "__main__":
    main()
