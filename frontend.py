import tkinter as tk
from PIL import ImageTk, Image
import os
import time
import svgutils
import svgutils.transform as sg

class MainApp:
    def __init__(self, parent, names):
        self.startTime = 0
        self.finishTime = 800
        self.parent = parent
        self.frame = tk.Frame(self.parent, bg = "white")
        self.frame2 = tk.Frame(self.parent,bg = "white")

        #FRAME 1
        self.chkValue = tk.BooleanVar()
        self.chkValue.set(False)
        self.selectButton = tk.Checkbutton(self.frame, bg = "white",text ="Select/Deselect all", bd = 0,font ="Helvetica 14", var = self.chkValue, command = self.selectAll)
        self.selectButton.pack(side = tk.TOP, anchor = tk.W)

        self.buttons = []
        self.colours = []
        self.values = []
        
        for name in names:
            value = tk.BooleanVar()
            value.set(False)
            self.values.append(value)

            button = tk.Checkbutton(self.frame, text = name,bg = "white", bd =0, font ="Helvetica 14",var = value)
            button.pack(side = tk.TOP, anchor = tk.W)
            self.buttons.append(button)

      
        


        
       #FRAME 2
        self.slider = tk.Scale(self.frame2, bd = 0,bg = "white",from_= self.startTime, to = self.finishTime, length = 800, orient = tk.HORIZONTAL)
        self.sliderStart = tk.Label(self.frame2, bg = "white", text = "time 0")
        self.sliderStart.pack(side = tk.LEFT)
        self.sliderFinish = tk.Label(self.frame2, bg = "white", text = "time 100")
        self.sliderFinish.pack(side = tk.RIGHT)
        self.slider.pack()
        self.frame.pack()
        self.frame2.pack(side = tk.BOTTOM)

 

    def selectAll(self):
        for value in self.values:
            if value.get() == self.chkValue.get():
                continue
            value.set(not value.get())
        
class Room:
    self __init__(self, x1 = 0, x2 = 0, y1 = 0, y2 = 0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
       
               
   

def main():
    fig = sg.fromfile('C:/Users/Bryan/Documents/GitHub/MartelloMurder/floorsvg.svg')
    txt1 = sg.TextElement(25,20, "A", size=12, weight="bold")
    txt2 = sg.TextElement(375.3,17.8672, "B", size=12, weight="bold")
    fig.append([txt1, txt2])
    fig.save("C:/Users/Bryan/Documents/GitHub/MartelloMurder/finalfloorsvg.svg")
    people = ["Veronica", "Jason", "Thomas", "Rob", "Kristina", "Marc-Andre", "Dave", "Salina", "Harrison", "Alok", "Eugene", "James"]
    root = tk.Tk()
    app = MainApp(root, people)
    root.mainloop()

if __name__ == '__main__':
    main()
