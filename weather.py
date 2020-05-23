import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from cloc_gui import *
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3038.30 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
class Weather():
    def __init__(self, url_root, root):
        r_root = requests.get(url_root, headers=headers, timeout=500)
        r_root.encoding = "UTF-8"
        demo1 = r_root.text
        self.demo = demo1
        self.root = root
        self.frame = Frame(self.root, height=440, width=680)
        self.frame.pack(fill=BOTH, expand=1)
        self.tex1 = Text(self.frame)
        self.tex2 = Text(self.frame)
        self.tex3 = Text(self.frame)
        self.tex4 = Text(self.frame)
        self.tex5 = Text(self.frame)
        self.tex6 = Text(self.frame)
        self.tex7 = Text(self.frame)
        self.tex8 = Text(self.frame)
        self.tex9 = Text(self.frame)
        self.tex10 = Text(self.frame)
        self.tex11 = Text(self.frame)
        self.tex12 = Text(self.frame)
        self.tex13 = Text(self.frame)
        self.tex14 = Text(self.frame)
        self.tex15 = Text(self.frame)
        self.tex1.place(x=20, y=90, height=40, width=200)
        self.tex2.place(x=240, y=90, height=40, width=200)
        self.tex3.place(x=460, y=90, height=40, width=200)
        self.tex4.place(x=20, y=150, height=40, width=200)
        self.tex5.place(x=240, y=150, height=40, width=200)
        self.tex6.place(x=460, y=150, height=40, width=200)
        self.tex7.place(x=20, y=210, height=40, width=200)
        self.tex8.place(x=240, y=210, height=40, width=200)
        self.tex9.place(x=460, y=210, height=40, width=200)
        self.tex10.place(x=20, y=270, height=40, width=200)
        self.tex11.place(x=240, y=270, height=40, width=200)
        self.tex12.place(x=460, y=270, height=40, width=200)
        self.tex13.place(x=20, y=330, height=40, width=200)
        self.tex14.place(x=240, y=330, height=40, width=200)
        self.tex15.place(x=460, y=330, height=40, width=200)
        self.lab=Label(self.frame,text="请输入想要查询的国家：",anchor='nw',font=('Arial', 12))
        self.lab.place(x=20,y=10,height=20,width=200)
        self.button=Button(self.frame,text="日程管理",command=self.change)
        self.button.place(x=420,y=10,height=20,width=60)
        self.b = Button(self.frame, text='确定', command=self.show_weather)
        self.b.place(x=360, y=10,height=20, width=40)
        self.e = Entry(self.frame, show=None,font=('Arial', 14))
        self.e.place(x=240, y=10,height=20, width=100)
        self.l2 = Label(self.frame, text='该国家主要地区的天气情况', font=('Arial', 12),anchor='center')
        self.l2.place(x=230, y=50,height=20,width=220)
        self.bt2=Button(self.frame,text="日历",command=self.change2)
        self.bt2.place(x=500, y=10, height=20, width=40)
        self.a = self.get_all_html()
        self.s = []
        for num in range(len(self.a)):
            self.s.append(self.parse_single_html(self.a[num]))
    def get_all_html(self,):
        soup = BeautifulSoup(self.demo, 'html.parser')
        articles = soup.find("div", class_="inter_weather main")
        SSS = articles.find("div", class_="inter_continent")
        SSSS = SSS.find("div", class_="continent_list chooseBox clearfix")
        SSSSS = SSSS.find_all("li")
        HREF = []
        for i in range(len(SSSSS)):
            HREF.append("https://www.tianqi.com" + SSSSS[i].find("a")["href"])
        return HREF

    def parse_single_html(self,html):
        r = requests.get(html, headers=headers, timeout=500)
        soup = BeautifulSoup(r.text, 'html.parser')
        articles = soup.find("div", class_="inter_cityweather mgb_ul clearfix")
        place = articles.find_all("li")
        place_info = soup.find("div", class_="tit")
        weather = [place_info.text[1:14]]
        for i in range(len(place) - 1):
            weather.append(place[i].find("a")["title"])
        return weather

    def show_weather(self):
        '''l3 = tk.Label(frame, text=place_name.get()).place(x=100, y=400)'''
        for i in range(len(self.s)):
            if self.e.get()[0:len(self.e.get())] == self.s[i][0][0:len(self.e.get())]:
                self.tex1.delete(1.0, END)
                self.tex2.delete(1.0, END)
                self.tex3.delete(1.0, END)
                self.tex4.delete(1.0, END)
                self.tex5.delete(1.0, END)
                self.tex6.delete(1.0, END)
                self.tex7.delete(1.0, END)
                self.tex8.delete(1.0, END)
                self.tex9.delete(1.0, END)
                self.tex10.delete(1.0, END)
                self.tex11.delete(1.0, END)
                self.tex12.delete(1.0, END)
                self.tex13.delete(1.0, END)
                self.tex14.delete(1.0, END)
                self.tex15.delete(1.0, END)
                self.tex1.insert(END, self.s[i][1])
                self.tex2.insert(END, self.s[i][2])
                self.tex3.insert(END, self.s[i][3])
                self.tex4.insert(END, self.s[i][4])
                self.tex5.insert(END, self.s[i][5])
                self.tex6.insert(END, self.s[i][6])
                self.tex7.insert(END, self.s[i][7])
                self.tex8.insert(END, self.s[i][8])
                self.tex9.insert(END, self.s[i][9])
                self.tex10.insert(END, self.s[i][10])
                self.tex11.insert(END, self.s[i][11])
                self.tex12.insert(END, self.s[i][12])
                self.tex13.insert(END, self.s[i][13])
                self.tex14.insert(END, self.s[i][14])
                self.tex15.insert(END, self.s[i][15])
    def change(self):
        self.frame.destroy()
        ClocFrame(self.root)
    def change2(self):
        self.frame.destroy()
        calen_gui.CanlenFrame(self.root)


