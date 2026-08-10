import os
import cv2

img = cv2.imread(os.path.join('assets', 'whiteboard.png'))
print("Image shape (H, W, C):", img.shape)

# line
# Starts at (50, 50), ends at (200, 300), color, thickness
cv2.line(img, (50, 50), (200, 300), (0, 255, 0), 3)

# recangle
# Top-left at (250, 80), Bottom-right at (450, 300), color, thickness
cv2.rectangle(img, (250, 80), (450, 300), (0, 255, 0), 4)

# circile
# Center at (580, 200), Radius = 60, color, thickness
cv2.circle(img, (580, 200), 60, (255, 0, 0), 5)

# text
# (image, text, bottom-left origin, font, scale, color, thickness)
cv2.putText(img, 'Hey you!', (330, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

cv2.imshow('img', img)

while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break