import cv2
import numpy as np
from matplotlib import pyplot as plt

def prewitt_operator(image):
    # Prewitt operator kernels
    kernel_x = np.array([[-1, 0, 1], 
                         [-1, 0, 1], 
                         [-1, 0, 1]], dtype=np.float32)
    
    kernel_y = np.array([[-1, -1, -1], 
                         [0, 0, 0], 
                         [1, 1, 1]], dtype=np.float32)
    
    # Apply the kernels using OpenCV's filter2D function
    prewitt_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    prewitt_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)
    
    # Compute the magnitude of the gradient
    magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)
    
    return prewitt_x, prewitt_y, magnitude

# Load the image
image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Prewitt operator
prewitt_x, prewitt_y, prewitt_magnitude = prewitt_operator(gray)

# Normalize the result to 8-bit for display
prewitt_magnitude = np.uint8(255 * prewitt_magnitude / np.max(prewitt_magnitude))

# Display the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title('Prewitt X')
plt.imshow(np.abs(prewitt_x), cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Prewitt Magnitude')
plt.imshow(prewitt_magnitude, cmap='gray')

plt.show()
