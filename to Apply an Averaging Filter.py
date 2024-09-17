import cv2
import numpy as np

def apply_averaging_filter(image_path, kernel_size=(5, 5)):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Create the averaging kernel
    kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

    # Apply the averaging filter
    smoothed_image = cv2.filter2D(image, -1, kernel)

    # Display the original and smoothed images
    cv2.imshow('Original Image', image)
    cv2.imshow('Smoothed Image', smoothed_image)

    # Wait until a key is pressed, then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
apply_averaging_filter("C:/Users/kumar/Desktop/rl/sample.jpg", kernel_size=(5, 5))
