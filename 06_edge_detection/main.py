import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('assets', 'bird.jpg'))
img_edge = cv2.Canny(img, 200, 200)
img_edge_d = cv2.dilate(img_edge, np.ones((10, 10), dtype=np.int8))


cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)

while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break