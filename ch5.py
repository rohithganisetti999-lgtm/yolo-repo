import cv2
import numpy as np

img = cv2.imread("resources/Clay Design.jpeg")

# Desired width and height of output
width, height = 250, 350

# Corners of the top-left card (A♦)
pts1 = np.float32([
    [0, 0],       # top-left
    [116, 0],     # top-right
    [116, 164],   # bottom-right
    [0, 164]      # bottom-left
])

# Destination points
pts2 = np.float32([
    [0, 0],
    [width, 0],
    [width, height],
    [0, height]
])

# Perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
imgOutput = cv2.warpPerspective(
    img,
    matrix,
    (width, height)
)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Card", imgOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()