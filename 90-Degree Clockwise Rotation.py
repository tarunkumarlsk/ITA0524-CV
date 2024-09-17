import cv2

def rotate_image_90_clockwise(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Rotate the image 90 degrees clockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('90-Degree Clockwise Rotated Image', rotated_image)

    # Wait until a key is pressed, then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
rotate_image_90_clockwise("C:/Users/kumar/Desktop/rl/sample.jpg")
