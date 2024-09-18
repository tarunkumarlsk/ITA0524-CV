import cv2
from matplotlib import pyplot as plt

# Load the image in grayscale
image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg", cv2.IMREAD_GRAYSCALE)

# Define the threshold value and maximum value
threshold_value = 127  # Change this value to suit your needs
max_value = 255

# Apply Binary Thresholding
_, binary_thresh = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Binary Thresholding')
plt.imshow(binary_thresh, cmap='gray')

plt.show()
