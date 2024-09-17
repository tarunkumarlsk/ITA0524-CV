import cv2

image = cv2.imread("C:/Users/kumar/Desktop/rl/sample.jpg")

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Blurred Image', blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('blurred_image.jpg', blurred_image)
