from tkinter import*
import random
class TicTacToe:
    def pressed(self, r, c):
        if self.end==True:
            if int(self.linecount[c]<6) :
                 if self.turn:  # x차례
                     self.buttonList[r+(5-r-int(self.linecount[c]))][c].configure(image=self.imageList[0])
                     self.explain.configure(text="X 차례")
                     #self.explain.configure(text=int(self.linecount[c]))
                     self.grid[5-int(self.linecount[c])][c] = 'x'
                     self.linecount[c] = 1+int(self.linecount[c])
                     self.count+=1
                 else:  # o차례
                     self.buttonList[r+(5-r-int(self.linecount[c]))][c].configure(image=self.imageList[1])
                     self.explain.configure(text="O 차례")
                     #self.explain.configure(text=int(self.linecount[c]))
                     self.grid[5-int(self.linecount[c])][c] = 'O'
                     self.linecount[c] = 1+int(self.linecount[c])
                     self.count+=1
                 self.turn = not self.turn
                 pass

                 self.win()

    def win(self):
        for r in range(6):
            for c in range(7):
                if c+3<=6:
                    if self.grid[r][c] == self.grid[r][c + 1] == self.grid[r][c + 2] == self.grid[r][c + 3]:
                        if self.turn:
                            self.explain.configure(text="X 승리!")
                            self.end = False
                        else:
                            self.explain.configure(text="O 승리!")
                            self.end = False
                if r + 3 <= 5:
                    if self.grid[r][c] == self.grid[r+1][c] == self.grid[r+2][c] == self.grid[r+3][c]:
                        if self.turn:
                            self.explain.configure(text="X 승리!")
                            self.end = False
                        else:
                            self.explain.configure(text="O 승리!")
                            self.end = False
                if r+3<=5 and c+3<=6:
                    if self.grid[r][c] == self.grid[r+1][c + 1] == self.grid[r+2][c + 2] == self.grid[r+3][c + 3]:
                        if self.turn:
                            self.explain.configure(text="X 승리!")
                            self.end = False
                        else:
                            self.explain.configure(text="O 승리!")
                            self.end = False
                if r - 3 >= 0 and c + 3 <= 6:
                    if self.grid[r][c] == self.grid[r - 1][c + 1] == self.grid[r - 2][c + 2] == self.grid[r - 3][c + 3]:
                        if self.turn:
                            self.explain.configure(text="X 승리!")
                            self.end = False
                        else:
                            self.explain.configure(text="O 승리!")
                            self.end = False

    def __init__(self):
        window = Tk()
        window.geometry("800x600+100+100")
        window.resizable(True, True)
        self.imageList = []
        self.imageList.append(PhotoImage(file='circle.gif'))
        self.imageList.append(PhotoImage(file='cross.gif'))
        self.imageList.append(PhotoImage(file='empty.gif'))
        self.buttonList = []
        self.turn = True    # True = O차례, False = X 차례
        self.end=True
        self.grid=[]
        self.count=0
        self.linecount=[0,0,0,0,0,0,0]
        frame1 = Frame(window)
        frame1.pack()
        for r in range(6):
            self.grid.append([])
            self.buttonList.append([])
            for c in range(7):
                self.buttonList[r].append(
                    Button(frame1, image=self.imageList[2], command=lambda Row = r, Col = c:self.pressed(Row, Col)))
                self.buttonList[r][c].grid(row=r, column=c)
                self.grid[r].append(r*7+c)
        frame2 = Frame(window)
        frame2.pack()
        self.explain = Label(frame2, text="O 차례")
        self.explain.pack()

        window.mainloop()

print(TicTacToe().grid)