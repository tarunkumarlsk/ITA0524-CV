import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg", cv2.IMREAD_GRAYSCALE)

# Define a structuring element (kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))  # You can change the size and shape

# Apply the Black Hat operation
black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Display the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Black Hat Operation')
plt.imshow(black_hat, cmap='gray')

plt.show()
