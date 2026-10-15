import cv2
import numpy as np

widthImg = 640
heightImg = 480
cap = cv2.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10, 150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, 100, 200)   # lower < upper
    Kernel = np.ones((5,5), np.uint8)         # use uint8
    imgDial = cv2.dilate(imgCanny, Kernel, iterations=2)
    imgThres = cv2.erode(imgDial, Kernel, iterations=1)
    return imgThres

while True:
    success, img = cap.read()
    img = cv2.resize(img, (widthImg, heightImg))
    imgThres = preProcessing(img)
    cv2.imshow("Result", imgThres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   # <-- only break here

cap.release()
cv2.destroyAllWindows()
