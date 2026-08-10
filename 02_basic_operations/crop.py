import os
import cv2

img = cv2.imread(os.path.join('assets', 'bird.jpg'))

print(img.shape)

cropped_img = img[800:2900, 2400:3850]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)

while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
