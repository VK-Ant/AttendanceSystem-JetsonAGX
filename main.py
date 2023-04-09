
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from datetime import date
import pytz
import csv


def identifyEncodings(images):
    '''
    Encoding is Recognition and comparing particular face in database or stored folder

    args:
    images:str
    '''
    
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    '''
    This function do two process
    1. Taken image name: vk.png -> vk
    2. Attendance entry in database or csv file
    
    args:
    name: str
    '''

    date = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%y_%m_%d||%H:%M")
    with open(f'Attendance_Entry/Attendance_{date}.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            print(dtString)
            date_i = now.strftime('%Y-%m-%d')

            print(date_i)
            f.writelines(f'\n{name},{dtString},{date_i}')

#  First create csv file in time and data
date = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%y_%m_%d||%H:%M")
print(date)
header = ("S.NO","Time","Date")

with open(f"Attendance_Entry/Attendance_{date}.csv","w") as file:
	writer = csv.writer(file)
	writer.writerow(header)

#Preprocessing the data 

path = 'Attendance_data'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
# split the data vk.png to vk
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

# Encoding of input image data
encodeListKnown = identifyEncodings(images)
print('Encoding Complete')


#Camera capture 
cap = cv2.VideoCapture('/dev/video0')

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    #Face recognition using dlib
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Attendance System', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
