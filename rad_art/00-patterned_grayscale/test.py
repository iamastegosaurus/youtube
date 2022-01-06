import cv2


img = cv2.imread('Z:\\rad_art\\00-patterned_grayscale\\img.jpg')
copy = img.copy()
gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
h, w, _ = img.shape 

customGray = gray.copy()

for j in range(h):
    for i in range(w):
        customGray[j][i] = 0.299 * img[j][i][2] + 0.587 * img[j][i][1] + 0.114 * img[j][i][0]

cv2.imshow('img', gray)
cv2.imshow('custom', customGray)
cv2.waitKey(0)