import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Sobel operator in the x direction
sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)  # dx=1, dy=0

# Apply Sobel operator in the y direction
sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)  # dx=0, dy=1

# Compute the magnitude of the gradient
sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Convert the magnitude to 8-bit to view the result
sobel_magnitude = np.uint8(255 * sobel_magnitude / np.max(sobel_magnitude))

# Display the result
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title('Sobel X')
plt.imshow(np.abs(sobel_x), cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Sobel Magnitude')
plt.imshow(sobel_magnitude, cmap='gray')

plt.show()
