import cv2
import numpy as np
img=cv2.imread("resources/opencv.png")
print(img.shape)
img_resize=cv2.resize(img,(300,450))
print(img_resize.shape)
crop_image=img[0:200,200:500]
cv2.imshow("orgImg",img)
cv2.imshow("ResizeImg",img_resize)
cv2.imshow("cropimage",crop_image)
cv2.waitKey(0)