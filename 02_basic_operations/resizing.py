import os
import cv2

img = cv2.imread(os.path.join('assets', 'bird.jpg'))

resized_img = cv2.resize(img, (640, 480))

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)

while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.waitKey(1)

