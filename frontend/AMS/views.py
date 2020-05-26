from django.shortcuts import render
from AMS.forms import StudentForm
from AMS.models import Student
from django.http import HttpResponse
import os
from django.conf import settings
import cv2
from random import randint
# Create your views here.


import datetime
import mtcnn
from matplotlib import pyplot
from mtcnn.mtcnn import  			
from matplotlib.patches import Rectangle
import schedule
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def stud(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect()
			except:
				pass
	else:
		form = StudentForm()
	return render(request,"index.html",{'form':form})


def adminLogin(request):
	if request.method == 'POST':
		user = request.POST['username']
		passw = request.POST['password']
		if(user == 'admin' and passw=='123'):
			students = Student.objects.all()
			return render(request,"index.html",{'students':students})
		else:
			return render(request,"login.html")	

def login(request):
	return render(request,"login.html")

def captureImages(request):
	rno = request.POST['rollno']
	name = request.POST['name']
	folder = rno+'_'+name
	os.mkdir(os.path.join('Datasets/', folder))
	cam = cv2.VideoCapture(0)
	i=0
	val=1
	while cam.isOpened():
	    #messagebox.showinfo("Info","Please look directly into camera and press ok")
	    for i in range (75):
	        ret, frame = cam.read()
	        cv2.imwrite('Datasets/'+folder+'/'+name+'_'+str(val)+'.jpg',frame)
	        val += 1
	    cam.release()
	    if cv2.waitKey(30) & 0xFF == ord('q'):
	        break
	    #messagebox.showinfo("Info","Images captured successfully")
	#exit()
	students = Student.objects.all()
	return render(request,"index.html",{'students':students})	


def StartSystem(request):
	prev_cnt = 0
	curr_cnt = 0


	def job():	
		try:
			valRead = open("img_val.txt", "r+")
		except IOError:
			valRead = open("img_val.txt", "w+")
			valRead.close()
			valRead = open("img_val.txt", "r+")

		text = valRead.read()
		if(text == ''):
			valRead.close()
			valRead = open("img_val.txt", "w")
			valRead.write('1')
			valRead.close()
		else:
			val = int(text)
			val = val + 1
			valRead.close()
			valRead = open("img_val.txt", "w")
			valRead.write(str(val))
			valRead.close()
		valRead = open("img_val.txt", "r")
		val = int(valRead.read())
		valRead.close()
		filename = 'capture.jpg'

		videoCaptureObject = cv2.VideoCapture(0)

		ret, frame = videoCaptureObject.read()
		if ret:
			detector = MTCNN()
			cv2.imwrite(filename,frame)
			pixels = pyplot.imread(filename)
			faces = detector.detect_faces(pixels)
			os.remove(filename)
		videoCaptureObject.release()
		cv2.destroyAllWindows()
		
		master = Tk()
		master.geometry("400x280")
		variable1=StringVar()
		global prev_cnt
		global curr_cnt

		try:
			f = open("output.txt", "r")
		except IOError:
			f = open("output.txt", "w+")
			x = datetime.datetime.now()
			f.writelines('{0} \t {1} \t {2}\n'.format(len(faces), 0,x))
			f.close()		

		with open("output.txt", "r") as f:
			data = f.readlines()
		lastline = data[-1]
		tail = data[-10:]
		f.close()
		day = lastline.split()[2]
		timee = lastline.split()[3]
		prev_cnt = int(lastline.split()[1])
		# curr_cnt = int(lastline.split()[0])
		# prev_cnt = curr_cnt
		curr_cnt = len(faces)
		def retrieve_input(master):
			global prev_cnt
			global curr_cnt
			f = open("output.txt", "a+")
			if(var1.get() == 1 and var2.get() == 0):			
				prev_cnt = curr_cnt
				x = datetime.datetime.now()
				f.writelines('{0} \t {1} \t {2}\n'.format(curr_cnt, prev_cnt,x))
				f.close()
				print("Current count : ", curr_cnt)
				print("Previous count : ", prev_cnt)
				master.destroy()
			elif((var1.get() == 0 and var2.get() == 0) or (var1.get() == 1 and var2.get() == 1)):
				messagebox.showwarning("Bad input","Illegal values, please try again")
				master.destroy()
				job()
			else:
				print("Previous count : ", prev_cnt)
				x = datetime.datetime.now()
				f.writelines('{0} \t {1} \t {2}\n'.format(prev_cnt, 0,x))
				f.close()
				master.destroy()

		Label(master, text = "Previous count is : ").place(x = 50,y = 50)   
		Label(master, text = prev_cnt).place(x = 180,y = 50)

		Label(master, text = "Currnet count is : ").place(x = 210,y = 50)   
		Label(master, text = curr_cnt).place(x = 330,y = 50)

		button1 = tk.Button(master, text="Submit", command=lambda: retrieve_input(master))
		button1.place(x = 120, y = 140)

		#button2 = tk.Button(master, text="QUIT", fg="red", command=master.destroy)
		button2 = tk.Button(master, text="QUIT", fg="red", command=quit)
		button2.place(x = 220, y = 140) 

		var1 = IntVar()
		Checkbutton(master, text="Lock Count", variable=var1).place(x = 30,y = 100)
		var2 = IntVar()
		Checkbutton(master, text="Use Previous count", variable=var2).place(x = 180, y = 100)

		mainloop()
		
	schedule.every(0.1).minutes.do(job)

	while True:
	    schedule.run_pending()
	    time.sleep(1)
	students = Student.objects.all()
	return render(request,"index.html",{'students':students})			