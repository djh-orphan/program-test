from tkinter import *
import time
from calen_gui import *
import tkinter.messagebox

# workbook = xlsxwriter.Workbook('hello.xlsx') # 建立文件
#
# worksheet = workbook.add_worksheet() # 建立sheet， 可以work.add_worksheet('employee')来指定sheet名，但中文名会报UnicodeDecodeErro的错误




class ClocFrame:
    def __init__(self, master):
        self.master=master
        self.master.config()
        self.frame2 = Frame(self.master,)
        self.frame2.pack()
        self.label1 = Label(self.frame2, text="任务名称")
        self.label1.pack(side=TOP)
        self.lbl1 = Label(self.frame2)
        self.lbl1.pack(fill=BOTH, expand=1)
        self.work = Entry(self.frame2)
        self.work["width"] = 10
        self.work.pack(side=TOP)


        self.entryWidget = Entry(self.frame2)
        self.entryWidget["width"] = 10
        self.entryWidget.pack(side=LEFT)
        self.a=Label(self.frame2,text="小时")
        self.a.pack(side=LEFT)
        self.entryW = Entry(self.frame2)
        self.entryW["width"] = 10
        self.entryW.pack(side=LEFT)
        self.b = Label(self.frame2, text="分钟")
        self.b.pack(side=LEFT)
        self.entry = Entry(self.frame2)
        self.entry["width"] = 10
        self.entry.pack(side=LEFT)
        self.c = Label(self.frame2, text="秒")
        self.c.pack(side=LEFT)
        self.hi_there = Button(self.frame2, text="开始", command=self.start)
        self.hi_there.pack(side=LEFT)
        self.button = Button(self.frame2, text="退出", fg="red", command=self.frame2.quit)
        self.button.pack(side=LEFT)

        self.button2 = Button(self.frame2, text="切换", fg="red", command=self.change)
        self.button2.place(x=135, y=400, width=30, height=30)
    def start(self):
        text = self.entryWidget.get().strip()
        text2 = self.entryW.get().strip()
        text3 = self.entry.get().strip()
        text4=self.work.get().strip()
        if text != ""and text2 != "":
            num = int(text)
            num2 = int(text2)
            num3=int(text3)
            self.countDown(num,num2,num3,text4)

    def countDown(self, m,n,z,s):
        self.lbl1.config(bg='yellow')
        self.lbl1.config(height=5, font=('times', 20, 'bold'))
        seconds=m*3600+n*60+z
        for k in range(seconds, 0, -1):
            a=k//3600
            b=(k%3600)//60
            c=k%3600%60
            self.lbl1["text"] = (a,"小时",b,"分钟",c,"秒")
            self.lbl1.update()
            time.sleep(1)
        tkinter.messagebox.showinfo('提示', '时间到')
        self.lbl1.config(bg='red')
        self.lbl1.config(fg='white')
        self.lbl1["text"] = "时间到！"
    def change(self):
        self.frame2.destroy()
        CanlenFrame(self.master)







