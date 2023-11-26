from math import *
from tkinter import *

class calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title('Scientific Calculator')
        # Setting up the main window properties
        self.title('Scientific Calculator')
        self.geometry('400x400')
        self.configure(background="white")

        # Creating a StringVar to store the input and result in the Entry widget
        self.string = StringVar()

        # Creating the Entry widget for user input        
        entry = Entry(self, textvariable=self.string, font=('Arial', 18), bd=10, insertwidth=12, width=12, justify='right')
        entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=10)
        entry.configure(background="white")
        self.btn_bg_color = 'white' # Background color for buttons
        entry.focus() # Setting focus to the Entry widget

        # List of button values
        values = ["7", "8", "9", "/", "%", "clear", "AC",
          "4", "5", "6", "", "(", ")", "*",
          "1", "2", "3", "-", "=", ",", "0", ".", "min", "+", "sin", "asin", "cos", "acos", "tan",
          "pow", "log", "max", "abs", "floor", "pi", "e", "ln", "ceil", "degrees", "radians"]
calculator()
