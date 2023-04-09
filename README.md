# **Face based Attendance system using Nvidia AGX Jetson**

![20230409_100542_1](https://user-images.githubusercontent.com/75832198/230754595-8df2c106-41a3-4782-acce-9d3b63601444.jpg)

## ***What steps you have to follow in this project***

### **1. Git clone and change directory**

```bash
$ git clone https://github.com/VK-Ant/AttendanceSystem-JetsonAGX.git
$ cd AttendanceSystem-JetsonAGX
```
Make sure your terminal is located in the  directory AttendanceSystem-JetsonAGX

### **2. Install reuirementfile**

```bash

$ pip3 install -r requirement.txt

```
Check that your AGX device has Opencv,numpy,dlib,cmake,datetime installed.

### **3. Initially person image stored in database or folder**

```bash
$ python3 initial_data_capture.py
```
After run the above cmd: Enter your name in terminal

Make sure your intial images stored in Attendance_data folder

### **4. Attendance System and automatically data entried into Excel sheet - Main script**

```bash
$ bash run.sh

or

$ python3 main.py
```

![b](https://user-images.githubusercontent.com/75832198/230757347-01e0a9a9-5799-4fd0-80e4-69de74837703.png)


## **Finally,Result shows**

### **Output: i. Face detection using dlib**

![vk](https://user-images.githubusercontent.com/75832198/230756159-20a50b3e-a8ee-4c14-9a51-5ac2c8a295ac.png)

### ***Output: ii. Automatically Attendance stored in Excel sheet***

![csv](https://user-images.githubusercontent.com/75832198/230755026-83840a34-af75-407f-9c64-46880c5928c0.png)

### **5. Remove the person's photograph from the database or folder**

```bash
$ python3 delete_image.py
```
After run the above cmd: Enter the name in terminal

Make sure image is delete or not in Attendance_data folder

## **Project explaination**

1. Install requirement file

2. first identify the face using face recognition library

3. store the data for Attendance_data folder

4. Then identify the face store the name for database or attendance_data folder

5. And finally automatically attendance stored in excel sheet(Name, Data, Time)

6. If you want remove the person data in database or data throught folder


Thankyou and credits,

1. My friends Venkatesan and bala
2. Bss. Narayan (Providing the development kit)

## **🤗Happy learning🤗**
