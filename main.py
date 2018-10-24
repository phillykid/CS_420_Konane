from board import *
from minimax import *
from player import *

b = gameBoard(8, 8,1)
hp=HumanPlayer("W","B")
cp=ComputerSimplePlayer("B","W",3)

b.print_board()
#print(b.evaluate_board_desiarbility())
#print(b.print_w())
cp.getMove(b)
b.print_board()
hp.getMove(b)
b.print_board()
cp.getMove(b)
b.print_board()
hp.getMove(b)
b.print_board()





