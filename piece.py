from board import *


class gamePiece():
    id = 1  # used as identifer for all pieces gets changed on new piece creation

    def __init__(self, color, cost, x, y):
        self.color = color
        self.piece_id = gamePiece.id
        gamePiece.id = gamePiece.id + 1
        self.cost = cost
        self.x = x
        self.y = y

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_id(self):
        return self.piece_id

    def __str__(self):
        return "Piece Color: " + str(self.color) + " | " + "Coordinates: (" + str(self.x) + ", " + str(self.y) + ")"
