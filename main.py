from utils import read_video,save_video
from trackers import Tracker
import cv2

def main():
    #read video
    video_frames = read_video(r'input_videos\08fd33_4.mp4')

    #initialise the tracker
    tracker = Tracker(r"models\best.pt")

    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True,stub_path= r'stubs\track_stubs.pkl')

    #save cropped image of a player
    for track_id, player in tracks['players'][0].items():
        bbox=player['bbox']
        frame = video_frames[0]
        cropped_image  = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
        cv2.imwrite(f'output_videos/cropped_image.jpg', cropped_image)
        break


    #Draw output
    ##Draw object_tracks
    output_video_frames = tracker.draw_annotation(video_frames,tracks)

    #save video
    save_video(output_video_frames,'output_videos/output_videos.avi')

if __name__== "__main__":
    main()