import cv2
import face_recognition
import numpy as np


E = face_recognition.load_image_file("/home/augray-ai/Desktop/face/images/e.jpg")
cvt1= cv2.cvtColor(E,cv2.COLOR_BGR2RGB)
J_Test = face_recognition.load_image_file(r"/home/augray-ai/Desktop/face/images/e1.jpg")
cvt2 = cv2.cvtColor(J_Test,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(E)[0]
encodeElon = face_recognition.face_encodings(E)[0]
cv2.rectangle(E, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(J_Test)[0]
encodeTest = face_recognition.face_encodings(J_Test)[0]
cv2.rectangle(J_Test, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 255, 255), 2)

results = face_recognition.compare_faces([encodeElon], encodeTest) #backend is linear svm used
#print(results)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDis)
cv2.putText(J_Test, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 1)

cv2.imshow('Elon Musk', E)
cv2.imshow('M',J_Test)
cv2.waitKey(0)

#cv2.imshow("Elon",E)
##cv2.imshow("Ma",j)
#cv2.imshow("cvtE",cvt1)
#cv2.imshow("cvtM",cvt2)
#cv2.waitKey(0)
