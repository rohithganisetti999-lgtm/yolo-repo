import cv2
import numpy as np

# Read image
img = cv2.imread("resources/opencv.png")


# Function to stack multiple images
def stackImages(scale, imgArray):

    # Get number of rows and columns
    rows = len(imgArray)
    cols = len(imgArray[0])

    # Check whether image array contains multiple rows
    rowsAvailable = isinstance(imgArray[0], list)

    if rowsAvailable:

        # Loop through rows
        for x in range(0, rows):

            # Loop through columns
            for y in range(0, cols):

                # Check if image size is same as first image
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:

                    # Resize image using scale
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y],
                        (0, 0),
                        None,
                        scale,
                        scale
                    )

                else:

                    # Resize image to first image size
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y],
                        (
                            imgArray[0][0].shape[1],
                            imgArray[0][0].shape[0]
                        ),
                        None,
                        scale,
                        scale
                    )

                # Check if image is grayscale
                if len(imgArray[x][y].shape) == 2:

                    # Convert grayscale to BGR
                    imgArray[x][y] = cv2.cvtColor(
                        imgArray[x][y],
                        cv2.COLOR_GRAY2BGR
                    )

        # Stack images horizontally in each row
        hor = [np.hstack(imgArray[x]) for x in range(rows)]

        # Stack all rows vertically
        ver = np.vstack(hor)

    else:

        # Loop through images
        for x in range(0, rows):

            # Check if image size is same as first image
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:

                # Resize image using scale
                imgArray[x] = cv2.resize(
                    imgArray[x],
                    (0, 0),
                    None,
                    scale,
                    scale
                )

            else:

                # Resize image to first image size
                imgArray[x] = cv2.resize(
                    imgArray[x],
                    (
                        imgArray[0].shape[1],
                        imgArray[0].shape[0]
                    ),
                    None,
                    scale,
                    scale
                )

            # Check if image is grayscale
            if len(imgArray[x].shape) == 2:

                # Convert grayscale to BGR
                imgArray[x] = cv2.cvtColor(
                    imgArray[x],
                    cv2.COLOR_GRAY2BGR
                )

        # Stack images horizontally
        ver = np.hstack(imgArray)

    # Return final stacked image
    return ver


# Create 2x2 image stack
imgStack = stackImages(
    1,
    [[img, img],
     [img, img]]
)

# Display image
cv2.imshow("Image Stack", imgStack)

# Wait until a key is pressed
cv2.waitKey(0)