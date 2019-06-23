from tkinter import*
import random
class TicTacToe:
    def pressed(self, r, c):
        if self.end==True:
            if self.check[r * 3 + c] == True:
                if self.turn:  # x차례
                    self.buttonList[r * 3 + c].configure(image=self.imageList[0])
                    self.explain.configure(text="X 차례")
                    self.grid[r * 3 + c] = 'x'
                    self.count+=1
                else:  # o차례
                    self.buttonList[r * 3 + c].configure(image=self.imageList[1])
                    self.explain.configure(text="O 차례")
                    self.grid[r * 3 + c] = 'O'
                    self.count+=1
                self.turn = not self.turn
                pass
                self.check[r * 3 + c] = False
                self.win()

    def win(self):
        for r in range(3):
            if self.grid[r * 3] == self.grid[r * 3 + 1] == self.grid[r * 3 + 2]:
                if self.turn:
                    self.explain.configure(text="X 승리!")
                    self.end=False
                else:
                    self.explain.configure(text="O 승리!")
                    self.end = False
            if self.grid[r]==self.grid[r+3]==self.grid[r+6]:
                if self.turn:
                    self.explain.configure(text="X 승리!")
                    self.end = False
                else:
                    self.explain.configure(text="O 승리!")
                    self.end = False
        if self.grid[0]==self.grid[4]==self.grid[8]:
            if self.turn:
                self.explain.configure(text="X 승리!")
                self.end = False
            else:
                self.explain.configure(text="O 승리!")
                self.end = False
        if self.grid[2] == self.grid[4] == self.grid[6]:
            if self.turn:
                self.explain.configure(text="X 승리!")
                self.end = False
            else:
                self.explain.configure(text="O 승리!")
                self.end = False
        if self.count==9 and self.end==True:
            self.explain.configure(text="무승부...")
            self.end = False

    def __init__(self):
        window = Tk()
        window.geometry("130x170+100+100")
        window.resizable(True, True)
        self.imageList = []
        self.imageList.append(PhotoImage(file='circle.gif'))
        self.imageList.append(PhotoImage(file='cross.gif'))
        self.imageList.append(PhotoImage(file='empty.gif'))
        self.buttonList = []
        self.turn = True    # True = O차례, False = X 차례
        self.end=True
        self.check=[]       # 각 버튼 체크 유무
        self.grid=[]
        self.count=0
        frame1 = Frame(window)
        frame1.pack()
        for r in range(3):
            for c in range(3):
                self.buttonList.append(
                    Button(frame1, image=self.imageList[2], command=lambda Row = r, Col = c:self.pressed(Row, Col)))
                self.buttonList[r*3+c].grid(row=r, column=c)
                self.check.append(True)
                self.grid.append(r*3+c)
        frame2 = Frame(window)
        frame2.pack()
        self.explain = Label(frame2, text="O 차례")
        self.explain.pack()

        window.mainloop()

TicTacToe()