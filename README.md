from calendar import c
from multiprocessing.spawn import old_main_modules
import sys
from threading import current_thread
from tkinter import *
import webbrowser
from tkinter import messagebox
import time
from tkinter import Menu
import requests
from bs4 import BeautifulSoup
from datetime import date
import tkinter as tk
import random


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()
 #СТРОКА
    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#D3D3D3", foreground="#000000")
        self.lbl.place(x=20, y=50)

    #ИНФО      
        def pll ():
            library1 = Tk ()
            library1.title ("О приложении")
            library1.resizable(width=False, height=False)
            library1.geometry ("475x175")
            lib1 = Label (library1, text = "Калькулятор (латинского «счётчик») — электронное вычислительное устрой-", foreground="#2F4F4F", font = ("Bahnschrift", 10) )
            lib2 = Label (library1, text = "ство для выполнения операций над числами или алгебраическими формулами.", foreground= "#2F4F4F", font = ("Bahnschrift", 10) )
            lib3 = Label (library1, text = "Автор:", font = 1, foreground="#008B8B")
            lib4 = Label (library1, text = "Березнев Иван", font  = 1, foreground= "#008B8B")
            lib5 = Label (library1, text = "Защищено авторискими правами \n ГК РФ Статья 1255")
            lib1.place (x = 0, y = 0)
            lib2.place (x = 0, y = 20)
            lib3.place (x = 0, y = 40)
            lib4.place (x = 0, y = 60)
            lib5.place (x = 275, y = 135)
            

            
        def click (): 
            webbrowser.open_new_tab("https://github.com/vanya1233421/vanya1233421/commit/9b6cd1d86a468a61b2ce16e28ee8bd24b31debbc")
        
        def exx ():
            sys.exit ()

        #КУРС
        def doll ():
            dol = Tk()
            dol["bg"] = "#C0C0C0"
            dol.title ("Доллар")
            dol.resizable(width=False, height=False)
            dol.geometry ("200x100")
            url = "https://quote.rbc.ru/ticker/72413"
            sours = requests.get (url)
            main_text = sours.text
            sop = BeautifulSoup (main_text, "html.parser")
            late = sop.findAll ("span", {"class": "chart__info__sum"})
            tetxt = (late [0].text)
            kdk = Label (dol, text  = tetxt, font = 100, bg = "#C0C0C0", foreground= "#800000")
            kdk1 = Label (dol, text  = "1 Доллар = ", font = 100,bg = "#C0C0C0")
            kdk2 = Label (dol, text = "Режим реального времени. \r Данные взяты с сайта \r https://quote.rbc.ru", bg = "#C0C0C0")     
            kdk1.place (x = 20, y = 15)
            kdk.place (x = 110, y = 15)
            kdk2.place (x = 20, y = 47 )

        def doll2 ():
            dol2 = Tk()
            dol2["bg"] = "#C0C0C0"
            dol2.title ("Доллар")
            dol2.resizable(width=False, height=False)
            dol2.geometry ("200x100")
            url312312 = "https://www.google.com/finance/quote/USD-RUB"
            sours11 = requests.get (url312312)
            main_text111 = sours11.text
            sopdsa = BeautifulSoup (main_text111, "html.parser")
            latesss = sopdsa.findAll ("div", {"class": "kf1m0"})
            tetxtsss = (latesss [0].text, "₽")
            kdk1 = Label (dol2, text  = tetxtsss, font = 100, bg = "#C0C0C0", foreground= "#800000")
            kdk11 = Label (dol2, text  = "1 Доллар = ", font = 100,bg = "#C0C0C0")
            kdk21 = Label (dol2, text = "Режим реального времени. \r Данные взяты с сайта \r https://www.google.com/finance", bg = "#C0C0C0")     
            kdk11.place (x = 20, y = 15)
            kdk1.place (x = 110, y = 15)
            kdk21.place (x = 10, y = 47 )


        def doll3 ():
            dol3 = Tk()
            dol3["bg"] = "#C0C0C0"
            dol3.title ("Доллар")
            dol3.resizable(width=False, height=False)
            dol3.geometry ("200x100")
            pjenkq = "https://invest.yandex.ru/catalog/quote/usd-cbr/"
            sdhrmnqw = requests.get (pjenkq)
            main_text1111 = sdhrmnqw.text
            sopdsa1 = BeautifulSoup (main_text1111, "html.parser")
            latesss1 = sopdsa1.findAll ("span", {"class": "bolbtRDz491tDq6jfmHd"})
            tetxtsss1 = (latesss1 [0].text, "₽")
            kdk11 = Label (dol3, text  = tetxtsss1, font = 100, bg = "#C0C0C0", foreground= "#800000")
            kdk111 = Label (dol3, text  = "1 Доллар = ", font = 100,bg = "#C0C0C0")
            kdk211 = Label (dol3, text = "Режим реального времени. \r Данные взяты с сайта \r https://invest.yandex.ru", bg = "#C0C0C0")     
            kdk111.place (x = 20, y = 15)
            kdk11.place (x = 110, y = 15)
            kdk211.place (x = 20, y = 47 )
       
        def euro ():
           euro = Tk()
           euro["bg"] = "#C0C0C0"
           euro.title ("Евро")
           euro.resizable(width=False, height=False)
           euro.geometry ("200x100")
           adr = "https://quote.rbc.ru/ticker/72383"
           soou = requests.get (adr)
           osnova = soou.text
           akd = BeautifulSoup (osnova, "html.parser")
           step = akd.findAll ("span", {"class": "chart__info__sum"})
           tttt = (step [0].text)
           euu = Label (euro, text = tttt)
           kd = Label (euro, text  = tttt, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kd1 = Label (euro, text  = "1 Евро = ", font = 100,bg = "#C0C0C0")
           kd2 = Label (euro, text = "Режим реального времени. \r Данные взяты с сайта \r https://quote.rbc.ru", bg = "#C0C0C0")     
           kd1.place (x = 30, y = 15)
           kd.place (x = 100, y = 15)
           kd2.place (x = 20, y = 47 )



        def euro1():
           euro123 = Tk()
           euro123["bg"] = "#C0C0C0"
           euro123.title ("Евро")
           euro123.resizable(width=False, height=False)
           euro123.geometry ("200x100")
           ppaspdekjqenasd = "https://www.google.com/finance/quote/EUR-RUB"
           poopokkk123 = requests.get (ppaspdekjqenasd)
           nichegonety = poopokkk123.text
           foienkjhasdf= BeautifulSoup (nichegonety, "html.parser")
           kidaysnus1283j = foienkjhasdf.findAll ("div", {"class": "YMlKec fxKbKc"})
           kakakakndjjf =  (kidaysnus1283j[0].text, "₽")
           kdkaka = Label (euro123, text  = kakakakndjjf, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kd1kaka = Label (euro123, text  = "1 Евро = ", font = 100,bg = "#C0C0C0")
           kd2ggg = Label (euro123, text = "Режим реального времени. \r Данные взяты с сайта \r https://www.google.com/finance", bg = "#C0C0C0")     
           kd1kaka.place (x = 30, y = 15)
           kdkaka.place (x = 100, y = 15)
           kd2ggg.place (x = 10, y = 47 )
        

        def euro2 ():
           euro1231 = Tk()
           euro1231["bg"] = "#C0C0C0"
           euro1231.title ("Евро")
           euro1231.resizable(width=False, height=False)
           euro1231.geometry ("200x100")
           ppaspdekjqenasd1 = "https://invest.yandex.ru/catalog/quote/eur-cbr/"
           poopokkk1231 = requests.get (ppaspdekjqenasd1)
           nichegonety1 = poopokkk1231.text
           foienkjhasdf1= BeautifulSoup (nichegonety1, "html.parser")
           kidaysnus1283j1 = foienkjhasdf1.findAll ("div", {"class": "_oUHzLvgHQ3gzS7grzt3"})
           kakakakndjjf1 =  (kidaysnus1283j1[0].text,)
           kdkaka1 = Label (euro1231, text  = kakakakndjjf1, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kd1kaka1 = Label (euro1231, text  = "1 Евро = ", font = 100,bg = "#C0C0C0")
           kd2ggg1 = Label (euro1231, text = "Режим реального времени. \r Данные взяты с сайта \r https://invest.yandex.ru", bg = "#C0C0C0")     
           kd1kaka1.place (x = 30, y = 15)
           kdkaka1.place (x = 100, y = 15)
           kd2ggg1.place (x = 10, y = 47 )
        





        def funt ():    
           funn = Tk()
           funn["bg"] = "#C0C0C0"
           funn.title ("Фунт")
           funn.resizable(width=False, height=False)
           funn.geometry ("200x100")
           lld = "https://quote.rbc.ru/ticker/77481"
           fkkk1 = requests.get (lld)
           mainn = fkkk1.text
           odo = BeautifulSoup (mainn, "html.parser")
           fdssa = odo.findAll ("span", {"class": "chart__info__sum"})
           pasdp = (fdssa [0].text)
           sda = Label (funn, text = pasdp)
           kaa = Label (funn, text  = pasdp, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kaa1 = Label (funn, text  = "1 Фунт = ", font = 100,bg = "#C0C0C0")
           kaa2 = Label (funn, text = "Режим реального времени. \r Данные взяты с сайта \r https://quote.rbc.ru", bg = "#C0C0C0")     
           kaa1.place (x = 30, y = 15)
           kaa.place (x = 100, y = 15)
           kaa2.place (x = 20, y = 47 )

        def funt1 ():
           funn1 = Tk()
           funn1["bg"] = "#C0C0C0"
           funn1.title ("Фунт")
           funn1.resizable(width=False, height=False)
           funn1.geometry ("200x100")
           ppaspdekjqenasd1231 = "https://www.google.com/finance/quote/GBP-RUB"
           poopokkk1231231 = requests.get (ppaspdekjqenasd1231)
           nichegonety2221 = poopokkk1231231.text
           foienkjhasdf3331= BeautifulSoup (nichegonety2221, "html.parser")
           kidaysnus1283j3331 = foienkjhasdf3331.findAll ("div", {"class": "YMlKec fxKbKc"})
           shestko_vkinulcya=  (kidaysnus1283j3331[0].text)
           sda1 = Label (funn1, text = shestko_vkinulcya)
           kaa1 = Label (funn1, text  = shestko_vkinulcya, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kaa11 = Label (funn1, text  = "1 Фунт = ", font = 100,bg = "#C0C0C0")
           kaa21 = Label (funn1, text = "Режим реального времени. \r Данные взяты с сайта \r https://www.google.com/finance", bg = "#C0C0C0")     
           kaa11.place (x = 30, y = 15)
           kaa1.place (x = 100, y = 15)
           kaa21.place (x = 10, y = 47 )

        def funt2 ():
           funn2 = Tk()
           funn2["bg"] = "#C0C0C0"
           funn2.title ("Фунт")
           funn2.resizable(width=False, height=False)
           funn2.geometry ("200x100")
           ppaspdekjqenasd12311 = "https://invest.yandex.ru/catalog/quote/gbp-cbr/"
           poopokkk12312311 = requests.get (ppaspdekjqenasd12311)
           nichegonety22211 = poopokkk12312311.text
           foienkjhasdf33311= BeautifulSoup (nichegonety22211, "html.parser")
           kidaysnus1283j33311 = foienkjhasdf33311.findAll ("div", {"class": "_oUHzLvgHQ3gzS7grzt3"})
           shestko_vkinulcya11 = (kidaysnus1283j33311[0].text)
           sda11 = Label (funn2, text = shestko_vkinulcya11)
           kaa11 = Label (funn2, text  = shestko_vkinulcya11, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kaa111 = Label (funn2, text  = "1 Фунт = ", font = 100,bg = "#C0C0C0")
           kaa211 = Label (funn2, text = "Режим реального времени. \r Данные взяты с сайта \r https://invest.yandex.ru", bg = "#C0C0C0")     
           kaa111.place (x = 30, y = 15)
           kaa11.place (x = 100, y = 15)
           kaa211.place (x = 20, y = 47 )


        def uanya ():
           kita = Tk()
           kita["bg"] = "#C0C0C0"
           kita.title ("Юань")
           kita.resizable(width=False, height=False)
           kita.geometry ("200x100")
           asd = "https://quote.rbc.ru/ticker/59066"
           kime = requests.get (asd)
           povoe = kime.text
           asda = BeautifulSoup (povoe, "html.parser")
           pkaje = asda.findAll ("span", {"class": "chart__info__sum"})
           knasd = (pkaje [0].text)
           asdss = Label (kita, text = knasd)
           kpp = Label (kita, text  = knasd, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kpp1 = Label (kita, text  = "1 Юань = ", font = 100,bg = "#C0C0C0")
           kpp2 = Label (kita, text = "Режим реального времени. \r Данные взяты с сайта \r https://quote.rbc.ru", bg = "#C0C0C0")     
           kpp1.place (x = 25, y = 15)
           kpp.place (x = 100, y = 15)
           kpp2.place (x = 20, y = 46 )

        def uanya1 ():
           kita1 = Tk()
           kita1["bg"] = "#C0C0C0"
           kita1.title ("Юань")
           kita1.resizable(width=False, height=False)
           kita1.geometry ("200x100")
           ppaspdekjqenasd1231112 = "https://www.google.com/finance/quote/CNY-RUB"
           poopokkk1231231112 = requests.get (ppaspdekjqenasd1231112)
           nichegonety2221112 = poopokkk1231231112.text
           foienkjhasdf3331112= BeautifulSoup (nichegonety2221112, "html.parser")
           kidaysnus1283j3331112 = foienkjhasdf3331112.findAll ("div", {"class": "YMlKec fxKbKc"})
           akkka =  (kidaysnus1283j3331112[0].text, "₽")
           asdss = Label (kita1, text = akkka)
           kpp1 = Label (kita1, text  = akkka, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kpp11 = Label (kita1, text  = "1 Юань = ", font = 100,bg = "#C0C0C0")
           kpp21 = Label (kita1, text = "Режим реального времени. \r Данные взяты с сайта \r https://www.google.com/finance", bg = "#C0C0C0")     
           kpp11.place (x = 25, y = 15)
           kpp1.place (x = 100, y = 15)
           kpp21.place (x = 10, y = 46 )

        def uanya2 ():
           kita11 = Tk()
           kita11["bg"] = "#C0C0C0"
           kita11.title ("Юань")
           kita11.resizable(width=False, height=False)
           kita11.geometry ("200x100")
           ppaspdekjqenasd1231112123 = "https://invest.yandex.ru/catalog/quote/cny-cbr/"
           poopokkk1231231112123 = requests.get (ppaspdekjqenasd1231112123)
           nichegonety2221112123 = poopokkk1231231112123.text
           foienkjhasdf3331112123= BeautifulSoup (nichegonety2221112123, "html.parser")
           kidaysnus1283j3331112123 = foienkjhasdf3331112123.findAll ("div", {"class": "_oUHzLvgHQ3gzS7grzt3"})
           pppla =  (kidaysnus1283j3331112123[0].text)
           asdss12 = Label (kita11, text = pppla)
           kpp112 = Label (kita11, text  = pppla, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kpp1112 = Label (kita11, text  = "1 Юань = ", font = 100,bg = "#C0C0C0")
           kpp2112 = Label (kita11, text = "Режим реального времени. \r Данные взяты с сайта \r https://invest.yandex.ru", bg = "#C0C0C0")     
           kpp1112.place (x = 25, y = 15)
           kpp112.place (x = 100, y = 15)
           kpp2112.place (x = 20, y = 46 )



        def shw ():
           plasd = Tk()
           plasd["bg"] = "#C0C0C0"
           plasd.title ("Франк")
           plasd.resizable(width=False, height=False)
           plasd.geometry ("200x100")
           aaa786 = "https://quote.rbc.ru/ticker/130131"
           kime = requests.get (aaa786)
           povoe12 = kime.text
           asda = BeautifulSoup (povoe12, "html.parser")
           pkaje3 = asda.findAll ("span", {"class": "chart__info__sum"})
           knasd4 = (pkaje3 [0].text)
           asdss5 = Label (plasd, text = knasd4)
           kpq = Label (plasd, text  = knasd4, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kpq1 = Label (plasd, text  = "1 Франк = ", font = 100,bg = "#C0C0C0")
           kpq2 = Label (plasd, text = "Режим реального времени. \r Данные взяты с сайта \r https://quote.rbc.ru", bg = "#C0C0C0")     
           kpq1.place (x = 25, y = 15)
           kpq.place (x = 103, y = 15)
           kpq2.place (x = 20, y = 46 )


        def shw1 ():
           plase1 = Tk()
           plase1["bg"] = "#C0C0C0"
           plase1.title ("Франк")
           plase1.resizable(width=False, height=False)
           plase1.geometry ("200x100")
           den123 = "https://www.google.com/finance/quote/CHF-RUB"
           p123 = requests.get (den123)
           n123 = p123.text
           f123= BeautifulSoup (n123, "html.parser")
           k123 = f123.findAll ("div", {"class": "YMlKec fxKbKc"})
           bkbIMBA =  (k123[0].text)
           asdss51 = Label (plase1, text = bkbIMBA)
           kpq1 = Label (plase1, text  = bkbIMBA, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kpq11 = Label (plase1, text  = "1 Франк = ", font = 100,bg = "#C0C0C0")
           kpq21 = Label (plase1, text = "Режим реального времени. \r Данные взяты с сайта \r https://www.google.com/finance", bg = "#C0C0C0")     
           kpq11.place (x = 25, y = 15)
           kpq1.place (x = 103, y = 15)
           kpq21.place (x = 10, y = 46 )

        def shw2 ():
           plllan = Tk()
           plllan["bg"] = "#C0C0C0"
           plllan.title ("Франк")
           plllan.resizable(width=False, height=False)
           plllan.geometry ("200x100")
           den1231 = "https://invest.yandex.ru/catalog/quote/chf-cbr/"
           p1231 = requests.get (den1231)
           n1231 = p1231.text
           f1231= BeautifulSoup (n1231, "html.parser")
           k1231 = f1231.findAll ("div", {"class": "_oUHzLvgHQ3gzS7grzt3"})
           hhhg =  (k1231[0].text)
           asdss511 = Label (plllan, text = hhhg)
           kpq11 = Label (plllan, text  = hhhg, font = 100, bg = "#C0C0C0", foreground= "#800000")
           kpq111 = Label (plllan, text  = "1 Франк = ", font = 100,bg = "#C0C0C0")
           kpq211 = Label (plllan, text = "Режим реального времени. \r Данные взяты с сайта \r https://invest.yandex.ru", bg = "#C0C0C0")     
           kpq111.place (x = 25, y = 15)
           kpq11.place (x = 103, y = 15)
           kpq211.place (x = 20, y = 46 )


        def pogg ():
            newokno = Toplevel()
            newokno.title ("Погода")
            newokno ["bg"]= "#DCDCDC"
            newokno.resizable (width=False, height=False)
            newokno.geometry ("200x100")
            adress = "https://world-weather.ru/pogoda/russia/krasnoyarsk/"
            soop = requests.get (adress)
            osnovnoy = soop.text
            apaq = BeautifulSoup (osnovnoy, "html.parser")
            kiday = apaq.findAll ("div", {"id": "weather-now-number"})
            pogoda = (kiday[0].text)
            textpog = Label (newokno, text = pogoda, font = 100, bg = "#DCDCDC")
            seychas = Label (newokno, text = "Погода в Красноярске \r на данный момент: ", justify=CENTER, bg = "#DCDCDC")
            dan = Label(newokno, text = "https://world-weather.ru",bg = "#DCDCDC")
            dan.place (x = 7, y = 79)
            textpog.place (x=80, y = 35)
            seychas.place (x = 35, y = 5)
            
            def timee():
                current_tie = time.strftime("%H : %M")
                clock1.config(text=current_tie)
                clock1.after(200,timee)
            clock1=Label(newokno,font=("times",10,"bold"),bg="#DCDCDC")
            clock1.place (x = 150, y = 80)
            timee()


        def okaoskd ():
            today = date.today()

            def get_age():
                d= int(e111.get())
                m=int(e222.get())
                y=int(e333.get())
                age =today.year-y-((today.month, today.day)<(m,d))
                t1.config(state='normal')
                t1.delete('1.0', tk.END)
                t1.insert(tk.END,age)
                t1.config(state='disabled')

                
            window = tk.Tk()
            window.geometry("400x230")
            window.config(bg="#C0C0C0")
            window.resizable(width=False,height=False)
            window.title('Калькулятор возраста')

            nadp = tk.Label(window,text="Калькулятор возраста!",font=("Arial", 20),fg="black",bg="#C0C0C0")
            qweqweqwq = tk.Label(window,font=("Arial",12),text="Введи дату рождения и узнай свой возраст",fg="black",bg="#C0C0C0")

            qweqwe=tk.Label(window,text="День: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#C0C0C0")
            qweqweqweqwe=tk.Label(window,text="Месяц: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#C0C0C0")
            pppqpp=tk.Label(window,text="Год: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#C0C0C0")
            e111=tk.Entry(window,width=5)
            e222=tk.Entry(window,width=5)
            e333=tk.Entry(window,width=5)

            b1=tk.Button(window,text="Посчитать!",font=("Arial",13, "bold"),fg = "#000000",command=get_age)

            l3 = tk.Label(window,text="Твой возраст: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#C0C0C0")
            t1=tk.Text(window,width=5,height=0,state="disabled")
            nadp.place(x=70,y=5)
            qweqweqwq.place(x=50,y=40)
            qweqwe.place(x=130,y=70)
            qweqweqweqwe.place(x=130,y=95)
            pppqpp.place(x=130,y=120)
            e111.place(x=210,y=70)
            e222.place(x=210,y=95)
            e333.place(x=210,y=120)
            b1.place(x=135,y=150)
            l3.place(x=85,y=188)
            t1.place(x=225,y=190)
            window.mainloop()


        def dlinna ():
            jnasdj = Tk()
            jnasdj.geometry ("200x170")
            jnasdj.title ("Длина")
            jnasdj ["bg"]= "#DCDCDC"
            jnasdj.resizable (width=False, height=False)
            dlin_text = Label (jnasdj, text = "Меры длины", bg = "#DCDCDC", font = ("times",15))
            dlin_text.place (x = 0, y = 6)
            dlin_text1 = Label (jnasdj, text = "1 км = 1 000 м", bg = "#DCDCDC", font = ("times", 13))
            dlin_text1.place (x = 0, y = 30)
            dlin_text2 = Label (jnasdj, text = "1 дм = 10 см = 100 мм", bg = "#DCDCDC",font = ("times", 13))
            dlin_text2.place (x = 0, y = 50)
            dlin_text3 = Label (jnasdj, text = "1 м = 10 дм = 100 см", bg = "#DCDCDC",font = ("times", 13))
            dlin_text3.place (x = 0, y = 70)
            dlin_text4 = Label (jnasdj, text = "1 см = 10 мм", bg = "#DCDCDC",font = ("times", 13))
            dlin_text4.place (x = 0, y = 90)
            dlin_text5 = Label (jnasdj, text = "1 мм = 1 000 мк", bg = "#DCDCDC",font = ("times", 13))
            dlin_text5.place (x = 0, y = 110)
        


        def plochs ():
            placeashm1 = Tk()
            placeashm1.geometry ("250x170")
            placeashm1.title ("Площадь")
            placeashm1 ["bg"]= "#DCDCDC"
            placeashm1.resizable (width=False, height=False)
            ploshad_text = Label (placeashm1, text = "Меры площади", bg = "#DCDCDC", font = ("times",15))
            ploshad_text.place (x = 0, y = 6)
            ploshad_text1 = Label (placeashm1, text = "1 га = 100 а = 10 000 м2", bg = "#DCDCDC", font = ("times", 13))
            ploshad_text1.place (x = 0, y = 30)
            ploshad_text2 = Label (placeashm1, text = "1 а = 100 м2 = 10 000 дм2", bg = "#DCDCDC",font = ("times", 13))
            ploshad_text2.place (x = 0, y = 50)
            ploshad_text3 = Label (placeashm1, text = "1 м2 = 100 дм2= 10 000 см2", bg = "#DCDCDC",font = ("times", 13))
            ploshad_text3.place (x = 0, y = 70)
            ploshad_text4 = Label (placeashm1, text = "1 дм2 = 100 см2= 10 000 мм2", bg = "#DCDCDC",font = ("times", 13))
            ploshad_text4.place (x = 0, y = 90)
            ploshad_text5 = Label (placeashm1, text = "1 см2 = 100 мм2", bg = "#DCDCDC",font = ("times", 13))
            ploshad_text5.place (x = 0, y = 110)


        def obbbem ():
            obbbbbbbem = Tk()
            obbbbbbbem.geometry ("200x170")
            obbbbbbbem.title ("Объем")
            obbbbbbbem ["bg"]= "#DCDCDC"
            obbbbbbbem.resizable (width=False, height=False)
            mera_ibem_text = Label (obbbbbbbem, text = "Меры объема", bg = "#DCDCDC", font = ("times",15))
            mera_ibem_text.place (x = 0, y = 6)
            mera_ibem_text1 = Label (obbbbbbbem, text = "1 м3 = 1 000 дм3", bg = "#DCDCDC", font = ("times", 13))
            mera_ibem_text1.place (x = 0, y = 30)
            mera_ibem_text2 = Label (obbbbbbbem, text = "1 дм3= 1 000 см3", bg = "#DCDCDC",font = ("times", 13))
            mera_ibem_text2.place (x = 0, y = 50)
            mera_ibem_text3 = Label (obbbbbbbem, text = "1 л = 1 дм3", bg = "#DCDCDC",font = ("times", 13))
            mera_ibem_text3.place (x = 0, y = 70)
            mera_ibem_text4 = Label (obbbbbbbem, text = "1 см3 = 1 000 мм3", bg = "#DCDCDC",font = ("times", 13))
            mera_ibem_text4.place (x = 0, y = 90)
            mera_ibem_text5 = Label (obbbbbbbem, text = "1 мм3 = 0,001 см3", bg = "#DCDCDC",font = ("times", 13))
            mera_ibem_text5.place (x = 0, y = 110)

       


        def vessa ():
            vessasssa = Tk()
            vessasssa.geometry ("200x170")
            vessasssa.title ("Вес")
            vessasssa ["bg"]= "#DCDCDC"
            vessasssa.resizable (width=False, height=False)
            ves_ibem_text = Label (vessasssa, text = "Меры веса", bg = "#DCDCDC", font = ("times",15))
            ves_ibem_text.place (x = 0, y = 6)
            ves_ibem_text1 = Label (vessasssa, text = "1 т = 10 ц = 1 000 кг", bg = "#DCDCDC", font = ("times", 13))
            ves_ibem_text1.place (x = 0, y = 30)
            ves_ibem_text2 = Label (vessasssa, text = "1 ц = 100 кг", bg = "#DCDCDC",font = ("times", 13))
            ves_ibem_text2.place (x = 0, y = 50)
            ves_ibem_text3 = Label (vessasssa, text = "1 кг = 1 000 г", bg = "#DCDCDC",font = ("times", 13))
            ves_ibem_text3.place (x = 0, y = 70)
            ves_ibem_text4 = Label (vessasssa, text = "1 г = 1 000 мг", bg = "#DCDCDC",font = ("times", 13))
            ves_ibem_text4.place (x = 0, y = 90)
            ves_ibem_text5 = Label (vessasssa, text = "1 мг = 0,001 г", bg = "#DCDCDC",font = ("times", 13))
            ves_ibem_text5.place (x = 0, y = 110)       




        def vrre ():
            vasesje = Tk()
            vasesje.geometry ("250x200")
            vasesje.title ("Время")
            vasesje ["bg"]= "#DCDCDC"
            vasesje.resizable (width=False, height=False)
            mera_vesa_text = Label (vasesje, text = "Меры времени", bg = "#DCDCDC", font = ("times",15))
            mera_vesa_text.place (x = 0, y = 6)
            mera_vesa_text1 = Label (vasesje, text = "1 век = 100 лет", bg = "#DCDCDC", font = ("times", 13))
            mera_vesa_text1.place (x = 0, y = 30)
            mera_vesa_text2 = Label (vasesje, text = "1 год = 12 мес = 365 или 366 сут", bg = "#DCDCDC",font = ("times", 13))
            mera_vesa_text2.place (x = 0, y = 50)
            mera_vesa_text3 = Label (vasesje, text = "1 мес = 30/31/28/29 сут. ", bg = "#DCDCDC",font = ("times", 13))
            mera_vesa_text3.place (x = 0, y = 70)
            mera_vesa_text4 = Label (vasesje, text = "1 неделя = 7 сут", bg = "#DCDCDC",font = ("times", 13))
            mera_vesa_text4.place (x = 0, y = 90)
            mera_vesa_text5 = Label (vasesje, text = "1 сут = 24 ч= 86 400 сек", bg = "#DCDCDC",font = ("times", 13))
            mera_vesa_text5.place (x = 0, y = 110)    
            mera_vesa_text6 = Label (vasesje, text = "1 ч = 60 мин = 3 600 сек", bg = "#DCDCDC",font = ("times", 13))
            mera_vesa_text6.place (x = 0, y = 130) 
            mera_vesa_text7 = Label (vasesje, text = "1 мин = 60 с", bg = "#DCDCDC",font = ("times", 13))
            mera_vesa_text7.place (x = 0, y = 150) 
            mera_vesa_text8 = Label (vasesje, text = "1 сек = 1 000 мсек", bg = "#DCDCDC",font = ("times", 13))
            mera_vesa_text8.place (x = 0, y = 170)   
        

        def password ():
            andreyka = Tk ()
            andreyka.geometry ("250x200")
            andreyka.title ("Пароль")
            andreyka ["bg"]= "#DCDCDC"
            andreyka.resizable (width=False, height=False)
            

            def ooa ():
                s1123 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                s2123 = "0123456789"
                s3123 = "~!@#$%^&*()_+{}[\]:/"
                s123 = s1123.upper() + s1123.lower() + s2123 + s3123
                pass1 = ""
                for i in range(15):
                    p = random.choice(s123)
                    pass1 = pass1 + p
                
                t11=tk.Text(andreyka,width=18,height=0,state="disabled", font= ("times", 15))
                t11.place (x = 32, y = 130)
                t11.config(state='normal')
                t11.delete('1.0', tk.END)
                t11.insert(tk.END,pass1)
                t11.config(state='disabled')
            kdas = Label (andreyka, text = "Поможет сгенерировать надежный \r и безопасный пароль.", font = ("times", 10), bg = "#DCDCDC")
            kdas.place (x = 23, y = 3)
            easd = Button (andreyka, text = "Генерировать",font = ("times", 15),foreground="#990000", command = ooa)
            easd.place (x = 55, y = 60)
            


       
            

        #СТРОКА1
        menu = Menu(root)  
        new = Menu(menu, tearoff = False) 
        new1 = Menu (menu, tearoff=False)
        new2 = Menu (menu, tearoff=False)
        new3 = Menu (menu, tearoff=False)
        new4 = Menu (menu, tearoff=False)
        new5 = Menu (menu, tearoff=False)
        fileMenu = Menu(new2, tearoff=False)
        fileMenu1 = Menu (new2, tearoff=False)
        fileMenu2 = Menu (new3, tearoff=False)
        fileMenu3 = Menu (new4, tearoff=False)
        fileMenu4 = Menu (new5, tearoff=False)
        txtkode = "Открытый код"     
        kod = new.add_command (label = txtkode, command = click)
        kakkk = new.add_command (label = "Калькулятор возраста", command = okaoskd)
        pog = new.add_command (label = "Погода сейчас", command = pogg)
        afsase = new.add_command (label = "Генератор паролей", command = password)
        pril = new.add_command(label='О приложении', command = pll)
        ex = new.add_command (label = "Exit",foreground="#A60000", command = exx)
        
        
        
        menu.add_cascade(label='Info', menu=new) 
        menu.add_cascade (label= "Курс", menu = new1)  
        menu.add_cascade (label = "Ед. измерения", menu = new2)
        dlinn = new2.add_command (label = "Меры длины",foreground = "#8106A9", command = dlinna)
        plow = new2.add_command (label = "Меры площади",foreground = "#8106A9", command = plochs)
        obem = new2.add_command (label = "Меры объема",foreground = "#8106A9", command = obbbem)
        ves = new2.add_command (label = "Меры веса",foreground = "#8106A9", command = vessa)
        vremya = new2.add_command (label = "Меры времени",foreground = "#8106A9", command = vrre)
        new1.add_cascade(label= "Доллар", menu=fileMenu)
        new1.add_cascade (label = "Евро", menu = fileMenu1)
        new1.add_cascade(label = "Фунт стерлингов", menu = fileMenu2)
        new1.add_cascade (label = "Китайский Юань", menu = fileMenu3)
        new1.add_cascade(label = "Швейцарский Франк", menu = fileMenu4)
        fileMenu.add_command (label = "Источник информации:", foreground= "#A61A00")
        fileMenu1,fileMenu2,fileMenu3,fileMenu4.add_command (label = "Источник информации:", foreground= "#A61A00")
        fileMenu1.add_command (label = "https://quote.rbc.ru",command = euro)
        fileMenu1.add_command (label = "https://www.google.com/finance", command = euro1)
        fileMenu1.add_command(label = "https://invest.yandex.ru", command = euro2)
        fileMenu.add_command(label="https://quote.rbc.ru", command = doll)
        fileMenu.add_command(label = "https://www.google.com/finance", command=doll2)
        fileMenu.add_command (label = "https://invest.yandex.ru", command = doll3)
        fileMenu2.add_command(label = "https://quote.rbc.ru", command = funt)
        fileMenu2.add_command (label = "https://www.google.com/finance", command = funt1)
        fileMenu2.add_command (label = "https://invest.yandex.ru", command = funt2)
        fileMenu3.add_command (label = "https://quote.rbc.ru", command = uanya)
        fileMenu3.add_command (label = "https://www.google.com/finance", command=uanya1)
        fileMenu3.add_command(label = "https://invest.yandex.ru", command = uanya2)
        fileMenu4.add_command (label = "https://quote.rbc.ru", command = shw)
        fileMenu4.add_command (label = "https://www.google.com/finance", command = shw1)
        fileMenu4.add_command (label = "https://invest.yandex.ru", command = shw2)
        root.config(menu=menu)  


        
        


        
  #ОЦЕНКА
        def ocenkacom (): 
            def okk ():
                def vvv ():
                    library.destroy()
                    messagebox.showinfo('Отзыв', 'Спасибо за вашу оценку, вы помогаете стать нам лучше\r (◕‿◕)')  

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
            

        
      #ВРЕМЯ  
        def timing():
            current_time = time.strftime("%H : %M : %S")
            clock.config(text=current_time)
            clock.after(200,timing)
        clock=Label(root,font=("times",15,"bold"),bg="#D3D3D3")
        clock.place (x = 10, y = 542)
        timing()
#ЦИФРЫ
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
            self.formula = self.formula = "0"
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
