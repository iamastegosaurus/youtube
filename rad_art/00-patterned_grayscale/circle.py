import cv2
import math

img = cv2.imread('Z:\\rad_art\\00-patterned_grayscale\\img.jpg')
copy = img.copy()
gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)

h, w, _ = img.shape 
r = h / 2

for j in range(h):

    theta = math.acos( (r - j) / r)
    a = r * math.sin(theta)

    left = w / 2 - a
    right = w / 2 + a

    for i in range(w):
        if i < left or i > right:
            img[j][i] = 0.299 * img[j][i][2] + 0.587 * img[j][i][1] + 0.114 * img[j][i][0] #[gray[j][i], gray[j][i], gray[j][i]]   


cv2.imshow('img', img)
cv2.waitKey(0)
# cv2.imwrite("final_circle.jpg", img)