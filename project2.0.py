import cv2
from ultralytics import YOLO

model = YOLO("best.pt")

# Enter your image path here
image_path = r"C:\Users\HP\Downloads\cv_frame_096.jpg.jpeg"

results = model(image_path, conf=0.5)

img = results[0].plot()

cv2.imshow("YOLO Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()