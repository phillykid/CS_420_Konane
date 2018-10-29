import tkinter
import time
from board import *
from minimax import *
from player import *
import tkinter as tk
from tkinter import ttk
from gui import *


root = tk.Tk()
T = tk.Text(root, height=5, width=30)
T.pack()
T.insert(tk.END,        "KONANE MASTERS\n              by\n     Luis Lopez-Bonilla\n        Albert Garcia")

gb=GameBoard(root)

style = tkinter.ttk.Style()
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

boardLabel = tkinter.ttk.Label(root, textvariable=board, style="BR.TLabel")
boardLabel.pack()

boardLabel1 = tkinter.ttk.Label(root, textvariable=board1, style="RB.TLabel")
boardLabel1.pack()

boardLabel2 = tkinter.ttk.Label(root, textvariable=board2, style="BR.TLabel")
boardLabel2.pack()

boardLabel3 = tkinter.ttk.Label(root, textvariable=board3, style="RB.TLabel")
boardLabel3.pack()

boardLabel4 = tkinter.ttk.Label(root, textvariable=board4, style="BR.TLabel")
boardLabel4.pack()

boardLabel5 = tkinter.ttk.Label(root, textvariable=board5, style="RB.TLabel")
boardLabel5.pack()


b = gameBoard(8, 8, 1)

print("INITIAL BOARD SETUP:")
print(b)

# First we have to do preliminary moves
print()
print("BLACK REMOVES A PIECE: ")
black_piece, black_choice, turn = b.first_two_moves_picker(0)
b.computer_move(str(black_piece.x)+str(black_piece.y), black_choice)
print(b)

print()
print("WHITE REMOVES A PIECE: ")
white_piece, white_choice, turn = b.first_two_moves_picker(0)
b.computer_move(str(white_piece.x)+str(white_piece.y), white_choice)
print(b)

# End of preliminary moves



#hp=HumanPlayer("W","B")
cp=ComputerSimplePlayer("B","W",2)
cp2=ComputerSimplePlayer("W","B",2)

#print(b.evaluate_board_desiarbility())
#print(b.print_w())
start_time = time.time()
while(b.gameWon == gameBoard.STILLPLAYING):
    if b.turn%2==0:
        cp.getMove(b)
        b.print_board()
        board.set(b.toString())
        root.update()
    else:
        cp2.getMove(b)
        b.print_board()
        board1.set(b.toString())
        root.update()
#get_stats()
print("--- %s seconds ---" % (time.time() - start_time))
print("--- seconds per turn ---" ,(time.time() - start_time)/b.turn)
