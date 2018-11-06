import tkinter
import time
from board import *
from minimax import *
from player import *
import tkinter as tk
from tkinter import ttk
from gui import *

time_list = []
stats_list = []


# Use this if we are black and they are white

def play(b, cp, cp2):
    start_time = time.time()
    counter = 0

    while b.gameWon == gameBoard.STILLPLAYING:
        counter += 1
        if b.turn % 2 == 0:
            cp.getMove(b)
            if b.gameWon == gameBoard.STILLPLAYING:
                update_gui(b.toString(), counter, b)
        else:
            cp2.getMove(b)
            if b.gameWon == gameBoard.STILLPLAYING:
                update_gui(b.toString(), counter, b)
        if counter == 6:
            counter = 0
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- seconds per turn ---", (time.time() - start_time) / b.turn)
    get_stats(1)


# Use this if we are white and they are black

def play2(b, cp, cp2):
    start_time = time.time()
    counter = 0

    while b.gameWon == gameBoard.STILLPLAYING:
        counter += 1
        if b.turn % 2 == 0:
            cp2.getMove(b)
            if b.gameWon == gameBoard.STILLPLAYING:
                update_gui(b.toString(), counter, b)
        else:
            cp.getMove(b)
            if b.gameWon == gameBoard.STILLPLAYING:
                update_gui(b.toString(), counter, b)
        if counter == 6:
            counter = 0
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- seconds per turn ---", (time.time() - start_time) / b.turn)
    get_stats(1)


def run_game_10():
    for x in range(1):
        b = gameBoard(8, 8)
        # cp=ComputerSimplePlayer("B","W",4)
        # cp2=ComputerSimplePlayer("W","B",4)

        # cp=ComputerCastlePlayer("B","W",4)
        # cp2=ComputerCastlePlayer("W","B",4)

        # cp=ComputerEliminatorPlayer("B","W",4)
        # cp2=ComputerEliminatorPlayer("W","B",4)

        cp = ComputerAttritionPlayer("W", "B", 4)
        # cp2 = ComputerAttritionPlayer("W", "B", 4)
        cp2 = HumanPlayer("B", "W")
        start_time = time.time()
        play2(b, cp, cp2)
        time_list.append(time.time() - start_time)
    print(sum(time_list) / len(time_list))


def update_gui(board_string, counter, b):
    if counter % 6 == 0:
        board6.set(board_string)

    elif counter % 5 == 0:
        board5.set(board_string)

    elif counter % 4 == 0:
        board4.set(board_string)

    elif counter % 3 == 0:
        board3.set(board_string)

    elif counter % 2 == 0:
        board2.set(board_string)

    elif counter % 1 == 0:
        board1.set(board_string)

    b.print_board()
    root.update()


root = tk.Tk()
T = tk.Text(root, height=5, width=30)
T.pack()
T.insert(tk.END, "KONANE MASTERS\n              by\n     Luis Lopez-Bonilla\n        Albert Garcia")

gb = GameBoard(root)

style = tkinter.ttk.Style()
style.configure("BR.TLabel", foreground="#A76571", background="#D8DCFF", justify="center")
style.configure("RB.TLabel", foreground="#D8DCFF", background="#A76571", justify="center")

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

boardLabel6 = tkinter.ttk.Label(root, textvariable=board6, style="BR.TLabel")
boardLabel6.pack()

run_game_10()
