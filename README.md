# **FACE BASED ATTENDANCE SYSTEM USING NVIDIA JETSON AGX XAVIER DEVICE**

![20230409_100542_1](https://user-images.githubusercontent.com/75832198/230754595-8df2c106-41a3-4782-acce-9d3b63601444.jpg)


## **OBJECTIVE:**

1. A face based attendance system incorporates facial recognition technology to recognize and verify an employee’s or student facial features and to record attendance automatically. 

2. A facial recognition attendance system is a non-contact approach to managing employees in a business significantly, when they are out on the field.


## **STEPS TO FOLLOW IN THIS PROJECT:**

### **1. Git clone and change directory**

```bash
$ git clone https://github.com/VK-Ant/AttendanceSystem-JetsonAGX.git
$ cd AttendanceSystem-JetsonAGX
```
Make sure the path is correct.

### **2. Install prerequisite library using requirement file**

```bash

$ pip3 install -r requirement.txt

```
Check that Opencv,numpy,dlib,cmake, and datetime are installed on your AGX device (Packages).

### **3. Take a picture of your input and save it to the "Attendance_data" folder.**

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

### **Output1: Face recognition**

![vk](https://user-images.githubusercontent.com/75832198/230756159-20a50b3e-a8ee-4c14-9a51-5ac2c8a295ac.png)

### ***Output2: Automatically Attendance stored in Excel sheet***

![csv](https://user-images.githubusercontent.com/75832198/230755026-83840a34-af75-407f-9c64-46880c5928c0.png)

### **5. Remove image in "Attendance_data" folder**

```bash
$ python3 delete_image.py
```
After run the above cmd: Enter the name in terminal

Make sure image deleted or not in Attendance_data folder.

## **PROJECT DESCRIPTION:**

1. Install requirement file.

2. Capture your input image of store it in "Attendance_data" folder. 

3. Next Recognized faces in the given input data using DLIB library.

4. Then Attendance entered in excel sheet.

5. If you want to delete the image throughout the folder use 5th step mentioned above.


### **THANK YOU & CREDIT**

1. HarishKumar, Venkatesan (Providing Data and taking demo output video) 
2. BSS.Narayan (Providing the development kit)

## **🤗Happy learning🤗**
