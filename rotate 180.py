import cv2

def rotate_image_180_y_axis(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    flipped_image_1 = cv2.flip(image, 1)  

    flipped_image_2 = cv2.flip(flipped_image_1, 1)

    cv2.imshow('Original Image', image)
    cv2.imshow('180-Degree Y-Axis Rotated Image', flipped_image_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
rotate_image_180_y_axis("C:/Users/kumar/Desktop/rl/sample.jpg")
