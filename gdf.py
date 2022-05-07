
from tkinter import *
import webbrowser
 
class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()
 #СТРОКА
    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#D3D3D3", foreground="#000000")
        self.lbl.place(x=20, y=50)
 #ЦИФРЫ
        def click (): 
            webbrowser.open_new_tab("https://github.com/vanya1233421/vanya1233421/commit/9b6cd1d86a468a61b2ce16e28ee8bd24b31debbc")
            
        txtkode = "Код"
        kod = Button (root, text = txtkode, command = click)
        kod.place (x=445, y=10)
     
        knopki = [ 
            "C", "DEL", "x²", "*",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "=",
                    
        ]
        
        x = 10
        y = 140
        for bt in knopki :
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#C0C0C0",
                   font=("Bahnschrift", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81
 #ОПЕРАЦИИ
    def logicalc(self, kod, operation):
        if operation == "C":
            self.formula = " "
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "x²":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()
  
 
    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)
 
 
if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#D3D3D3"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
