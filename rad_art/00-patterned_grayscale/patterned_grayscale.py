import cv2
import math

img = cv2.imread('img.jpg')
h, w, _ = img.shape

r = h / 2

video = cv2.VideoWriter('output.mp4', fourcc = cv2.VideoWriter_fourcc(*'DIVX'), fps=30, frameSize = (w, h))

for j in range(h):

    theta = math.acos( (r - j) / r)
    dist = r * math.sin(theta)

    left = w / 2 - dist
    right = w / 2 + dist

    for i in range(w):

        if i < left or i > right:

            img[j][i] = 0.299 * img[j][i][2] + 0.587 * img[j][i][1] + 0.114 * img[j][i][0]

    if j % 10 == 0:
        video.write(img)

cv2.imshow('title', img)
cv2.waitKey(0)

video.write(img)
video.release()
