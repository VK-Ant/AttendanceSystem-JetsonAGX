import threading
import os
import cv2
from deepface import DeepFace

folder_path = "/home/vk/Desktop/CVpractise/face_recognition/data"  # Replace with the path to your image folder
reference_images = [cv2.imread(os.path.join(folder_path, img)) for img in os.listdir(folder_path)]

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False


def check_face(frame):
    global face_match
    try:
        for reference_img in reference_images:
            if DeepFace.verify(frame, reference_img.copy())['verified']:
                face_match = True
                return
        face_match = False
    except ValueError:
        face_match = False


while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    key = cv2.waitKey(0)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
