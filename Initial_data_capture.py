import cv2

def Intial_data_capture(camera_id:int=None):

    """
    At first, a person's image was taken using a reference object.     
    
    args:
    camera_id : int
    """
    path = "Attendance_image"
    if camera_id == None:
        camera_id = 0
    
    Name:str = input("Please Enter your name:")

    camera = cv2.VideoCapture(camera_id)
    for i in range(1):
        return_value, image = camera.read()
        cv2.imwrite(f'path/{Name}'+'.png', image)
    del(camera)
    
Intial_data_capture()