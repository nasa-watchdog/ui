# NASA mock UI
# Edited by Jingzhe Chen & Anzhe Ye

from tkinter import *
import tkinter.messagebox
# import time

Title = ["Task 1", "Task 2","Task 3","Task 4","Task 5","Task 6","Task 7"]
txt = ["Place the plastic marker or approach the site as near as possible...", "Lay down the stick...", "Take pictures...", "Record temperature...", "Record air pressure and weather...","Take some samples using the hammer...", "Prepare for go to the next position..."]

TSK = ["1. Place your marker at target point.\n\nOR\n\n2. Approach the site as near as possible until system gets the Bluetooth signal",
       "1. Lay down the stick on the ground.\n\n2.Make sure the body camera can capture the stick.",
       "1. Take the pictures of the stick on the ground.",
       "1. Use the Probe Thermometer to measure the temperature of target point.\n\n2.Make sure the body camera can capture the Probe Thermometer.",
       "1. Use the Barometer to measure the air pressure of target point.\n\n2.Make sure the body camera can capture the Barometer.",
       "1. Use the bluetooth and body camera to search the samples;\n\n2. Use the body camera to identify those target samples;\n\n3. Use the hammer to collect some samples.",
       "1. Leave the current position and go to the next position.\n\n2. Make sure you have left the detecting area of Bluetooth."]

Status = ["In-progress", "Done", "Waiting", "Warning"]
color = ["Yellow", "Green", "Grey", "Red"]
Case_save = [1,1,1,1,3,2,2]

emmm = [0,0,0,0,0,0,0]
imgDict = {}


class TaskWindow:
	
	# fitting the LCD touch screen size
	def center_window(self, w = 400, h = 300): 
		ws = self.root.winfo_screenwidth()
		hs = self.root.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		self.root.geometry("%dx%d+%d+%d" % (w,h,x,y))

	def __init__(self, num, c):
		self.n = num
		self.case = c
		self.root = Tk(className = 'IPT_UI')
		self.center_window(800,440)

		# constructing frame of UI

		txtlabel = Label(self.root, text = "Current Task", font=("Helvetica", 28),pady = 5)
		txtlabel.grid(row = 0, column = 0, columnspan = 4)

		left_part = Frame(self.root, height = 350, width = 380)
		right_part = Frame(self.root, height = 350, width = 380)

		left_part.grid(row=1, column=0, columnspan = 2)
		right_part.grid(row=1, column=2, columnspan = 2)

		left_part.grid_propagate()
		right_part.grid_propagate()

		# setting buttons to switch tasks
		BTN_prev = Button(self.root, text = 'previous', font = "Helvetica", width = 25, command = self.OnBack)
		BTN_list = Button(self.root, text = 'task list', font = "Helvetica", width = 25, command = self.ToList)
		BTN_next = Button(self.root, text = 'next', font = "Helvetica", width = 25, command = self.OnNext)

		BTN_prev.grid(row=2, column=0, padx = 5, pady = 10)
		BTN_list.grid(row=2, column=1, columnspan = 2, padx = 5, pady = 10)
		BTN_next.grid(row=2, column=3, padx = 5, pady = 10)

		cv1 = Canvas(left_part, width = 380, height = 340, bg = 'white')
		cv2 = Canvas(right_part, width = 380, height = 340, bg = 'white')

		cv1.create_rectangle(5,5,377,337)
		# cv1.pack()
		cv2.create_rectangle(3,5,377,337)
		# cv2.pack()

		cv1.create_text(70,40, text = Title[self.n], font = ("Helvetica",30))
		cv1.create_text(180,150, text = txt[self.n], width = 340, font = ("Helvetica",20))
		
		cv1.create_text(180,260, text = "(click for more details)", font = ("Helvetica",20))

		cv1.bind('<Button-1>', self.ShowDetail)

		cv2.create_text(150,100, text = "Completion Check :", font = ("Helvetica",20))
		cv2.create_text(150,180, text = "Working Status:", font = ("Helvetica",20))

		# in the condition of warning signal 
		cv2.create_oval(280,75,330,125, fill = color[self.case], tags = "circle")
		cv2.create_text(220,220, text = Status[self.case], font = ("Helvetica",20), fill = color[self.case])

		if self.case == 3:
			filename = PhotoImage(file = 'warning.gif', master = self.root)
			imgDict['warning.gif'] = filename
			image = cv2.create_image(80,280, image=filename)
			cv2.create_text(230,310, text = "(click for details)", font = ("Helvetica",20))

		cv1.pack()
		cv2.pack()

	def OnNext(self):
		Case_save[self.n] = self.case
		if self.n == 6:
			win = FinalWindow()
			self.root.destroy()
		else:
			if (Case_save[self.n] == 1) and (Case_save[self.n+1] == 2):
				win = TaskWindow((self.n + 1)%7,0)
				self.root.destroy()
			else:
				win = TaskWindow((self.n + 1)%7,Case_save[self.n+1])
				self.root.destroy()
		# win.root.after(5000,win.Signal_Update)
		

	def OnBack(self):
		Case_save[self.n] = self.case
		if self.n == 0:
			title = "System Information"
			tkinter.messagebox.showwarning(title, "Warning! It is the first Task.")
		
		else:
			win = TaskWindow((self.n - 1)%7,Case_save[self.n-1])
			self.root.destroy()
		# win.root.after(5000,win.Signal_Update)

	def ToList(self):
		Case_save[self.n] = self.case
		win = ListWindow()
		self.root.destroy()

	def ShowDetail(self,event):
		Case_save[self.n] = self.case
		win = DetailWindow(self.n)
		self.root.destroy()
		# win.root.after(5000,win.Signal_Update)

	# def Signal_Update(self):
	# 	if Case_save[self.n] == 2:
	# 		Case_save[self.n] = 0
	# 	elif Case_save[self.n] == 0:
	# 		if self.n == 5:
	# 			Case_save[self.n] = 3
	# 		else:
	# 			Case_save[self.n] = 1
	# 	elif Case_save[self.n] == 3:
	# 		Case_save[self.n] = 1
	# 		win = TaskWindow((self.n),Case_save[self.n])
	# 		self.root.destroy()
	# 		win.root.after(5000,win.Signal_Update)

class DetailWindow:

	# fitting the LCD touch screen size
	def center_window(self, w = 400, h = 300): 
		ws = self.root.winfo_screenwidth()
		hs = self.root.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		self.root.geometry("%dx%d+%d+%d" % (w,h,x,y))

	def __init__(self, num):
		self.n = num
		self.root = Tk(className = 'IPT_UI')
		self.center_window(800,440)

		# constructing frame of UI
		main = Frame(self.root, height = 400, width = 800)
		main.grid(row=0, column=0)
		main.grid_propagate()
		BTN_back = Button(self.root, text = 'Back', font = "Helvetica", width = 25, command = self.ToTask)
		BTN_back.grid(row=1, column=0, padx = 5, pady = 10)
		CVM = Canvas(main, width = 800, height = 400, bg = 'white')
		CVM.create_rectangle(5,5,795,395)
		CVM.pack()
		CVM.create_text(190,40, text = "Current Task Detail:", font = ("Helvetica",30))
		CVM.create_text(350,220, text = TSK[self.n],width = 660, font = ("Helvetica",24))
		

	def ToTask(self):
		win = TaskWindow(self.n, Case_save[self.n])
		self.root.destroy()
		# win.root.after(5000,win.Signal_Update)

class FinalWindow:
	# fitting the LCD touch screen size
	def center_window(self, w = 400, h = 300): 
		ws = self.root.winfo_screenwidth()
		hs = self.root.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		self.root.geometry("%dx%d+%d+%d" % (w,h,x,y))

	def __init__(self):
		self.root = Tk(className = 'IPT_UI')
		self.center_window(800,440)
		# constructing frame of UI
		main = Frame(self.root, height = 400, width = 800)
		main.grid(row=0, column=0, columnspan =3)
		main.grid_propagate()
		BTN_Back = Button(self.root, text = 'Back', font = "Helvetica", width = 25, command = self.Back)
		BTN_Review = Button(self.root, text = 'Review', font = "Helvetica", width = 25, command = self.Review)
		BTN_Check = Button(self.root, text = 'Check', font = "Helvetica", width = 25, command = self.Check)
		BTN_Back.grid(row=1, column=0, padx = 5, pady = 10)
		BTN_Review.grid(row=1, column=1, padx = 5, pady = 10)
		BTN_Check.grid(row=1, column=2, padx = 5, pady = 10)
		CVF = Canvas(main, width = 800, height = 400, bg = 'white')
		CVF.create_rectangle(5,5,795,395)
		CVF.create_text(400,200,text = "The End", font = ("Helvetica",40))
		CVF.pack()

	def Back(self):
		# self.root.destroy()
		win = TaskWindow(6,Case_save[6])
		self.root.destroy()

	def Review(self):
		win = ListWindow()
		self.root.destroy()

	def Check(self):
		titlE = "System Information"
		if Case_save == [1,1,1,1,1,1,1]:
			tkinter.messagebox.showinfo(titlE,"Congratulations!\n\nYou have finished all tasks!",parent = self.root)
		else:
			tkinter.messagebox.showinfo(titlE,"Sorry, you have not accomplished all tasks yet!\nPlease review and finish all tasks:)",parent = self.root)

class ListWindow:
	# fitting the LCD touch screen size
	def center_window(self, w = 400, h = 300): 
		ws = self.root.winfo_screenwidth()
		hs = self.root.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		self.root.geometry("%dx%d+%d+%d" % (w,h,x,y))

	def __init__(self):
		self.root = Tk(className = 'IPT_UI')
		self.center_window(720,440)
		# constructing frame of UI

		BTN_T1 = Button(self.root, text = 'Task 1', font = "Helvetica", width = 80,height = 1, command = self.T1)
		BTN_T2 = Button(self.root, text = 'Task 2', font = "Helvetica", width = 80,height = 1, command = self.T2)
		BTN_T3 = Button(self.root, text = 'Task 3', font = "Helvetica", width = 80,height = 1, command = self.T3)
		BTN_T4 = Button(self.root, text = 'Task 4', font = "Helvetica", width = 80,height = 1, command = self.T4)
		BTN_T5 = Button(self.root, text = 'Task 5', font = "Helvetica", width = 80,height = 1, command = self.T5)
		BTN_T6 = Button(self.root, text = 'Task 6', font = "Helvetica", width = 80,height = 1,  command = self.T6)
		BTN_T7 = Button(self.root, text = 'Task 7', font = "Helvetica", width = 80,height = 1, command = self.T7)
		BTN_T1.grid(row=0, column=0, padx = 5, pady = 5)
		BTN_T2.grid(row=1, column=0, padx = 5, pady = 5)
		BTN_T3.grid(row=2, column=0, padx = 5, pady = 5)
		BTN_T4.grid(row=3, column=0, padx = 5, pady = 5)
		BTN_T5.grid(row=4, column=0, padx = 5, pady = 5)
		BTN_T6.grid(row=5, column=0, padx = 5, pady = 5)
		BTN_T7.grid(row=6, column=0, padx = 5, pady = 5)

	def T1(self):
		win = TaskWindow(0,Case_save[0])
		self.root.destroy()
	def T2(self):
		win = TaskWindow(1,Case_save[1])
		self.root.destroy()
	def T3(self):
		win = TaskWindow(2,Case_save[2])
		self.root.destroy()
	def T4(self):
		win = TaskWindow(3,Case_save[3])
		self.root.destroy()
	def T5(self):
		win = TaskWindow(4,Case_save[4])
		self.root.destroy()
	def T6(self):
		win = TaskWindow(5,Case_save[5])
		self.root.destroy()
	def T7(self):
		win = TaskWindow(6,Case_save[6])
		self.root.destroy()
		

win = TaskWindow(0,Case_save[0])
# win.root.after(1000,win.Signal_Update)
win.root.mainloop()


