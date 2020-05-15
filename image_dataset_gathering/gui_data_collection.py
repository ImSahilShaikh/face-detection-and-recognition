from tkinter import *
from tkinter import messagebox
import cv2
from random import randint
from PIL import ImageTk ,Image


def capture():
    cam = cv2.VideoCapture(0)
    i=0
    val=1
    while cam.isOpened():
        messagebox.showinfo("Info","Please look directly into camera and press ok")
        for i in range (15):
            ret, frame = cam.read()
            cv2.imwrite('img_data/'+str(val)+'.jpg',frame)
            val += 1
        
        messagebox.showinfo("Info","Please tilt you head towards left and press ok")
        for j in range(i,i+15):
            ret, frame = cam.read()
            cv2.imwrite('img_data/'+str(val)+'.jpg',frame)
            val += 1
        
        messagebox.showinfo("Info","Please tilt you head down and press ok")
        for k in range(j,j+15):
            ret, frame = cam.read()
            cv2.imwrite('img_data/'+str(val)+'.jpg',frame) 
            val += 1
        
        messagebox.showinfo("Info","Please tilt you head towards right and press ok")
        for l in range(k,k+15):
            ret, frame = cam.read()
            cv2.imwrite('img_data/'+str(val)+'.jpg',frame)
            val += 1
        
        messagebox.showinfo("Info","Please tilt you head up and press ok")
        for m in range(l,l+15):
            ret, frame = cam.read()
            cv2.imwrite('img_data/'+str(val)+'.jpg',frame)
            val += 1

        cam.release()
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        messagebox.showinfo("Info","Images captured successfully")

def terminate():
    messagebox.showinfo("Info","Thanks for using our system")
    exit()

myframe = Tk(className = " Window")
myframe.geometry("720x650")
myframe['background'] = '#f5f5f5'


img=ImageTk.PhotoImage(Image.open ("capture.jpg"))
lab=Label(image=img)

capture = Button(myframe, image = img, command = capture, activebackground  = '#3E4149')
capture.place(x = 50, y = 150)
capture.pack()
exit_b = Button(myframe, text = 'Exit', command = terminate)
exit_b.place(x = 150, y = 150)
exit_b.pack()
myframe.mainloop()
