from deepface import DeepFace

# Provide the folder path containing images for face recognition
folder_path = r"/home/vk/Desktop/CVpractise/face_recognition/data/"

# Perform face recognition
result = DeepFace.verify(folder_path, enforce_detection=False)

# Print the result
print(result)
