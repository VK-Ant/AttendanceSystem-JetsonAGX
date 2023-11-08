#pip install mtcnn, opencv-python, deepface
import threading
import os
import cv2
from deepface import DeepFace
from mtcnn.mtcnn import MTCNN
import time

folder_path = "/home/vk/Desktop/CVpractise/face_recognition/data"  # Replace with the path to your image folder
reference_images = {os.path.splitext(img)[0]: cv2.imread(os.path.join(folder_path, img)) for img in os.listdir(folder_path)}

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
start_time = time.time()

face_match = False


def check_face(frame):
    global face_match
    try:
        detector = MTCNN()
        results = detector.detect_faces(frame)

        for result in results:
            x, y, w, h = result['box']
            face_img = frame[y:y+h, x:x+w]
            for name, reference_img in reference_images.items():
                if DeepFace.verify(face_img, reference_img.copy())['verified']:
                    face_match = True
                    return name
            face_match = False
            return None
    except ValueError:
        face_match = False
        return None


while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                name = threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass

        # Face detection using MTCNN
        detector = MTCNN()
        results = detector.detect_faces(frame)

        for result in results:
            x, y, w, h = result['box']
            confidence = result['confidence']

            # Draw bounding box around detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Label name for detected face
            if face_match:
                cv2.putText(frame, f"Match: {name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "No Match", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        counter += 1

        # Calculate and display FPS
        fps = 1 / (time.time() - start_time)
        cv2.putText(frame, f"FPS: {fps:.2f}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('video', frame)

        # Update start time for the next FPS calculation
        start_time = time.time()

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
