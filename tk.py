from tkinter import *
import tkinter.ttk
from mapp import*
from mail import*
from seoul import GetInfo

class GUI:
    def map(self):
        Lati = 0
        Longi = 0
        name=[]
        for i in self.row:
            if self.chec1==i.get('stationName'):
                Lati=float(i.get('stationLatitude'))
                Longi=float(i.get('stationLongitude'))
                name=str(i.get('stationName'))

        map(Lati,Longi,name)

    def click(self):

        Send(self.p3tb.get(1.0,"end"))
        self.ll3.config(text='전송 완료')
        self.p3tb.delete(1.0,"end")


    def search(self):
        num = 0
        self.listbox.delete(0, self.listbox.size())
        name = self.inputEntry.get()
        category = self.combobox.get()
        if category == '지역구명':
            if name[-1] != '구':
                name += '구'
            for i in range(len(self.row) - 1):
                if name == str(self.row[i]['gooName']):
                    self.listbox.insert(num, self.row[i]['stationName'])
                    num += 1
        elif category == '대여소명':
            for i in range(len(self.row) - 1):
                if name in str(self.row[i]['stationName']):
                    self.listbox.insert(num, self.row[i]['stationName'])
                    num += 1
    def add(self):
        num=0
        check= self.listbox.get(self.listbox.curselection())
        for j in range(self.listbox.index("end")):
            check1=self.listbox1.get(self.listbox1.index(j))
            if check1==check:
                return
        for i in self.row:
            if i.get('stationName')==check:
                self.listbox1.insert(num, i.get('stationName'))
                num += 1

    def choice1(self):
        check= self.listbox.get(self.listbox.curselection())
        self.chec1=check
        self.Rtext.delete(1.0,tkinter.END)
        for i in self.row:
            if i.get('stationName') == check:
                self.Rtext.insert("insert", "대여소 명: \n")
                self.Rtext.insert("insert", str(i.get('stationName')) + "\n")
                self.Rtext.insert("insert", "자전거 거치대 수: " + str(i.get('rackTotCnt') + "\n"))
                self.Rtext.insert("insert", "자전거 총 주차건수: " + str(i.get('parkingBikeTotCnt')) + "\n")
                self.Rtext.insert("insert", "대여소 ID: " + str(i.get('stationId')) + "\n")

    def choice2(self):
        check=self.listbox1.get(self.listbox1.curselection())
        self.chec1 = check
        self.Rtext2.delete(1.0,tkinter.END)
        for i in self.row:
            if i.get('stationName') == check:
                self.Rtext2.insert("insert", "대여소 명: \n")
                self.Rtext2.insert("insert", str(i.get('stationName')) + "\n")
                self.Rtext2.insert("insert", "자전거 거치대 수: " + str(i.get('rackTotCnt') + "\n"))
                self.Rtext2.insert("insert", "자전거 총 주차건수: " + str(i.get('parkingBikeTotCnt')) + "\n")
                self.Rtext2.insert("insert", "대여소 ID: " + str(i.get('stationId')) + "\n")


    def __init__(self):
        self.row = GetInfo()

        window = Tk()
        window.title("공공자전거 따릉이")
        window.geometry("600x400+100+100")
        window.resizable(False, False)

        self.chec1 = []

        nb=tkinter.ttk.Notebook(window,height=400,width=600)
        nb.pack()

        self.Page1 = Frame(window, height=400,width=600 ,relief='solid', bd=2)
        self.Page2 = Frame(window, height=400, width=600, relief='solid', bd=2)
        self.Page3 = Frame(window, height=400, width=600, relief='solid', bd=2)

        self.p1Frame1 = Frame(self.Page1, height=100, width=600, relief='solid', bd=2)
        self.p1Frame2 = Frame(self.Page1,height=300, width=100, relief='solid', bd=2)
        self.p1Frame3 = Frame(self.Page1,height=300, width=10, relief='solid', bd=2)

        self.p2Frame1= Frame(self.Page2,height=300, width=100, relief='solid', bd=2)
        self.p2Frame2 = Frame(self.Page2, height=300, width=100, relief='solid', bd=2)

        self.Page1.pack()
        self.p1Frame1.pack(side="top", fill='both', expand='true',)
        self.p1Frame2.pack(side="left", expand='true', fill="both")
        self.p1Frame3.pack(side="right", expand="true", fill="both")

        self.Page2.pack()
        self.p2Frame1.pack(side='left',expand='true',fill='both')
        self.p2Frame2.pack(side='right',expand='true',fill='both')

        self.Page3.pack()


        nb.add(self.Page1, text="검색")
        nb.add(self.Page2, text="즐겨찾기")
        nb.add(self.Page3, text="문의하기")

        # page1
        # frame1
        # values=['지역구명','대여소명']
        self.combobox = tkinter.ttk.Combobox(self.p1Frame1, width=10, height=3, values=['지역구명', '대여소명'])
        self.combobox.set("목록 선택")
        self.combobox.current(1)
        self.inputEntry = Entry(self.p1Frame1, width=30)
        self.button = Button(self.p1Frame1,width=5, text="검색", command=self.search)

        self.combobox.place(x=100, y=51)
        self.inputEntry.place(x=200, y=52)
        self.button.place(x=420, y=48)
        # frame2
        self.scrollbar = Scrollbar(self.p1Frame2)
        self.listbox = tkinter.Listbox(self.p1Frame2, height=10,width=30, yscrollcommand=self.scrollbar.set, selectmode='single')
        self.scrollbar["command"] = self.listbox.yview
        self.button2=Button(self.p1Frame2,text="선택",command=self.choice1)

        self.scrollbar.pack(side='right')
        self.listbox.place(x=40, y=30)
        self.button2.place(x=130, y=200)

        # frame3
        self.tIndex=0
        self.Rtext = Text(self.p1Frame3,height=12,width=30)
        self.button3 = Button(self.p1Frame3, text="즐겨찾기", command=self.add)
        self.button4=Button(self.p1Frame3,text="상세정보",command=self.map)

        self.Rtext.place(x=45, y=30)
        self.button3.place(x=70, y=200)
        self.button4.place(x=170,y=200)

        # page2
        self.scrollbar1 = tkinter.Scrollbar(self.p2Frame1)
        #self.scrollbar1.place(x=250, y=200, height=100)
        self.listbox1 = tkinter.Listbox(self.p2Frame1, yscrollcommand=self.scrollbar.set, selectmode='single')
        self.listbox1.place(x=50, y=50)
        self.scrollbar1["command"] = self.listbox.yview
        self.scrollbar1.pack(side='right')
        self.Rtext2 = Text(self.p2Frame2, height=12, width=30)
        self.Rtext2.place(x=45, y=50)
        self.button2_2 = Button(self.p2Frame1, text="선택", command=self.choice2)
        self.button2_2.place(x=105, y=230)

        self.button2_3=Button(self.p2Frame2,text='지도',command=self.map)
        self.button2_3.place(x=135,y=230)


        #page3
        self.ll3=Label(self.Page3,text='메일 문의')
        self.p3tb=Text(self.Page3,height=12,width=30)
        self.B3=Button(self.Page3,text='클릭',command=self.click)

        self.ll3.pack()
        self.p3tb.pack()
        self.B3.pack()

        window.mainloop()

GUI()

