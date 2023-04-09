import glob
import os

def Remove_file(file_path:str=None):

    """
    Removing the input image file
    args:
    file_path:str
    """

    if file_path==None:
        file_path = "Attendance_data"
    else:
    	print("Enter the correct parent path")
    	

    Remove_file_name:str = input("Please Enter your name:")
    removing_files = glob.glob(f'{file_path}/{Remove_file_name}.png')
    for i in removing_files:
        os.remove(i)
        
Remove_file()
