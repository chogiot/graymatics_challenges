import cv2
import numpy as np
import sys


def video_capture(video):
    cap = cv2.VideoCapture(video)

    amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    video_duration = amount_of_frames/fps

    start_pos = 30
    end_pos = 35
    start_frame=float( start_pos*amount_of_frames/video_duration)
    end_frame=float( end_pos*amount_of_frames/video_duration )
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)


    # success, image = cap.read()
    while(cap.isOpened()):
        success, image = cap.read()
        if success:
            img = cv2.rectangle(image, (width//2-50, height//2+50), (width//2+50, height//2-50), (0, 0, 255), 5)
            cv2.imshow('frame',img)
            cv2.waitKey(1)
            if cap.get(cv2.CAP_PROP_POS_FRAMES) > end_frame:
                break
        else:
            break

    cap.release()

if __name__ == "__main__":
    video = sys.argv[1]
    video_capture(video)
