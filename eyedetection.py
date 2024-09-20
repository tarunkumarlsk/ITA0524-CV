import cv2

# Load the Haar Cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load the image
image = cv2.imread('/Users/manoj/Desktop/face.jpg')  # Replace 'face.jpg' with your image path

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# For each detected face, detect eyes
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face_roi = gray[y:y + h, x:x + w]
    face_color = image[y:y + h, x:x + w]

    # Detect eyes within the face region
    eyes = eye_cascade.detectMultiScale(face_roi)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Display the result
cv2.imshow('Eye Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()