import cv2
import numpy as np
#5,5 is matrix size
kernel=np.ones((5,5),np.uint8)
img=cv2.imread("resources/opencv.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(19,19),1)
img_canny=cv2.Canny(img,100,150)
#dilation-thickness increases
img_dilation=cv2.dilate(img_canny,kernel,iterations=1)

cv2.imshow("Gray Image",img_gray)
cv2.imshow("Blur Image",img_blur)
cv2.imshow("Canny Image",img_canny)
cv2.imshow("Dilation Image",img_dilation)
cv2.waitKey(0)