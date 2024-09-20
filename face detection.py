import cv2

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam (you can replace '0' with a video file path if needed)
cap = cv2.imread(r"/Users/manoj/Desktop/face.jpg")


while True:
    
    # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=18, minSize=(30, 30))
    
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(cap, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the output
    cv2.imshow('Face Detection', cap)
    
    # Exit when the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
