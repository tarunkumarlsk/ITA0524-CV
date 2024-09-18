import cv2
import numpy as np
from matplotlib import pyplot as plt

def roberts_cross(image):
    # Roberts Cross operator kernels
    kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    
    # Apply the kernels using OpenCV's filter2D function
    roberts_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    roberts_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)
    
    # Compute the magnitude of the gradient
    magnitude = np.sqrt(roberts_x**2 + roberts_y**2)
    
    return roberts_x, roberts_y, magnitude

# Load the image
image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Roberts Cross operator
roberts_x, roberts_y, roberts_magnitude = roberts_cross(gray)

# Normalize the result to 8-bit for display
roberts_magnitude = np.uint8(255 * roberts_magnitude / np.max(roberts_magnitude))

# Display the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title('Roberts X')
plt.imshow(np.abs(roberts_x), cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Roberts Magnitude')
plt.imshow(roberts_magnitude, cmap='gray')

plt.show()
