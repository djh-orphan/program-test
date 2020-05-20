from tkinter import *
import time
import calen_gui
import tkinter.messagebox
from prettytable import PrettyTable
import pymysql

con = pymysql.connect(host='127.0.0.1', user='root', passwd='djh660993', db='data', charset='utf8')
c = con.cursor()
sql = "insert into event(eventCT,eventtime,eventcost) value(%s,%s,%s)"
sql2 = "select eventCT,eventtime,eventcost from event where eventtime>=%s and eventtime<=%s"


class ClocFrame:
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.frame2 = Frame(self.master, height=420, width=420)
        self.frame2.pack(fill=BOTH, expand=1)
        self.label1 = Label(self.frame2, text="任务名称:")
        self.label1.place(x=10, y=10, height=20, width=60)
        self.work = Entry(self.frame2)
        self.work.place(x=80, y=10, height=20, width=270)
        self.entryWidget = Entry(self.frame2)
        self.entryWidget.place(x=4, y=50, height=20, width=50)
        self.a = Label(self.frame2, text="时")
        self.a.place(x=60, y=50, height=20, width=20)
        self.entryW = Entry(self.frame2)
        self.entryW.place(x=90, y=50, height=20, width=50)
        self.b = Label(self.frame2, text="分")
        self.b.place(x=150, y=50, height=20, width=20)
        self.entry = Entry(self.frame2)
        self.entry.place(x=180, y=50, height=20, width=50)
        self.c = Label(self.frame2, text="秒")
        self.c.place(x=240, y=50, height=20, width=20)
        self.hi_there = Button(self.frame2, text="开始", command=self.start)
        self.hi_there.place(x=270, y=50, height=20, width=40)
        self.button = Button(self.frame2, text="退出", fg="red", command=self.frame2.quit)
        self.button.place(x=370, y=50, height=20, width=40)
        self.button2 = Button(self.frame2, text="切换", fg="#000000", command=self.change)
        self.button2.place(x=320, y=50, width=40, height=20)
        self.entry2 = Entry(self.frame2)
        self.entry2.place(x=10, y=90, height=20, width=130)
        self.entry3 = Entry(self.frame2)
        self.entry3.place(x=180, y=90, height=20, width=130)
        self.label3 = Label(self.frame2, text="至").place(x=150, y=90, height=20, width=20)
        self.button3 = Button(self.frame2, text="查询", command=self.check).place(x=320, y=90, height=20, width=40)
        self.lbl1 = Label(self.frame2)
        self.text = Text(self.frame2)

    def start(self):
        self.lbl1 = Label(self.frame2)
        self.text.destroy()
        self.lbl1.place(x=10, y=130, height=200, width=400)
        self.lbl1.config(fg='#000000', font=('宋体', 20))
        text = self.entryWidget.get().strip()
        text2 = self.entryW.get().strip()
        text3 = self.entry.get().strip()
        self.text4 = str(self.work.get().strip())

        if text != "" and text2 != "":
            num = int(text)
            num2 = int(text2)
            num3 = int(text3)
            self.countDown(num, num2, num3, self.text4)
            c.execute(sql,
                      (self.text4, time.strftime('%Y%m%d%H%M%S', time.localtime()), text + ':' + text2 + ':' + text3))
            con.commit()

    def countDown(self, m, n, z, s):
        self.lbl1.config(bg='yellow')
        seconds = m * 3600 + n * 60 + z
        for k in range(seconds, 0, -1):
            a = k // 3600
            b = (k % 3600) // 60
            c = k % 3600 % 60
            self.lbl1["text"] = (a, "小时", b, "分钟", c, "秒")
            self.lbl1.update()
            time.sleep(1)
        tkinter.messagebox.showinfo('提示', '时间到')
        self.lbl1.config(bg='red')
        self.lbl1.config(fg='white')
        self.lbl1["text"] = "时间到！"

    def change(self):
        self.frame2.destroy()
        calen_gui.CanlenFrame(self.master)

    def check(self):
        self.lbl1.destroy()
        self.text = Text(self.frame2)
        self.text.place(x=10, y=130, height=200, width=400)
        self.text.delete('0.0', 'end')
        d = self.entry2.get()
        e = self.entry3.get()
        c.execute(sql2, (d, e))
        a = c.fetchall()
        header = '事件内容 事件发生时间 事件耗费时间'.split()
        pt = PrettyTable()
        pt._set_field_names(header)
        for b in a:
            pt.add_row(b)
        self.text.insert(INSERT, pt)
