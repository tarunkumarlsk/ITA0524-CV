import cv2

def rotate_image_270_y_axis(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Flip the image horizontally (along the y-axis)
    flipped_image = cv2.flip(image, 1)  # 1 means flipping around the y-axis

    # Rotate the flipped image 270 degrees clockwise
    rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 270 clockwise = 90 counterclockwise

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('270-Degree Y-Axis Rotated Image', rotated_image)

    # Wait until a key is pressed, then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
rotate_image_270_y_axis("C:/Users/kumar/Desktop/rl/sample.jpg")
