from calendar import *
from tkinter import *
from datetime import datetime
import cloc_gui
import time
import weather
setfirstweekday(firstweekday=6)
url_root = "https://www.tianqi.com/"

class CanlenFrame:
    showyear = datetime.now().year
    showmonth = datetime.now().month

    def __init__(self, master):
        self.master = master
        self.master.config()
        self.frame1 = Frame(self.master, height=450, width=320)
        self.frame1.pack(fill=BOTH, expand=1)
        self.label1 = Label(self.frame1, text=time.strftime('%Y年%m月%d日', time.localtime(time.time())), anchor='nw',
                            font=('正文', 15))
        self.label1.place(x=10, y=10, width=300, height=30)
        self.text = Text(self.frame1, font=('正文', 20))
        self.text.place(x=10, y=100, width=300, height=250)
        self.text.insert(INSERT, month(self.showyear, self.showmonth))
        self.button1 = Button(self.frame1, text='>', command=self.plus)
        self.button1.place(x=280, y=350, width=30, height=30)
        self.button2 = Button(self.frame1, text='<', command=self.sub)
        self.button2.place(x=10, y=350, width=30, height=30)
        self.button3 = Button(self.frame1, text='back', command=self.back)
        self.button3.place(x=135, y=350, width=30, height=30)
        self.entry1 = Entry(self.frame1, justify='right')
        self.entry1.place(x=20, y=50, width=100, height=30)
        self.label2 = Label(self.frame1, text='年', justify='left')
        self.label2.place(x=125, y=50, width=15, height=30)
        self.entry2 = Entry(self.frame1, justify='right')
        self.entry2.place(x=140, y=50, width=100, height=30)
        self.label3 = Label(self.frame1, text='月', justify='left')
        self.label3.place(x=245, y=50, width=15, height=30)
        self.button4 = Button(self.frame1, text='查询', command=self.check)
        self.button4.place(x=275, y=50, width=30, height=30)
        self.button5 = Button(self.frame1, text='日程管理', command=self.change)
        self.button5.place(x=95, y=400, width=60, height=30)
        self.button6 = Button(self.frame1, text='天气', command=self.change2)
        self.button6.place(x=175, y=400, width=40, height=30)
    def plus(self):
        self.text.delete('0.0', 'end')
        if self.showmonth < 12:
            self.showmonth = self.showmonth + 1
        else:
            self.showyear = self.showyear + 1
            self.showmonth = 1
        self.text.insert(INSERT, month(self.showyear, self.showmonth))
        print('+1', self.showmonth)

    def sub(self):
        self.text.delete('0.0', 'end')
        if self.showmonth > 1:
            self.showmonth = self.showmonth - 1
        else:
            self.showyear = self.showyear - 1
            self.showmonth = 12
        self.text.insert(INSERT, month(self.showyear, self.showmonth))
        print('-1', self.showmonth)

    def back(self):
        self.showyear = datetime.now().year
        self.showmonth = datetime.now().month
        self.text.delete('0.0', 'end')
        self.text.insert(INSERT, month(self.showyear, self.showmonth))

    def check(self):
        self.showyear = int(self.entry1.get())
        self.showmonth = int(self.entry2.get())
        self.text.delete('0.0', 'end')
        self.text.insert(INSERT, month(self.showyear, self.showmonth))

    def change(self):
        self.frame1.destroy()
        cloc_gui.ClocFrame(self.master)
    def change2(self):
        self.frame1.destroy()
        weather.Weather(url_root,self.master)
