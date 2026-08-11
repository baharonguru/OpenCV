import os
import cv2

img = cv2.imread(os.path.join('assets', 'birdflock.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting to gray scale
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV) # applying inverse threshold
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 1000:
        #cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 10)

cv2.imshow('img', img)
#cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)

while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break