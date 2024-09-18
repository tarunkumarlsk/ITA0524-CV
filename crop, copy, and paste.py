import cv2

# Load the source image
image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg")

# Define the ROI coordinates (x, y, width, height)
x, y, w, h = 100, 100, 200, 200  # Example values

# Crop the ROI from the source image
roi = image[y:y+h, x:x+w]

# Define the location to paste the cropped ROI
paste_x, paste_y = 300, 300  # Top-left corner of the location to paste

# Ensure the ROI fits in the target area
if paste_y + h <= image.shape[0] and paste_x + w <= image.shape[1]:
    # Paste the ROI onto the source image
    image[paste_y:paste_y+h, paste_x:paste_x+w] = roi
else:
    print("ROI does not fit in the target area.")

# Display the results
cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
