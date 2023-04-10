# <h><center><b>FACE BASED ATTENDANCE SYSTEM USING NVIDIA JETSON AGX XAVIER</b></center></h>

![20230409_100542_1](https://user-images.githubusercontent.com/75832198/230754595-8df2c106-41a3-4782-acce-9d3b63601444.jpg)


## **Objective:**

A face based attendance system incorporates facial recognition technology to recognize and verify an employee’s or student facial features and to record attendance automatically. 

A facial recognition attendance system is a non-contact approach to managing employees in a business significantly when they are out on the field.

![6390a10c3644738a41e9b528_Face-Recognition](https://user-images.githubusercontent.com/75832198/230925305-f66ef39a-9be0-47e5-a14e-fb029578c6a6.jpeg)


## **STEPS TO FOLLOW IN THE PROJECT**

### **1. Git clone and change directory**

```bash
$ git clone https://github.com/VK-Ant/AttendanceSystem-JetsonAGX.git
$ cd AttendanceSystem-JetsonAGX
```
Make sure the path is correct.

### **2. Install requirement file**

```bash

$ pip3 install -r requirement.txt

```
Check that your AGX device has Opencv,numpy,dlib,cmake,datetime installed (Package).

### **3. Initially person image taken and stored in "Attendance_data" folder**

```bash
$ python3 initial_data_capture.py
```
After run the above cmd: Enter your name in terminal

Make sure your initial images stored in "Attendance_data" folder.

### **4. Attendance system (Main script)**

```bash
$ bash run.sh

or

$ python3 main.py
```

![b](https://user-images.githubusercontent.com/75832198/230757347-01e0a9a9-5799-4fd0-80e4-69de74837703.png)


## **Result's**

### **Output1: Face detection using dlib**

![vk](https://user-images.githubusercontent.com/75832198/230756159-20a50b3e-a8ee-4c14-9a51-5ac2c8a295ac.png)

### ***Output2: Automatically Attendance stored in Excel sheet***

![csv](https://user-images.githubusercontent.com/75832198/230755026-83840a34-af75-407f-9c64-46880c5928c0.png)

### **5. Remove image in "Attendance_data" folder**

```bash
$ python3 delete_image.py
```
After run the above cmd: Enter the name in terminal

Make sure image deleted or not in Attendance_data folder.

## **Project Description:**

1. Install requirement file.

2. Capture your input image of store it in "Attendance_data" folder. 

3. Next identify the faces in the given input data using DLIB library.

4. Then identify the face and store entry in excel sheet.

5. If you want to delete the image throughout the folder use 5th step mentioned above.

5. And finally automatically attendance stored in excel sheet(Name, Data, Time).

6. If you want remove the person data in database or data throught folder.


Thank you and credits,

1. Venkatesan (Providing Data and taking demo output video) 
2. BSS.Narayan (Providing the development kit)

## **🤗Happy learning🤗**
