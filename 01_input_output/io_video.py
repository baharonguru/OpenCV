import os
import cv2

# read video
video_path = os.path.join('..', 'assets', 'dog.mp4')
video = cv2.VideoCapture(video_path)

# visualize video
ret = True
while ret:
    ret, frame = video.read()

    if not ret:
            break
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break