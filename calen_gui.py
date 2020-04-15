from calendar import *
from tkinter import *
from datetime import datetime
import time

setfirstweekday(firstweekday=6)


class canlenframe:
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.frame1 = Frame(self.master, height=360, width=320)
        self.frame1.pack(fill=BOTH, expand=1)
        self.label1 = Label(self.frame1, text=time.strftime('%Y年%m月%d日', time.localtime(time.time())), anchor='n',
                            font=('正文', 15))
        self.label1.place(x=10, y=10, width=300, height=30)
        self.text = Text(self.frame1, font=('正文', 20))
        self.text.place(x=10, y=50, width=300, height=250)
        self.text.insert(INSERT, month(datetime.now().year, datetime.now().month))

        
