# NASA mock UI
# Edited by Jingzhe Chen & Anzhe Ye

from tkinter import *
import tkinter.messagebox

# fitting the LCD touch screen size
def center_window(w = 400, h = 300): 
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	root.geometry("%dx%d+%d+%d" % (w,h,x,y))


root = Tk(className = 'IPT_UI')

center_window(800,480)

# constructing frame of UI

txtlabel = Label(root, text = "Current Task", font=("Helvetica", 28),pady = 10)
txtlabel.grid(row = 0, column = 0, columnspan = 4)

left_part = Frame(root, height = 380, width = 400, bg = 'blue')
right_part = Frame(root, height = 380, width = 400, bg = 'green')

left_part.grid(row=1, column=0, columnspan = 2)
right_part.grid(row=1, column=2, columnspan = 2)

left_part.grid_propagate()
right_part.grid_propagate()

# setting buttons to switch tasks
BTN_prev = Button(root, text = 'previous', font = "Helvetica", width = 30)
BTN_list = Button(root, text = 'task list', font = "Helvetica", width = 30)
BTN_next = Button(root, text = 'next', font = "Helvetica", width = 30)

BTN_prev.grid(row=2, column=0, padx = 5, pady = 10)
BTN_list.grid(row=2, column=1, columnspan = 2, padx = 5, pady = 10)
BTN_next.grid(row=2, column=3, padx = 5, pady = 10)

cv1 = Canvas(left_part, width = 400, height = 380, bg = 'white')
cv2 = Canvas(right_part, width = 400, height = 380, bg = 'white')

cv1.create_rectangle(5,5,397,380);
cv1.pack();
cv2.create_rectangle(3,5,390,380);
cv2.pack();

cv1.create_text(60,40, text = " Task 6", font = ("Helvetica",30), tags = "txt")
cv1.create_text(200,150, text = "Take some samples ", font = ("Helvetica",30), tags = "txt")
cv1.create_text(200,180, text = "using the hammer...", font = ("Helvetica",30), tags = "txt")
cv1.create_text(200,280, text = "(click for more details)", font = ("Helvetica",26), tags = "txt")

cv2.create_text(150,100, text = "Completion Check :", font = ("Helvetica",28), tags = "txt")
cv2.create_text(150,180, text = "Working Status:", font = ("Helvetica",28), tags = "txt")

# in the condition of warning signal 
cv2.create_oval(300,75,350,125, fill = "red", tags = "circle")
cv2.create_text(200,220, text = "Warning", font = ("Helvetica",30), fill = "red", tags = "txt")
filename = PhotoImage(file = "warning.gif")
image = cv2.create_image(100, 320, image=filename)
cv2.create_text(260,330, text = "(click for details)", font = ("Helvetica",26), tags = "txt")

#try instead using parameter and using text from another file later...
def click_left(e):
	title = "Detail Instruction for task 6"# + str(num);
	tkinter.messagebox.showinfo(title, "1. Use the bluetooth and body camera to search the samples;\n2. Use the body camera to identify those target samples;\n3. Use the hammer to collect some samples.")

cv1.bind('<Button-1>', click_left)

# warning interface to be continued...








root.mainloop()