import cv2
import numpy as np

def find_contour_coordinates(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding or edge detection (e.g., Canny)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # Alternatively, you can use Canny edge detection
    # edges = cv2.Canny(gray, 100, 200)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create a copy of the original image to draw contours on
    contour_image = image.copy()
    
    # Iterate over the contours and print their coordinates
    for i, contour in enumerate(contours):
        print(f"Contour {i + 1} coordinates:")
        for point in contour:
            x, y = point[0]
            print(f"({x}, {y})")
            # Draw the contour on the image (optional)
            cv2.circle(contour_image, (x, y), 1, (0, 255, 0), -1)
    
    # Display the original image with contours (optional)
    cv2.imshow('Contours', contour_image)
    
    # Wait until a key is pressed, then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
find_contour_coordinates("C:/Users/kumar/Desktop/rl/sample.jpg")