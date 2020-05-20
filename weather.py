import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *


def get_all_html(demo):
    soup = BeautifulSoup(demo, 'html.parser')
    articles = soup.find("div", class_="inter_weather main")
    SSS = articles.find("div", class_="inter_continent")
    SSSS = SSS.find("div", class_="continent_list chooseBox clearfix")
    SSSSS = SSSS.find_all("li")
    HREF = []
    for i in range(len(SSSSS)):
        HREF.append("https://www.tianqi.com" + SSSSS[i].find("a")["href"])
    return HREF


def parse_single_html(html):
    r = requests.get(html, headers=headers, timeout=500)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find("div", class_="inter_cityweather mgb_ul clearfix")
    place = articles.find_all("li")
    place_info = soup.find("div", class_="tit")
    weather = [place_info.text[1:14]]
    for i in range(len(place) - 1):
        weather.append(place[i].find("a")["title"])
    return weather


url_root = "https://www.tianqi.com/worldcity.html"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
r_root = requests.get(url_root, headers=headers, timeout=500)
r_root.encoding = "UTF-8"
demo1 = r_root.text
a = get_all_html(demo1)
s = []
for num in range(len(a)):
    s.append(parse_single_html(a[num]))
print(s)
window = tk.Tk()
window.title('weather')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('700x500')


def show_weather():
    l3 = tk.Label(window, text=place_name.get()).place(x=100, y=400)
    for i in range(len(s)):
        if place_name.get()[0:2] == s[i][0][0:2]:
            str1.set(s[i][1])
            str2.set(s[i][2])
            str3.set(s[i][3])
            str4.set(s[i][4])
            str5.set(s[i][5])
            str6.set(s[i][6])
            str7.set(s[i][7])
            str8.set(s[i][8])
            str9.set(s[i][9])
            str10.set(s[i][10])
            str11.set(s[i][11])
            str12.set(s[i][12])
            str13.set(s[i][13])
            str14.set(s[i][14])
            str15.set(s[i][15])


str1 = StringVar()
str2 = StringVar()
str3 = StringVar()
str4 = StringVar()
str5 = StringVar()
str6 = StringVar()
str7 = StringVar()
str8 = StringVar()
str9 = StringVar()
str10 = StringVar()
str11 = StringVar()
str12 = StringVar()
str13 = StringVar()
str14 = StringVar()
str15 = StringVar()
place_name = StringVar()
l1 = tk.Label(window, text='请输入您想查询的国家', font=('Arial', 12)).place(x=20, y=10)
lab1 = Label(window, textvariable=str1, font=('Arial', 9)).place(x=100, y=150)
lab2 = Label(window, textvariable=str2, font=('Arial', 9)).place(x=300,y=150)
lab3 = Label(window, textvariable=str3, font=('Arial', 9)).place(x=500,y=150)
lab4 = Label(window, textvariable=str4, font=('Arial', 9)).place(x=100,y=200)
lab5 = Label(window, textvariable=str5, font=('Arial', 9)).place(x=300,y=200)
lab6 = Label(window, textvariable=str6, font=('Arial', 9)).place(x=500,y=200)
lab7 = Label(window, textvariable=str7, font=('Arial', 9)).place(x=100,y=250)
lab8 = Label(window, textvariable=str8, font=('Arial', 9)).place(x=300,y=250)
lab9 = Label(window, textvariable=str9, font=('Arial', 9)).place(x=500,y=250)
lab10 = Label(window, textvariable=str10, font=('Arial', 9)).place(x=100,y=300)
lab11 = Label(window, textvariable=str11, font=('Arial', 9)).place(x=300,y=300)
lab12 = Label(window, textvariable=str12, font=('Arial', 9)).place(x=500,y=300)
lab13 = Label(window, textvariable=str13, font=('Arial', 9)).place(x=100,y=350)
lab14 = Label(window, textvariable=str14, font=('Arial', 9)).place(x=300,y=350)
lab15 = Label(window, textvariable=str15, font=('Arial', 9)).place(x=500,y=350)
b = tk.Button(window, text='确定', command=show_weather).place(x=400, y=50)
e = tk.Entry(window, show=None, textvariable=place_name, font=('Arial', 14)).place(x=400, y=10)
l2 = tk.Label(window, text='该国家主要地区的天气情况', font=('Arial', 12)).place(x=170, y=110)
# 第5步，主窗口循环显示
window.mainloop()