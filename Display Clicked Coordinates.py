import cv2

# List to store the coordinates of clicked points
points = []

def mouse_callback(event, x, y, flags, param):
    """
    Mouse callback function to capture and display coordinates of clicked points.

    Parameters:
        event: The type of the mouse event.
        x: The x-coordinate of the mouse event.
        y: The y-coordinate of the mouse event.
        flags: Any flags associated with the event.
        param: Additional parameters.
    """
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Point clicked: ({x}, {y})")
        # Draw a circle at the clicked point
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        # Display the coordinates on the image
        cv2.putText(image, f"({x}, {y})", (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.imshow('Image', image)

def display_coordinates(image_path):
    """
    Display the coordinates of points clicked on the image.

    Parameters:
        image_path (str): Path to the input image.
    """
    global image
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Create a window and set the mouse callback function
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', mouse_callback)

    # Display the image and wait for user interaction
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
display_coordinates("C:/Users/kumar/Desktop/rl/sample.jpg")
