# -*- coding: utf-8 -*-
###################
#画布，使用Canvas小构件
###################
from tkinter import *

class CanvasDemo:
    def __init__(self):
        window = Tk() #创建窗口
        window.title("Canvas Demo") #给窗口命名

        #在窗口画布
        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()

        #创建frame的框架，窗口window为这个框架的父容器
        frame = Frame(window)
        frame.pack()
        #frame框架作为Button的父容器
        btRectangle = Button(frame, text="rectangle", command = self.displayRect)
        btOval = Button(frame, text = "Oval", command = self.displayOval)
        btArc = Button(frame, text = "Arc", command = self.displayArc)
        btPolygon = Button(frame, text = "Polygon", command = self.displayPolygon)
        btLine = Button(frame, text = "Line", command = self.displayLine)
        btString = Button(frame, text = "String", command = self.displayString)
        btClear = Button(frame, text = "Clear", command = self.displayClear)

        #Button在画布上布局
        btRectangle.grid(row = 1, column = 1)
        btOval.grid(row = 1, column = 2)
        btArc.grid(row = 1, column = 3)
        btPolygon.grid(row = 1, column = 4)
        btLine.grid(row = 1, column = 5)
        btString.grid(row = 1, column = 6)
        btClear.grid(row = 1, column = 7)

        #创建事件循环直到关闭主窗口
        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(10,10,190,90,tags = "rect")

    #fill填充oval的颜色
    def displayOval(self):
        self.canvas.create_oval(10,10,190,90, fill = "red", tags = "oval")

    # start为开始的度数，extent为要转的度数.全部以逆时针为正方向，0为x轴正方向
    def displayArc(self):
        self.canvas.create_arc(10,10,190,90, start = 0, extent = 90, width = 8, fill = "red",tags = "arc")

    def displayPolygon(self):
        self.canvas.create_polygon(10,10,190,90,10,90,tags = "polygon")

    #arrow表示line指向，activefill：当鼠标在line上时出现的特定风格，本例中鼠标移动到第二个line上时line变蓝
    def displayLine(self):
        self.canvas.create_line(10,10,190,90,fill = "red",tags = "line")
        self.canvas.create_line(10,90,190,10,width = 9,arrow = "first",activefill = "blue", tags = "line")

    #font定义字体（字体名，大小，风格）
    def displayString(self):
        self.canvas.create_text(60,40,text= "hi, i am string", font = "time 10 bold underline", tags = "string")

    #delete方法通过tags参数从画布上删除图形
    def displayClear(self):
        self.canvas.delete("rect","oval","arc","polygon","line","string")

CanvasDemo()