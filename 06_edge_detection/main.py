import os
import cv2
import numpy as np

# Dilation = Expands white areas (Connecting broken edges/text)
# Erosion = Shrinks white areas (Removing small background noise)
# Erode --> Dilate = Removes small background objects (Eliminating stray pixel specks)
# Dilate --> Erode = Fills small holes / gaps (Closing gaps inside an object)

img = cv2.imread(os.path.join('assets', 'bird.jpg'))
img_edge = cv2.Canny(img, 200, 200)
img_edge_d = cv2.dilate(img_edge, np.ones((10, 10), dtype=np.int8))
img_edge_e = cv2.erode(img_edge_d, np.ones((10, 10), dtype=np.int8))


cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)

while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break