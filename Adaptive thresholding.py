import cv2
from matplotlib import pyplot as plt

# Load the image in grayscale
image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Adaptive Mean Thresholding
adaptive_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY, 11, 2)

# Apply Adaptive Gaussian Thresholding
adaptive_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 11, 2)

# Display the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Adaptive Mean Thresholding')
plt.imshow(adaptive_mean, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Adaptive Gaussian Thresholding')
plt.imshow(adaptive_gaussian, cmap='gray')

plt.show()
