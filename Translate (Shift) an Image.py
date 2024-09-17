import cv2
import numpy as np

def translate_image(image_path, tx, ty):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Define the translation matrix
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

    # Apply the translation
    translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

    # Display the original and translated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Translated Image', translated_image)

    # Wait until a key is pressed, then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
translate_image("C:/Users/kumar/Desktop/rl/sample.jpg", tx=50, ty=100)
