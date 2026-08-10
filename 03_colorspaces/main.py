import os
import cv2

img = cv2.imread(os.path.join('assets', 'bird.jpg'))
img_rbg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('img_rbg', img_rbg)
cv2.imshow('img_gray', img_gray)

while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break