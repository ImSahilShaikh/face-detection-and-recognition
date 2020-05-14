from tkinter import *
from tkinter import messagebox
import cv2
import os

def capture():
    cam = cv2.VideoCapture(0)
    i=0
    while True:
        ret, frame = cam.read()
        cv2.imshow("Test",frame)
        messagebox.showinfo("Info","Please look directly into camera and press ok")
        for i in range (15):
            cv2.imwrite('img_data/img{:>03}.jpg'.format(i),frame)
        
        messagebox.showinfo("Info","Please tilt you head towards left and press ok")
        for j in range(i+15):
            cv2.imwrite('img_data/img{:>03}.jpg'.format(j),frame)
        
        messagebox.showinfo("Info","Please tilt you head down and press ok")
        for k in range(j+15):
            cv2.imwrite('img_data/img{:>03}.jpg'.format(k),frame)     
        
        messagebox.showinfo("Info","Please tilt you head towards right and press ok")
        for l in range(k+15):
            cv2.imwrite('img_data/img{:>03}.jpg'.format(l),frame)
        
        messagebox.showinfo("Info","Please tilt you head up and press ok")
        for m in range(l+15):
            cv2.imwrite('img_data/img{:>03}.jpg'.format(m),frame)

        cam.release()
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        messagebox.showinfo("Info","Images captured successfully")

def terminate():
    messagebox.showinfo("Info","Thanks for using our system")
    exit()

myframe = Tk(className = " Window")
myframe.geometry("500x250")
myframe['background'] = '#f5f5f5'

capture = Button(myframe, text = "Capture", command = capture, activebackground  = '#3E4149')
capture.place(x = 50, y = 150)
exit_b = Button(myframe, text = 'Exit', command = terminate)
exit_b.place(x = 150, y = 150)
myframe.mainloop()
