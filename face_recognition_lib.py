import cv2
import mediapipe as mp
import face_recognition
import os

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Initialize the face detection module
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

# Load known faces and names
known_faces = []
known_names = []

images_folder = 'images'

for filename in os.listdir(images_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(images_folder, filename)
        image = face_recognition.load_image_file(img_path)
        face_encoding = face_recognition.face_encodings(image)[0]

        # Extract name from filename (assuming filename is in the format "Name.jpg")
        name = os.path.splitext(filename)[0]

        known_faces.append(face_encoding)
        known_names.append(name)

# Open the webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform face detection
    results = face_detection.process(rgb_frame)

    # Check if faces are detected
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)

            # Extract face encoding
            face_encoding = face_recognition.face_encodings(frame, [bbox])[0]

            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            name = "Unknown"

            # If a match is found, use the name of the first matching known face
            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]

            # Draw bounding box and name on the frame
            mp_drawing.draw_detection(frame, detection)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (bbox[0], bbox[1] - 10), font, 0.5, (255, 255, 255), 1)

    # Display the frame with detected faces and names
    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
