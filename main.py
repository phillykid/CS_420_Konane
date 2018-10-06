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

coordinates = input("Coordinate of Piece to be moved and destination (from 0 0 to 7 7)").split()
if game_turn<2:
    b.move_piece(coordinates[0] + coordinates[1], coordinates[2] + coordinates[3])
b.print_board()
b=minimax(b,0,2)[0]


