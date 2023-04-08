import cv2
import glob
import os
from datetime import datetime
from datetime import date
import numpy as np
import face_recognition
from datetime import datetime
from datetime import date

def Intial_data_capture(camera_id:int=None):

    """
    At first, a person's image was taken using a reference object.     
    
    args:
    camera_id : int
    """

    if camera_id == None:
        camera_id = 0
    
    Name:str = input("Please Enter your name:")

    camera = cv2.VideoCapture(camera_id)
    for i in range(1):
        return_value, image = camera.read()
        cv2.imwrite(f'{Name}'+'.png', image)
    del(camera)
    
def Remove_file(file_path:str=None):

    """
    Removing the input image file
    args:
    file_path:str
    """

    if file_path==None:
        file_path = "/home/vk/Desktop/AGX/Attendance/images"
    else:
        print("Enter the correct parent path")
        break

    Remove_file_name:str = input("Please Enter your name:")
    removing_files = glob.glob(f'{file_path}/{Remove_file_name}.jpg')
    for i in removing_files:
        os.remove(i)

def identifyEncodings(images):   
    '''
    Encoding is used for the compare the person to stored listed documents
    args: str
    '''
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):

    '''
    This procedure saves the attendance of every person in a csv file.    
    '''
    with open('Attendance.csv', 'r+') as f:
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

