import cv2
import sys
import numpy as np
import urllib.request
from win32api import GetSystemMetrics

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

while True:

    # Capture frame-by-frame
    #retval, frame = video_capture.read()
    imgr=urllib.request.urlopen("http://192.168.43.1:8080/shot.jpg")
    imgnp=np.array(bytearray(imgr.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    # Convert to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Detect features specified in Haar Cascade
    faces = faceCascade.detectMultiScale(
       gray,
       scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    )

    # Draw a rectangle around recognized faces 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50,1000), 5)

    # Display the resulting frame
    cv2.imshow('Video',cv2.resize(frame,(GetSystemMetrics(0)-700,GetSystemMetrics(1)-400)))

    # Exit the camera view
    if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       video_capture.release() 
       sys.exit() 
