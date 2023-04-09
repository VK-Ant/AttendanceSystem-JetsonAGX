import cv2

def Intial_data_capture(camera_id=None):

    """
    At first, a person's image was taken using a reference object.     
    
    args:
    camera_id : int
    """
    path = "Attendance_Data/"
    if camera_id == None:
     	camera_id = '/dev/video0'
    
    Name:str = input("Please Enter your name:")

    camera = cv2.VideoCapture(camera_id)
    for i in range(10):
        return_value, image = camera.read()
        cv2.imwrite(f'{path}{Name}'+'.png', image)
    del(camera)
    
Intial_data_capture()
