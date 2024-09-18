import cv2
import numpy as np

def add_text_watermark(image, text, position, font_scale=1, color=(255, 255, 255), thickness=2, alpha=0.5):
    # Make a copy of the image to avoid modifying the original
    overlay = image.copy()
    
    # Add text to the overlay image
    cv2.putText(overlay, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

    # Blend the overlay with the original image
    watermarked_image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    
    return watermarked_image

# Load the image
image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg")

# Define the text and its position
text = "Watermark"
position = (50, 50)  # x, y coordinates

# Add the text watermark
watermarked_image = add_text_watermark(image, text, position, font_scale=3, color=(255, 255, 0), thickness=4, alpha=0.9)

# Display the result
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
