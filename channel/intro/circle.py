import cv2
import math

img = cv2.imread('Z:\\channel\\intro\\img.jpg')
copy = img.copy()
gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)

h, w, _ = img.shape 
r = h / 2

for j in range(h):

    theta = math.acos( (r - j) / r)
    a = (-r * math.sin(theta) ) + w / 2
    b = (r * math.sin(theta) ) + w / 2

    for i in range(w):
        if i < a or i > b:
            img[j][i] = [gray[j][i], gray[j][i], gray[j][i]]   

    if j % 10 == 0:
        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        filename = 'Z:\\channel\\intro\\frames\\' + str(j) + ".jpg"
        print(filename)
        cv2.imwrite(filename, img)

cv2.imwrite('Z:\\channel\\intro\\frames\\' + str(h) + ".jpg", img)