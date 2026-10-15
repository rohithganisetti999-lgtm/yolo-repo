import cv2
from ultralytics import YOLO

# Load the YOLOv8 pretrained model
model = YOLO("yolov8n.pt")

# Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    # Read a frame from the webcam
    success, frame = cap.read()

    if not success:
        print("Error: Could not read camera frame")
        break

    # Detect objects in the current webcam frame using the YOLOv8 model.
    # 'frame' contains the image captured by the webcam.
    # 'model' is the pretrained YOLOv8 Nano model loaded earlier.
    # 'conf=0.5' sets the confidence threshold to 50%.
    # Only detections with a confidence score of 0.5 or higher
    # are retained in the results.
    results = model(frame, conf=0.5)

    # Draw the detection results on the current webcam frame.
    # 'results[0]' accesses the results for the first image in the
    # prediction batch (here, we process one webcam frame at a time).
    # '.plot()' draws bounding boxes around detected objects,
    # displays their class names, and shows confidence scores.
    # The annotated image is returned as a NumPy array.
    # 'annotated_frame' stores this image for display in the webcam window.
    annotated_frame = results[0].plot()

    # Display the output
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()