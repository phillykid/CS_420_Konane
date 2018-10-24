from board import *

class pieceTracker():
    def __init__(self,rows):
        self.total_pieces=[[0 for x in range(rows)] for y in range(rows)]
        self.black_pieces={}
        self.white_pieces={}

    def add_piece(self,color,cost,x,y):
        current_piece = gamePiece(color,cost,x,y)

        if color == gameBoard.BLACK_ICON:
            self.total_pieces[current_piece.x][current_piece.y]=current_piece
            self.black_pieces[current_piece.piece_id]=current_piece
        else:
            self.total_pieces[current_piece.x][current_piece.y]=current_piece
            self.white_pieces[current_piece.piece_id]=current_piece
        return color

    def update_game_piece_position(self,x1,y1,x2, y2):
        self.total_pieces[x2][y2]=self.total_pieces[x1][y1]
        self.total_pieces[x2][y2].update_coordinates(x2,y2)
        self.total_pieces[x1][y1]=None



class gamePiece():
    id=1

    def __init__(self, color, cost, x,y):
        self.color=color
        self.piece_id=gamePiece.id
        gamePiece.id=gamePiece.id+1
        self.cost=cost
        self.x=x
        self.y=y

    def update_coordinates(self,x,y):
        self.x=x
        self.y=y


    def get_id(self):
        return self.piece_id


