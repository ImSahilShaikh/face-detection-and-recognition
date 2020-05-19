import schedule
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def job():	
	prev_cnt = 10
	curr_cnt = 8

	master = Tk()
	master.geometry("400x280")
	variable1=StringVar()

	def retrieve_input(master):
		if(var1.get() == 1 and var2.get() == 0):
			print("Current count : ", curr_cnt)
			master.destroy()
		elif((var1.get() == 0 and var2.get() == 0) or (var1.get() == 1 and var2.get() == 1)):
			messagebox.showwarning("Bad input","Illegal values, please try again")
			master.destroy()
			job()
		else:
			print("Previous count : ", prev_cnt)
			master.destroy()

	Label(master, text = "Previous count is : ").place(x = 50,y = 50)   
	Label(master, text = prev_cnt).place(x = 180,y = 50)

	Label(master, text = "Currnet count is : ").place(x = 210,y = 50)   
	Label(master, text = curr_cnt).place(x = 330,y = 50)

	button1 = tk.Button(master, text="Submit", command=lambda: retrieve_input(master))
	button1.place(x = 120, y = 140)

	button2 = tk.Button(master, text="QUIT", fg="red", command=master.destroy)
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
