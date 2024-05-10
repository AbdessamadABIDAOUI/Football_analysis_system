from utils import read_video , save_video
from trackers import tracker

def main():
    #read video
    video_frames = read_video('input_videos/trial1.mp4')
    #initialize Tracker
    Tracker = tracker('models/best.pt')
    tracks = Tracker.get_object_tracks(video_frames)

    #save video
    save_video(video_frames, 'output_videos/output_video.avi')
if __name__ == '__main__':
    main()