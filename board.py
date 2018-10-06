# Game Board requires height and width dimensions.
from piece import *
import random

"""
GameBoard has been to designed to work with 6x6 or 8x8 boards.
Other formats are not guaranteed nor expected to work.
"""

class gameBoard():
    WHITE=1
    BLACK=-1
    STILLPLAYING=0
    BLACK_ICON="1"  #black circle
    WHITE_ICON="0"


    def add_piece(self,color,cost,x,y):
        current_piece = gamePiece(color,cost,x,y)

        if color == 1:
            self.total_pieces[current_piece.x][current_piece.y]=current_piece
            self.black_pieces[current_piece.piece_id]=current_piece
        else:
            self.total_pieces[current_piece.x][current_piece.y]=current_piece
            self.white_pieces[current_piece.piece_id]=current_piece
        return color

    def update_game_piece_position(self,x1,y1,x2, y2):
        if not x2 == None and y2 ==None:
            self.total_pieces[x2][y2]=self.total_pieces[x1][y1]
            self.total_pieces[x2][y2].update_coordinates(x2,y2)
            self.total_pieces[x1][y1]="-"
        else:
            piece_to_remove=self.total_pieces[x1][y1]
            self.total_pieces[x1][y1]="-"
            if piece_to_remove.color == 1:
                del self.black_pieces[piece_to_remove.piece_id]



    def __init__(self, height, width, startingPlayer):
        """
        Constructs a board with given dimensions and sets the inital player turn ordering.
        """

        self.width=width
        self.height=height
        self.turn=1
        self.total_pieces=[[" " for x in range(width)] for y in range(width)]
        self.black_pieces={}
        self.white_pieces={}

        for i in range(width):
            for j in range(height):
                if (j+i)%2 == 0:
                    self.add_piece(1,1,i,j)
                else:
                    self.add_piece(0,-1,i,j)


        self.gameWon = self.STILLPLAYING
        self.turn = startingPlayer
        self.maxDepth = 10





    def print_board(self):
        s=""
        for h in range(self.height):
            for w in range(self.width):
                piece=self.total_pieces[h][w]
                if not piece == "-":
                    s=s+str(self.total_pieces[h][w].color)+"  "
                else:
                    s=s+"-- "
            s=s+" \n"
        print(s)


    def move_piece(self,piece_coordinates,destination_coordinates):
        x1,y1 = piece_coordinates
        x2,y2 = destination_coordinates
        print(x1+y1)
        print(type(x1+y1))
        if(destination_coordinates == '--'):
            self.update_game_piece_position(int(x1),int(y1),None,None)
        else:
            self.update_game_piece_position(int(x1),int(y1),int(x2),int(y2))
        self.turn=self.turn+1


    def check_is_move_legal(self,move):
        return 0



    def expand_white_moves(self):

        for key, piece in self.white_pieces.items():
            for move in self.expand_moves_for_piece(piece):
                print("moves?")
                yield piece,move

    def print_w(self):
        g=self.expand_white_moves()
        for i in g:
            print(i)

    def expand_black_moves(self):
        for key, piece in self.black_pieces.items():
            for move in self.expand_moves_for_piece(piece):
                print(piece.x,piece.y,"addddddddddddadadadadadadadda")
                yield piece,move


    def expand_moves_for_piece(self, piece):
        return self.iterBoth(piece)


    def first_two_moves_picker(self):
        pieces=[self.total_pieces[0][0],self.total_pieces[self.width-1][self.height-1]
            ,self.total_pieces[int(self.width/2)][int(self.height/2)],
                self.total_pieces[int((self.width/2)-1)][int((self.height/2)-1)]]

        id_list=[]
        for it in pieces:
            id_list.append(it.piece_id)
        if self.turn == 1:
                print("did")
        else:
            print("dont")
            white_has_to_pick_adjacent = None
            for it in pieces:
                if not it.piece_id in self.black_pieces:
                    white_has_to_pick_adjacent=it
            print(white_has_to_pick_adjacent.piece_id)
            white_choice = random.choice(self.generate_set_of_legal_moves_for_second_move(white_has_to_pick_adjacent))
            return self.total_pieces[white_choice[0]][white_choice[1],"--",self.turn+1]



        return (random.choice(pieces),"--",self.turn+1)


    def generate_set_of_legal_moves_for_second_move(self,adjacent):
        moves=[(-1,0),(1,0),(0,1),(0,-1)]
        legal_pieces_to_remove=[]
        for move in moves:
            white_choice_x=move[0]+adjacent.x
            white_choice_y=move[1]+adjacent.y
            if not (self.width > white_choice_x > -1 and self.height > white_choice_y > -1):
                continue
            legal_pieces_to_remove.append(white_choice_x,white_choice_y)





    """
    The general movement options are the 4 cardinals:
    (-1,0)Left, (1,0)Right, (0,-1)Down, (0,1)Up. 

    The method below returns all possible legal moves from those above and 
    returns it will a turn counter to keep track of player switch. 

    """
    def iter_for_all_moves(self,piece):
        moves=[(-1,0),(1,0),(0,1),(0,-1)]



        for move in moves:
            destination_x=move[0]+piece.x
            destination_y=move[1]+piece.y

            # print(destination_y,"2222")
            # print(destination_x,"33333")
            # print(self.width > destination_x > -1)
            # print(self.height > destination_y > -1)
            # print(not(self.width > destination_x > -1 and self.height > destination_y > -1))

            if not (self.width > destination_x > -1 and self.height > destination_y > -1):
                continue
            # print(destination_y,"sss")
            # print(destination_x,"ssss")
            if self.total_pieces[destination_x][destination_y]=="-":
                yield (piece,move,self.turn+1)
            else:
                if piece.color == self.total_pieces[destination_x][destination_y].color:
                    continue

                landing_x=move[0]+piece.x+move[0]
                landing_y=move[1]+piece.y+move[1]

                if not (self.width > landing_x > -1 and self.height > landing_y > -1):
                    continue
                if self.total_pieces[landing_x][landing_y]=="-":
                    yield (piece,[[landing_x],[landing_y]],self.turn+1)


    def evaluate_board_desiarbility(self):
        if self.gameWon==1 and self.turn==0:
            return float('inf')
        if self.gameWon==1 and self.turn==1:
            return float('-inf')

        desirability=0

        for key, value in self.black_pieces.items():
            desirability+=value.cost
        for key, value in self.white_pieces.items():
            desirability+=value.cost

        return desirability











