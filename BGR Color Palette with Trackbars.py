import cv2
import numpy as np

def nothing(x):
    pass

def bgr_color_palette():
    # Create a black image
    image = np.zeros((300, 300, 3), dtype=np.uint8)

    # Create a window named 'BGR Color Palette'
    cv2.namedWindow('BGR Color Palette')

    # Create trackbars for B, G, and R channels
    cv2.createTrackbar('Blue', 'BGR Color Palette', 0, 255, nothing)
    cv2.createTrackbar('Green', 'BGR Color Palette', 0, 255, nothing)
    cv2.createTrackbar('Red', 'BGR Color Palette', 0, 255, nothing)

    while True:
        # Get the current positions of the trackbars
        blue = cv2.getTrackbarPos('Blue', 'BGR Color Palette')
        green = cv2.getTrackbarPos('Green', 'BGR Color Palette')
        red = cv2.getTrackbarPos('Red', 'BGR Color Palette')

        # Set the color of the image based on the trackbar positions
        image[:] = [blue, green, red]

        # Display the image
        cv2.imshow('BGR Color Palette', image)

        # Break the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy all windows
    cv2.destroyAllWindows()

# Example usage
bgr_color_palette()
