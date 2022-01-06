import cv2
import math

img = cv2.imread('Z:\\channel\\intro\\img.jpg')
copy = img.copy()
gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)

h, w, _ = img.shape 
r = h / 2

video = cv2.VideoWriter("Z:\\channel\\intro\\output.mp4", 
fourcc = cv2.VideoWriter_fourcc(*'DIVX'), 
fps=30, 
frameSize=(w, h))


# writer = cv2.VideoWriter(filename="my_video.avi",  #Provide a file to write the video to
# fourcc=cv2.cv.CV_FOURCC('i','Y', 'U', 'V'),            #Use whichever codec works for you...
# fps=15,                                        #How many frames do you want to display per second in your video?
# frameSize=(width, height)) 

for j in range(h):

    theta = math.acos( (r - j) / r)
    a = (-r * math.sin(theta) ) + w / 2
    b = (r * math.sin(theta) ) + w / 2

    for i in range(w):
        if i < a or i > b:
            img[j][i] = [gray[j][i], gray[j][i], gray[j][i]]   

    if j % 10 == 0:
        video.write(img)  

video.write(img)  
video.release()
