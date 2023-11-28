from math import *
from tkinter import *

# Create a class named 'calculator' that inherits from 'Tk' (Tkinter's main window class)
class calculator(Tk):

    def __init__(self):

        # Initializing the class by calling the constructor of the superclass (Tk)
        super().__init__()

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
          "4", "5", "6", "*", "(", ")", "**",
          "1", "2", "3", "-", "=", ",", "0", ".", "min", "+", "sin", "asin", "cos", "acos", "tan",
          "pow", "log", "max", "abs", "floor", "pi", "e", "ln", "ceil", "degrees", "radians"]
        
        # Initializing row and column for the grid
        row, col = 1, 0
        padx, pady = 10, 10

        for i, txt in enumerate(values):

            # If the index is in a set of specific indices, move to the next row
            if i in {7, 14, 19, 26, 33}:
                row += 1
                col = 0

            # Creating '=' button with special background color
            if txt == '=':
                btn = Button(self, height=2, width=4, padx=70, pady=pady, text=txt, command=lambda t=txt: self.equals())
                btn.grid(row=row, column=col, columnspan=3, padx=2, pady=2)
                btn.configure(background="grey")
            elif txt in {'clear', 'AC'}:
                btn_text = 'C' if txt == 'clear' else 'AC'
                btn = Button(self, height=2, width=4, padx=padx, pady=pady, text=btn_text, command=lambda t=txt: self.delete() if t == 'clear' else self.clearall())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="red" if txt == 'clear' else "red")
            else:
                btn = Button(self, height=2, width=4, padx=padx, pady=pady, text=txt, command=lambda t=txt: self.addChar(t))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background=self.btn_bg_color)

            col += 1  # Moving to the next column
            i += 1  # Incrementing the index

        # Starting the main event loop
        self.mainloop()

    # Method to clear all input in the Entry widget

    def clearall(self):
        self.string.set("")

    # Method to evaluate the expression in the Entry widget and display the result
    def equals(self):
        result = ""

        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "ERR"
        self.string.set(result)

    # Method to add a character to the input in the Entry widget
    def addChar(self, char):
        self.string.set(self.string.get() + (str(char)))

    # Method to delete the last character in the input in the Entry widget
    def delete(self):
        self.string.set(self.string.get()[0:-1])
        


calculator()
