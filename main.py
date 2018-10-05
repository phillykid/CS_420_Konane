from board import *
game_turn=0;
b = gameBoard(8, 8, 1)
b.print_board()
coordinates = input("Coordinate of Piece to be moved and destination (from 0 0 to 7 7)").split()
if game_turn<2:
    b.move_piece(coordinates[0] + coordinates[1], coordinates[2] + coordinates[3])
b.print_board()
print(b.evaluate_board_desiarbility())
