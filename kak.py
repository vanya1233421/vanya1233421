import sys
from threading import current_thread
from tkinter import *
import webbrowser
from tkinter import messagebox
import time

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()
 #СТРОКА
    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#D3D3D3", foreground="#000000")
        self.lbl.place(x=20, y=50)

  #ОЦЕНКА
        def ocenkacom (): 
            def okk ():
                def vvv ():
                    library.destroy()
                    messagebox.showinfo('Отзыв', 'Спасибо за вашу оценку, вы помогаете стать нам лучше')  

                oke = Button (library, text = "Оценил", command = vvv)
                oke.place (x = 170, y = 120)
            library = Tk ()
            library.title ("Оцени нас!")
            library.geometry ("420x175")
            def Quit():
                pass
            library.protocol("WM_DELETE_WINDOW", Quit)
            library.resizable(width=False, height=False)
            lib = Label (library, text = "Поставь здесь свою оценку, помоги нам стать лучше.", font = 10, foreground= "#000000")
            lib.place (x = 17, y = 1)
            radioValue = IntVar()
            rdioOne = Radiobutton(library, text='5',variable=radioValue, value=1,font = 20, command = okk) 
            rdioTwo = Radiobutton(library, text='4',variable=radioValue, value=2, font = 20,command = okk) 
            rdioThree = Radiobutton(library, text='3',variable=radioValue, value=3, font = 20,command = okk)
            rdio4 = Radiobutton(library, text='2',variable=radioValue, value=4, font = 20,command = okk)
            rdio5 = Radiobutton(library, text='1',variable=radioValue, value=5, font = 20,command = okk)
        
            rdioOne.place (x = 30, y = 40)
            rdioTwo.place (x = 100, y = 40)
            rdioThree.place (x = 170, y = 40)
            rdio4.place (x = 240, y = 40)
            rdio5.place (x = 310, y = 40)
            
            
        ocen = Button (root, text = "Оцените нас", font = ("Courier New", 8, "bold"), bg="#DCDCDC", foreground="#000000", command = ocenkacom)
        ocen.place (x = 375, y = 544)
            

        #ЦИФРЫ
        def click (): 
            webbrowser.open_new_tab("https://github.com/vanya1233421/vanya1233421/commit/9b6cd1d86a468a61b2ce16e28ee8bd24b31debbc")
            
        txtkode = "код"
        kod = Button (root, text = txtkode, command = click)
        kod.place (x=445, y=10)
        def timing():
            current_time = time.strftime("%H : %M : %S")
            clock.config(text=current_time)
            clock.after(200,timing)
        clock=Label(root,font=("times",15,"bold"),bg="#D3D3D3")
        clock.place (x = 10, y = 542)
        timing()

       

        
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
    def logicalc(self,operation):
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
        
 
 #ОКНО
if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#D3D3D3"
    root.geometry("485x570+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    kalkc = Main(root)
    kalkc.pack()
    root.mainloop()
