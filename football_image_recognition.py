#import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/612133011/Downloads/opencv-master/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

team = cv2.imread('C:\\Users\\612133011\\Downloads\\football.jpg',1)

gray_img = cv2.cvtColor(team,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
# Box plotting for the face recognition
#          cv2.rectangle(team,(60,70),(100,125),(255,255,255),2)

# resizing of the image
#      resized = cv2.resize(team,(int (team.shape[1]*2),int(team.shape[0]*2)))

#      cv2.imshow('Football Germany Team',resized)

#print(type(faces))
#print(faces)

for x,y,w,h in faces:
    cv2.rectangle(team,(x,y),(x+w,y+h),(0,255,0),3)

#cv2.imshow('Football Germany Team',team)

resized = cv2.resize(team,(int (team.shape[1]*2),int(team.shape[0]*2)))

cv2.imshow('Football Germany Team',resized)

cv2.waitKey(0)

cv2.destroyAllWindows()