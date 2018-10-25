# Game Board requires height and width dimensions.
from piece import *
import random

"""
GameBoard has been to designed to work with 6x6 or 8x8 boards.
Other formats are not guaranteed nor expected to work.
"""

class gameBoard():
    WHITE=-1
    BLACK=1
    STILLPLAYING=0
    BLACK_ICON="B"  #black circle
    WHITE_ICON="W"


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
        print("Updating here")
        if not (x2 == None and y2 ==None):
            print(x1,y1,x2,y2,"babababbaba")
            print(x2 == None and y2 ==None,"pppppppppp")
            self.last_move="["+str(x1)+","+str(y1)+"]"+" to "+"["+str(x2)+","+str(y2)+"]"+"piece color: "+self.total_pieces[x1][y1].color
            self.total_pieces[x2][y2]=self.total_pieces[x1][y1]
            self.total_pieces[x2][y2].update_coordinates(x2,y2)
            self.total_pieces[x1][y1]="-"
        else:
            self.last_move="Removed ["+str(x1)+","+str(y1)+"]"+"piece color: "+self.total_pieces[x1][y1].color
            print(self.total_pieces[y1][x1].color)
            piece_to_remove=self.total_pieces[x1][y1]
            if piece_to_remove.color == gameBoard.BLACK_ICON:
                del self.black_pieces[piece_to_remove.piece_id]
            else:
                del self.white_pieces[piece_to_remove.piece_id]
            self.total_pieces[x1][y1]="-"







    def __init__(self, height, width,computer_is_first):
        """
        Constructs a board with given dimensions and sets the inital player turn ordering.
        """

        self.width=width
        self.height=height
        self.turn=0
        self.computer_is_first=computer_is_first
        self.total_pieces=[[" " for x in range(width)] for y in range(width)]
        self.black_pieces={}
        self.white_pieces={}
        self.last_move="No moves"

        self.draw_board(width,height)
        self.gameWon = self.STILLPLAYING
        self.maxDepth = 10

    def draw_board(self,width,height):
        for i in range(width):
            for j in range(height):
                if (j+i)%2 == 0:
                    self.add_piece(gameBoard.BLACK_ICON,1,i,j)
                else:
                    self.add_piece(gameBoard.WHITE_ICON,-1,i,j)


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

    def toString(self):
        s=""
        for h in range(self.height):
            for w in range(self.width):
                piece=self.total_pieces[h][w]
                if not piece == "-":
                    s=s+str(self.total_pieces[h][w].color)+"  "
                else:
                    s=s+"--- "
            s=s+"\n"
        s=s+"Turn:"+str(self.turn)+"\n"+"Last Move: "+self.last_move
        return s

    def is_legal_move(self,x1,y1,x2,y2):
        print("dest coordinates: ",x2,y2)
        if(self.turn<2):
            legal_moves = self.first_two_moves_picker(1)
            if [x1,y1] in legal_moves:
                return 1
            return 0

        print(x2,x1)
        difference_x=int(x2)-int(x1)
        difference_y=int(y2)-int(y1)
        pieces_jumped = []
        print("yodoododo")
        print()
        if (abs(difference_x)==2 and abs(difference_y)==0) or (abs(difference_x)==0 and abs(difference_y)==2):
            print("1sttt")
            if self.total_pieces[x2][y2] == '-':
                if difference_y == 2:
                    print("2sttt")

                    if self.total_pieces[x2][y2-1]=="-" or self.total_pieces[x2][y2-1].color == self.total_pieces[x1][y1].color:
                        return 0
                    else:
                        pieces_jumped.append([x2,y2-1])
                if difference_y == -2:
                    print("3sttt")
                    if self.total_pieces[x2][y2+1]=="-" or self.total_pieces[x2][y2+1].color == self.total_pieces[x1][y1].color:
                        return 0
                    else:
                        pieces_jumped.append([x2,y2+1])
                if difference_x == 2:
                    print("4sttt")
                    if self.total_pieces[x2-1][y2]=="-" or self.total_pieces[x2-1][y2].color == self.total_pieces[x1][y1].color:
                        return 0
                    else:
                        pieces_jumped.append([x2-1,y2])
                if difference_x == -2:
                    print("5sttt")
                    if self.total_pieces[x2+1][y2]=="-" or self.total_pieces[x2+1][y2].color == self.total_pieces[x1][y1].color:
                        return 0
                    else:
                        pieces_jumped.append([x2+1,y2])
                return 1

        return 0


    def list_of_jumped_pieces(self,x1,y1,x2,y2):
        print(x1,y1,x2,y2)
        if(x2 == None or y2== None):
            return []
        difference_x=int(x2)-int(x1)
        difference_y=int(y2)-int(y1)
        pieces_jumped = []

        print("got here so",difference_x,difference_y)
        if(abs(difference_x)==2 and abs(difference_y)==0) or (abs(difference_x)==0 and abs(difference_y)==2):
            print("almosttttttt")
            if self.total_pieces[x2][y2] == '-':
                print("closer")
                if difference_y == 2:
                    if self.total_pieces[x2][y2-1]!="-" and self.total_pieces[x2][y2-1].color != self.total_pieces[x1][y1].color:
                        pieces_jumped.append([x2,y2-1])

                if difference_y == -2:
                    if self.total_pieces[x2][y2+1]!="-" and self.total_pieces[x2][y2+1].color != self.total_pieces[x1][y1].color:
                        pieces_jumped.append([x2,y2+1])
                if difference_x == 2:

                    print("222222222")

                    if self.total_pieces[x2-1][y2]!="-" and self.total_pieces[x2-1][y2].color != self.total_pieces[x1][y1].color:
                        pieces_jumped.append([x2-1,y2])
                if difference_x == -2:
                    print("-222222222")
                    if self.total_pieces[x2+1][y2]!="-" and self.total_pieces[x2+1][y2].color != self.total_pieces[x1][y1].color:
                        pieces_jumped.append([x2+1,y2])


        return pieces_jumped

    def remove_piece_from_board(self,x,y):
        print("remocing piece")
        piece = self.total_pieces[x][y]
        self.total_pieces[x][y]="-"
        if piece.color == gameBoard.BLACK_ICON:
            del self.black_pieces[piece.piece_id]
        else:
            del self.white_pieces[piece.piece_id]




    def derive_coordinates(self,x1,y1,direction):
        if direction == 'u':
            return x1,y1-2
        if direction == 'd':
            return x1,y1+2
        if direction == 'l':
            return x1-2,y1
        if direction == 'r':
            return x1+2,y1
        if direction == 'p':
            return None,None

    def move_piece_computer(self,piece_coordinates,dest):
        x1,y1 = piece_coordinates
        x1 = int(x1)
        y1 = int(y1)
        print("computer moving",dest)
        if dest=="--":
            self.update_game_piece_position(x1,y1,None,None)
            self.turn=self.turn+1
            return
        x2=int(dest[1])
        y2=int(dest[0])
        print("first check",x1,y1,x2,y2)



        pieces_to_remove_after_move=self.list_of_jumped_pieces(x1,y1,x2,y2)
        self.update_game_piece_position(x1,y1,x2,y2)

        for piece in pieces_to_remove_after_move:
            print("looping")
            self.remove_piece_from_board(piece[0],piece[1])

        self.turn=self.turn+1


    def move_piece_human(self,piece_coordinates,direction):
        row,col = piece_coordinates
        x1 = int(col)
        y1 = int(row)
        x2=None
        y2=None
        direction_returned=self.derive_coordinates(x1,y1,direction)
        if not(direction_returned==None):
            x2=direction_returned[0]
            y2=direction_returned[1]
            if(self.is_legal_move(x1,y1,x2,y2) == 0):
                print("Illegal move please try again (Middle)")
                return 0
        else:
            if(self.is_legal_move(x1,y1,None,None) == 0):
                print("Illegal move please try again (Opening)")
                return 0



        print(x1+y1)
        print(type(x1+y1))
        if(direction == 'p'):
            self.update_game_piece_position(x1,y1,None, None)
        else:
            jumped = self.list_of_jumped_pieces(x1,y1,x2,y2)
            self.update_game_piece_position(x1,y1,x2,y2)
            for piece in jumped:
                self.remove_piece_from_board(piece[0],piece[1])
                print("sqqqqqqqqqqqqqqqqqqqqqqqq")
        self.turn=self.turn+1
        return 1





    def expand_white_moves(self):

        for key, piece in self.white_pieces.items():
            for move in self.expand_moves_for_piece(piece):
                yield piece,move

    def print_w(self):
        g=self.expand_white_moves()
        for i in g:
            print(i)

    def expand_black_moves(self):
        for key, piece in self.black_pieces.items():
            for move in self.expand_moves_for_piece(piece):
                print(piece.x,piece.y,"black move predicted")
                print(move[1][0])
                yield piece,move


    def expand_moves_for_piece(self, piece):
        return self.iter_for_all_moves(piece)



    def first_two_moves_picker(self,legal_check):
        pieces=[self.total_pieces[0][0],self.total_pieces[self.width-1][self.height-1]
            ,self.total_pieces[int(self.width/2)][int(self.height/2)],
                self.total_pieces[int((self.width/2)-1)][int((self.height/2)-1)]]
        coordinates=[[0,0],[self.width-1,self.height-1],
                     [int(self.width/2),int(self.height/2)],
                     [int((self.width/2)-1),int((self.height/2)-1)]]

        if self.turn == 0:
                print("did")
        else:
            white_has_to_pick_adjacent = None
            for it in coordinates:
                print(it)
                x=it[0]
                y=it[1]
                if self.total_pieces[x][y]=='-':
                    adj_x,adj_y=x,y
            if legal_check==1:
                return self.generate_set_of_legal_moves_for_second_move(adj_x,adj_y)
            white_choice = random.choice(self.generate_set_of_legal_moves_for_second_move(adj_x,adj_y))
            x=white_choice[0]
            y=white_choice[1]

            return self.total_pieces[y][x],"--",self.turn+1
        return (random.choice(pieces),"--",self.turn+1)


    def generate_set_of_legal_moves_for_second_move(self,adjacent_x,adjacent_y):
        moves=[(-1,0),(1,0),(0,1),(0,-1)]
        legal_pieces_to_remove=[]
        for move in moves:
            white_choice_x=move[0]+adjacent_x
            white_choice_y=move[1]+adjacent_y
            if not (self.width > white_choice_x > -1 and self.height > white_choice_y > -1):
                continue
            legal_pieces_to_remove.append([white_choice_x,white_choice_y])
        return legal_pieces_to_remove





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
                continue
            else:
                if piece.color == self.total_pieces[destination_x][destination_y].color:
                    continue

                landing_x=move[0]+piece.x+move[0]
                landing_y=move[1]+piece.y+move[1]

                if not (self.width > landing_x > -1 and self.height > landing_y > -1):
                    continue
                if self.total_pieces[landing_x][landing_y]=="-":
                    print("color:",self.total_pieces[destination_x][destination_y].color)
                    print(landing_x,landing_y)
                    print(piece.x,piece.y)

                    print(piece.color)

                    yield (piece,[landing_x,landing_y],self.turn+1)


    def evaluate_board_desiarbility(self):
        if self.gameWon==1 and self.turn%2==0:
            return float('inf')
        if self.gameWon==1 and self.turn%2==1:
            return float('-inf')

        desirability=0

        for key, value in self.black_pieces.items():
            desirability+=value.cost
        for key, value in self.white_pieces.items():
            desirability+=value.cost

        return desirability











