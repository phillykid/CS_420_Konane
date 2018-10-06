from board import *
from minimax import *
game_turn=0;
b = gameBoard(8, 8, 1)
b.print_board()
#print(b.evaluate_board_desiarbility())
#print(b.print_w())
b=minimax(b,0,2)[0]
b.print_board()
print(b.total_pieces[2][1].color)

move = input("Coordinate of Piece to be moved and direction(u d l r) (EX: 0 0 u = moves to 0 1) (t)").split()
if game_turn<2:
    b.move_piece_human(move[0] + move[1], move[2])
b.print_board()
b=minimax(b,0,2)[0]


