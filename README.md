# OTP generator using Face recognition

To develop a robust security model OTP using Facial Co-ordinates through Machine Learning algorithms and cryptography.

FACE RECOGNITION:

Module used: OpenCV, dlib, Face_recognition.
Creating a dataset of user information like user’s images, name, phone
number, etc…
Loading the dataset like sample image to recognize the user.
Creating an array for face encoding and their names.
Processing a single frame of video.
Resizing the video for ¼ size for faster face recognition process.
Convert image from BGR color to RGB color.
Find all the images in face encoding using the frame of video.
Draw box around the face with label of his/her name on it.
Display the resulting image.


1.Data Preparation:
Collecting 100 images to store in the database for a new user

2.Preparing face file and training the model

3.Face verification:
OTP gets generated as soon as the face is matched.

4.Web Page for OTP verification
        When the correct OTP is entered:
         the OTP generated is encrypted using Triple DES algorithm explained
 
 When the incorrect OTP is entered:
   INCORRECT OTP
