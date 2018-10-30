from alpha_beta_pruning import alpha_beta_pruning
from minimax import *

def get_stats():
    print("Branch Totals: ",Minimax_tracker.total_branches)
    print("Eval Calls: ",Minimax_tracker.total_evauls)
    print("Cutoff Totals",Minimax_tracker.total_cut_offs)
    print("Avg Branching Factor: ",Minimax_tracker.total_branches/Minimax_tracker.total_parents)
    print("Eval Calls: ",Minimax_tracker.total_evauls)
    print("Cutoff Totals",Minimax_tracker.total_cut_offs)


class HumanPlayer():
    def __init__(self,color,opponent_color):
        name = "Human"
        self.color=color
        self.o_color=opponent_color
        
    def getMove(self,board):
        check=0;
        if board.terminal_state():
            print("Game Over")
            board.player_has_no_moves(self.color)
            print(board.gameWon)
        while(check==0):
            move = input()
            print(move)
            if board.turn == 0 or board.turn == 1:
                check = board.human_move_start(move)
                print(check)
            else:
                check = board.human_move(move)
    


class ComputerSimplePlayer():
    def __init__(self,color,opponent_color,depth_limit):
        name = "Computer_Simple_Player"
        self.color=color
        self.o_color=opponent_color
        self.depth_limit=depth_limit

    def getMove(self,board):
        #bboard,score,move= Minimax_tracker.minimax(board,0,self.depth_limit,1)
        move = alpha_beta_pruning(board, 0, self.depth_limit)
        print("Move:",move)
        if move==None:
            #print(self.color,"GAME LOSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            board.player_has_no_moves(self.color)
            print(board.gameWon)
            return
        board.computer_move(move[0],move[1])


class ComputerCastlePlayer():
    def __init__(self,color,opponent_color,depth_limit):
        name = "Computer_Simple_Player"
        self.color=color
        self.o_color=opponent_color
        self.depth_limit=depth_limit

    def getMove(self,board):
        bboard,score,move= Minimax_tracker.minimax(board,0,self.depth_limit,2)
        #move = alpha_beta_pruning(board, 0, self.depth_limit)
        print("Move:",move)
        if move==None:
            print(self.color,"GAME LOSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            board.player_has_no_moves(self.color)
            print(board.gameWon)

            return
        board.computer_move(move[0],move[1])


class ComputerEliminatorPlayer():
    def __init__(self,color,opponent_color,depth_limit):
        name = "Computer_Simple_Player"
        self.color=color
        self.o_color=opponent_color
        self.depth_limit=depth_limit

    def getMove(self,board):
        bboard,score,move= Minimax_tracker.minimax(board,0,self.depth_limit,3)
        #move = alpha_beta_pruning(board, 0, self.depth_limit)
        print("Move:",move)
        if move==None:
            print(self.color,"GAME LOSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            board.player_has_no_moves(self.color)
            print(board.gameWon)
            return
        board.computer_move(move[0],move[1])


class ComputerAttritionPlayer():
    def __init__(self,color,opponent_color,depth_limit):
        name = "Computer_Simple_Player"
        self.color=color
        self.o_color=opponent_color
        self.depth_limit=depth_limit

    def getMove(self,board):
        bboard,score,move= Minimax_tracker.minimax(board,0,self.depth_limit,4)
        #move = alpha_beta_pruning(board, 0, self.depth_limit)
        print("Move:",move)
        if move==None:
            print(self.color,"GAME LOSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            board.player_has_no_moves(self.color)
            print(board.gameWon)
            return
        board.computer_move(move[0],move[1])




