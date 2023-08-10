from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.task = ""
        self.userIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg="#5BC8AC", bd=29,
                                insertwidth=4, width=24,
                                font=("Verdana", 20, "bold"), textvariable=self.userIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)
        self.user_input.insert(0, "0")

        # ... Button creation code ...
         #button for value 7
        self.button1 = Button(self, bg= "#98dbc6" , bd=12,
                              text="7", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("7"))
        self.button1.grid(row=2, column=0, sticky=W)

#button for value 8
        self.button2 = Button(self, bg= "#98dbc6" , bd=12,
                              text="8", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("8"))
        self.button2.grid(row=2, column=1, sticky=W)

#button for value 9
        self.button3 = Button(self, bg= "#98dbc6" , bd=12,
                              text="9", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("9"))
        self.button3.grid(row=2, column=2, sticky=W)

#button for value 4
        self.button4 = Button(self, bg= "#98dbc6" , bd=12,
                              text="4", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("4"))
        self.button4.grid(row=3, column=0, sticky=W)

#button for value 5
        self.button5 = Button(self, bg= "#98dbc6" , bd=12,
                              text="5", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("5"))
        self.button5.grid(row=3, column=1, sticky=W)


        #button for value 6
        self.button6 = Button(self, bg= "#98dbc6" , bd=12,
                              text="6", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("6"))
        self.button6.grid(row=3, column=2, sticky=W)
        
#button for value 3
        self.button7 = Button(self, bg= "#98dbc6" , bd=12,
                              text="1", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("1"))
        self.button7.grid(row=4, column=0, sticky=W)



#button for value 2
        self.button8 = Button(self, bg= "#98dbc6" , bd=12,
                              text="2", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("2"))
        self.button8.grid(row=4, column=1, sticky=W)


        #button for value 1
        self.button9 = Button(self, bg= "#98dbc6" , bd=12,
                              text="3", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("3"))
        self.button9.grid(row=4, column=2, sticky=W)
        

        #button for value 0
        self.button10 = Button(self, bg= "#98dbc6" , bd=12,
                              text="0", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("0"))
        self.button10.grid(row=5, column=0, sticky=W)


        #button for add
        self.addbutton = Button(self, bg= "#98dbc6" , bd=12,
                              text="+", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("+"))
        self.addbutton.grid(row=2, column=3, sticky=W)


        #button for value sub
        self.subbutton = Button(self, bg= "#98dbc6" , bd=12,
                              text="-", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("-"))
        self.subbutton.grid(row=3, column=3, sticky=W)
        
#button for value mul
        self.mulbutton = Button(self, bg= "#98dbc6" , bd=12,
                              text="*", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("*"))
        self.mulbutton.grid(row=4, column=3, sticky=W)


        #button for value div
        self.divbutton = Button(self, bg= "#98dbc6" , bd=12,
                              text="/", padx=33,pady=25,font=("Helvetica", 20, "bold",),
                              command=lambda: self.buttonClick("/"))
        self.divbutton.grid(row=5, column=3, sticky=W)

        # button for value equal
        self.equalbutton = Button(self, bg="#E6D72A", bd=12,
                                  text="=", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                  command=lambda: self.buttonClick("="))
        self.equalbutton.grid(row=5, column=1, sticky=W, columnspan=2)

        # button for value clear
        self.clearbutton = Button(self, bg="#E6D72A", bd=12,
                                  text="AC", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                  command=self.clearDisplay)
        self.clearbutton.grid(row=1, sticky=W, columnspan=4)

    def buttonClick(self, value):
        if value == "=":
            self.calculateTask()
        else:
            self.task += str(value)
            self.userIn.set(self.task)

    def calculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = str(self.answer)
        except SyntaxError:
            self.displayText("Invalid Syntax")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def clearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

calculator = Tk()
calculator.title("Calculator")
app = Application(calculator)
calculator.resizable(width=False, height=False)
calculator.mainloop()
