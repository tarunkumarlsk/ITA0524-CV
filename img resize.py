import cv2

image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg")

smaller_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

larger_image = cv2.resize(image, (0, 0), fx=2.0, fy=2.0)

specific_size_image = cv2.resize(image, (800, 600))  

cv2.imshow('Original Image', image)
cv2.imshow('Smaller Image', smaller_image)
cv2.imshow('Larger Image', larger_image)
cv2.imshow('Specific Size Image', specific_size_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
