import schedule
import time
from tkinter import *
import tkinter as tk
cnt = 4

def job():
	master = Tk()
	master.geometry("400x280")
	variable1=StringVar()

	def retrieve_input(master):
		ans = variable1.get()
		if(ans == "yes"):
			print("Current count : ", cnt)
			master.destroy()
		else:
			print("Previous count : ", cnt)
			schedule.every(1).minutes.do(job)
			master.destroy()

	Label(master, text = "Currnet count is : ").place(x = 130,y = 50)   
	Label(master, text = cnt).place(x = 250,y = 50)

	button1 = tk.Button(master, text="Submit", command=lambda: retrieve_input(master))
	button1.place(x = 120, y = 140)

	button2 = tk.Button(master, text="QUIT", fg="red", command=master.destroy)
	button2.place(x = 220, y = 140) 

	count = Label(master, text = "Lock count (yes/ no)? :").place(x = 30,y = 100)  
	e1 = Entry(master,width = 20,textvariable=variable1).place(x = 180, y = 100)  

	mainloop()

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
