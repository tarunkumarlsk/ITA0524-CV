import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/manoj/Desktop/dataset-cover.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve circle detection
gray_blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Hough Circle detection
circles = cv2.HoughCircles(gray_blurred, 
                           cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, 
                           param1=50, param2=30, 
                           minRadius=20, maxRadius=50)

# If any circle is detected, draw them on the image
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Draw the outer circle
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw the center of the circle
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

# Display the result
cv2.imshow('Detected Watch', image)
cv2.waitKey(0)
cv2.destroyAllWindows()