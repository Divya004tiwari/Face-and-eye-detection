import cv2
import sys

def main():
    # Load the pre-trained Haar cascades for face and eye detection
    # OpenCV provides these XML files, typically located in the cv2 data folder
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    eye_cascade_path = cv2.data.haarcascades + 'haarcascade_eye.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    if face_cascade.empty() or eye_cascade.empty():
        print("Error loading cascade classifiers. Make sure opencv-python is installed correctly.")
        sys.exit(1)

    # Initialize the video capture object (0 is usually the default laptop camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        sys.exit(1)

    print("Starting camera... Press 'q' to quit.")

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Convert the frame to grayscale, as face detection works better on grayscale images
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Loop over all detected faces
        for (x, y, w, h) in faces:
            # Draw a blue rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # Region of Interest (ROI) for eyes within the face
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # Detect eyes within the face region
            eyes = eye_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(15, 15)
            )

            # Loop over all detected eyes
            for (ex, ey, ew, eh) in eyes:
                # Draw a green rectangle around the eyes
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                cv2.putText(roi_color, 'Eye', (ex, ey - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display the resulting frame
        cv2.imshow('Face and Eye Detection', frame)

        # Wait for 1 millisecond and check if the user pressed the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
