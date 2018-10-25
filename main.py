from board import *
from minimax import *
from player import *
from tkinter import *

root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")
board = StringVar()
board.set("NO BOARD")
board1 = StringVar()
board1.set("NO BOARD")
board2 = StringVar()
board2.set("NO BOARD")
board3 = StringVar()
board3.set("NO BOARD")


boardLabel = Label(root, textvariable=board)
boardLabel.pack()

boardLabel1 = Label(root, textvariable=board1)
boardLabel1.pack()

boardLabel2 = Label(root, textvariable=board2)
boardLabel2.pack()

boardLabel3 = Label(root, textvariable=board3)
boardLabel3.pack()

b = gameBoard(8, 8,1)
#hp=HumanPlayer("W","B")
cp=ComputerSimplePlayer("B","W",4)
cp2=ComputerSimplePlayer("W","B",4)


b.print_board()
#print(b.evaluate_board_desiarbility())
#print(b.print_w())
while(True):
    cp.getMove(b)
    b.print_board()
    board.set(b.toString())
    root.update()
    cp2.getMove(b)
    b.print_board()
    board1.set(b.toString())
    root.update()
    cp.getMove(b)
    b.print_board()
    board2.set(b.toString())
    root.update()
    cp2.getMove(b)
    b.print_board()
    board3.set(b.toString())
    root.update()






