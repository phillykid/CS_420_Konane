from minimax import *

class HumanPlayer():
    def __init__(self,color,opponent_color):
        name = "Human"
        self.color=color
        self.o_color=opponent_color
        
    def getMove(self,board):
        check=0;
        while(check==0):
            move = input("Coordinate of Piece to be moved and direction(u d l r) (EX: 0 0 u = moves to 0 1)").split()
            check = board.move_piece_human(move[0] + move[1], move[2])
    


class ComputerSimplePlayer():
    def __init__(self,color,opponent_color,depth_limit):
        name = "Computer_Simple_Player"
        self.color=color
        self.o_color=opponent_color
        self.depth_limit=depth_limit

    def getMove(self,board):
        bboard,score,move= minimax(board,0,self.depth_limit)
        print(move)
        board.move_piece_computer(move[0],move[1])



