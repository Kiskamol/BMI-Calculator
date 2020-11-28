from tkinter import *
import math

def leftClickButton(event):
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    Calculate = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if Calculate < 18.5:
        labelResult2.configure(text="ผอมเกินไป")
        labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    elif Calculate < 18.5 and Calculate > 22.9:
        labelResult2.configure(text="น้ำหนักปกติ เหมาะสม")
        labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    elif Calculate < 23.0 and Calculate > 24.9:
        labelResult2.configure(text="น้ำหนักเกิน")
        labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    elif Calculate < 25.0 and Calculate > 29.9:
        labelResult2.configure(text="อ้วน")
        labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    else :
        labelResult2.configure(text="อ้วนมาก")
        labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน",command = leftClickButton)
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ค่า BMI ของคุณ")
labelResult.grid(row=2,column=1)
labelResult2 = Label(MainWindow,text="รูปร่างของคุณ")
labelResult2.grid(row=3,column=0)


MainWindow.mainloop()