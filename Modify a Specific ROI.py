import cv2
import numpy as np

def modify_roi(image_path, top_left, bottom_right, color):
    """
    Modify a specific region of interest (ROI) in an image by filling it with a solid color.

    Parameters:
        image_path (str): Path to the input image.
        top_left (tuple): (x, y) coordinates of the top-left corner of the ROI.
        bottom_right (tuple): (x, y) coordinates of the bottom-right corner of the ROI.
        color (tuple): BGR color values to fill the ROI.
    """
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Define the ROI coordinates
    x1, y1 = top_left
    x2, y2 = bottom_right

    # Ensure the ROI coordinates are within the image dimensions
    height, width = image.shape[:2]
    x1 = max(0, min(x1, width))
    y1 = max(0, min(y1, height))
    x2 = max(0, min(x2, width))
    y2 = max(0, min(y2, height))

    # Modify the ROI by filling it with the specified color
    image[y1:y2, x1:x2] = color

    # Display the original and modified images
    cv2.imshow('Modified Image', image)

    # Wait until a key is pressed, then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
modify_roi("C:/Users/kumar/Desktop/rl/sample.jpg", (50, 50), (200, 200), (0, 255, 0))  # Fill ROI with green color
