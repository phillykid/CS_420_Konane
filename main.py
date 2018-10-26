from board import *
from minimax import *
from player import *
import tkinter as tk
from tkinter import ttk
from gui import *


root = tk.Tk()
T = tk.Text(root, height=10, width=30)
T.pack()
T.insert(tk.END, "KONANE MASTERS\n               by\nLuis Lopez-Bonilla\n Albert Garcia")

gb=GameBoard(root)

style = ttk.Style()
style.configure("BR.TLabel", foreground="#A76571", background="#D8DCFF", justify="center")
style.configure("RB.TLabel", foreground="#D8DCFF", background="#A76571", justify="center")


board = tk.StringVar()
board.set("NO BOARD")
board1 = tk.StringVar()
board1.set("NO BOARD")
board2 = tk.StringVar()
board2.set("NO BOARD")
board3 = tk.StringVar()
board3.set("NO BOARD")

board4 = tk.StringVar()
board4.set("NO BOARD")

board5 = tk.StringVar()
board5.set("NO BOARD")

board6 = tk.StringVar()
board6.set("NO BOARD")

boardLabel = ttk.Label(root, textvariable=board, style="BR.TLabel")
boardLabel.pack()

boardLabel1 = ttk.Label(root, textvariable=board1, style="RB.TLabel")
boardLabel1.pack()

boardLabel2 = ttk.Label(root, textvariable=board2, style="BR.TLabel")
boardLabel2.pack()

boardLabel3 = ttk.Label(root, textvariable=board3, style="RB.TLabel")
boardLabel3.pack()

boardLabel4 = ttk.Label(root, textvariable=board4, style="BR.TLabel")
boardLabel4.pack()

boardLabel5 = ttk.Label(root, textvariable=board5, style="RB.TLabel")
boardLabel5.pack()


b = gameBoard(8, 8,1)
#hp=HumanPlayer("W","B")
cp=ComputerSimplePlayer("B","W",4)
cp2=ComputerSimplePlayer("W","B",4)


b.print_board()
#print(b.evaluate_board_desiarbility())
#print(b.print_w())
while(b.gameWon==gameBoard.STILLPLAYING):
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

    cp.getMove(b)
    b.print_board()
    board4.set(b.toString())
    root.update()
    cp2.getMove(b)
    b.print_board()
    board5.set(b.toString())
    root.update()







