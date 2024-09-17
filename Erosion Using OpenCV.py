import cv2
import numpy as np

def apply_erosion(image_path, kernel_size=(5, 5), iterations=1):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Create the erosion kernel
    kernel = np.ones(kernel_size, np.uint8)

    # Apply erosion
    eroded_image = cv2.erode(image, kernel, iterations=iterations)

    # Display the original and eroded images
    cv2.imshow('Original Image', image)
    cv2.imshow('Eroded Image', eroded_image)

    # Wait until a key is pressed, then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
apply_erosion("C:/Users/kumar/Desktop/rl/sample.jpg", kernel_size=(5, 5), iterations=1)
