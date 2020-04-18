import cv2

front_face_cascade = cv2.CascadeClassifier("lbpcascade_frontalface.xml")
profile_face_cascade = cv2.CascadeClassifier("lbpcascade_profileface.xml")

videoCapture = cv2.VideoCapture(0)

scalefactor = 1.3

while 1:
    ret, pic = videoCapture.read()

    faces = front_face_cascade.detectMultiScale(pic, scalefactor, 5)
    faces1 = profile_face_cascade.detectMultiScale(pic, scalefactor, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(pic,(x , y),(x+w , y+h), (0,255,255), 2)

    for(x,y,w,h) in faces1:
        cv2.rectangle(pic,(x , y),(x+w , y+h), (0,255,255), 2)

    print("number of faces found {}",format(len(faces)))
    cv2.imshow("Face_Detection", pic)
    k = cv2.waitKey(30) & 0xff
    if k==2:
        break

cv2.destroyAllWindows()