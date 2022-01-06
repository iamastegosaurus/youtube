import cv2
import numpy as np


w, h = 300, 300

color1 = (255, 255, 0)
color2 = (0, 255, 0)


image = np.zeros((h, w, 3), np.uint8)

for i in range (w):
    for j in range(h):

        if j > i:
            image[j][i] = color1
        else:
            image[j][i] = color2



cv2.imshow('img', image)
cv2.waitKey(0)