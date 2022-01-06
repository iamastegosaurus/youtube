import cv2
import math

img = cv2.imread('Z:\\rad_art\\00-patterned_grayscale\\img.jpg')
h, w, _ = img.shape 
r = int(h / 2)

mid_x = int(w / 2)
mid_y = int(h / 2)


y_point = 300


white = (255, 255, 255)
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
thiccness = 3


theta = math.acos( (r - y_point) / r)
a = int((-r * math.sin(theta) ) + w / 2)
b = int((r * math.sin(theta) ) + w / 2)

cv2.line(img, (mid_x, mid_y), (mid_x, y_point), white, thiccness)
cv2.line(img, (mid_x, mid_y), (a, y_point), white, thiccness) # radius
cv2.line(img, (a, y_point), (mid_x, y_point), white, thiccness)


cv2.circle(img, (mid_x, mid_y), r, green, thiccness +3)

cv2.circle(img, (a, y_point), 4, red, thiccness +3)
cv2.circle(img, (b, y_point), 4, red, thiccness +3)

cv2.circle(img, (mid_x, y_point), 4, blue, thiccness +3)


# cv2.putText(img, "theta", (mid_x - 60, mid_y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, white, 2)

# radius_text_x = int(mid_x - a + 100)
# radius_text_y = int(mid_y)

# cv2.putText(img, "radius", (radius_text_x, radius_text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, white, 5)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite("Z:\\rad_art\\00-patterned_grayscale\\example2.jpg", img)