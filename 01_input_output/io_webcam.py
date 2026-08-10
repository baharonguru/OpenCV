import cv2

# read webcam
webcam = cv2.VideoCapture(1)


# visualize webcam

while True:
    ret, frame = webcam.read()

    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.distroyAllWindows()