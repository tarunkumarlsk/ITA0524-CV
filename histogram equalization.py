import cv2

image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg", cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)

cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
