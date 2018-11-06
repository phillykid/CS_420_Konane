from alpha_beta_pruning import ABTracker
from minimax import *


# Returns the given stats of the Minimax function
def get_stats(type):
    if type == 0:
        print("Branch Totals: ", Minimax_tracker.total_branches)
        print("Eval Calls: ", Minimax_tracker.total_evals)
        print("Cutoff Totals: ", Minimax_tracker.total_cut_offs)
        print("Avg Branching Factor: ", Minimax_tracker.total_branches / Minimax_tracker.total_non_leafs)
    if type == 1:
        print("Branch Totals: ", ABTracker.total_branches)
        print("Eval Calls: ", ABTracker.number_of_static_evaluations)
        print("Cutoff Totals: ", ABTracker.number_of_cut_offs)
        print("Avg Branching Factor: ", ABTracker.total_branches / ABTracker.max_min_calls)


"""
The different player types and the main differences are human vs computer and the evaluation function which that
computer play is going to use.
"""


class HumanPlayer():
    def __init__(self, color, opponent_color):
        name = "Human"
        self.color = color
        self.o_color = opponent_color

    def getMove(self, board):
        check = 0;
        while (check == 0):
            if board.turn == 0 or board.turn == 1:
                print("Enter value like this to remove a piece: 1,1")
                move = input()
                check = board.human_move_start(move)
            else:
                if board.terminal_state(self.color):
                    print(self.color, "Lost!")
                    board.player_has_no_moves(self.color)
                    print(board.gameWon)
                    check = 1
                else:
                    print("Enter string of moves like this: 1,1 to 1,3 to 1,5")
                    move2 = input()
                    check = board.human_move(move2)


# Makes moves based on the ratio between number of ally pieces and enemy pieces
class ComputerSimplePlayer:
    def __init__(self, color, opponent_color, depth_limit):
        name = "Computer_Simple_Player"
        self.color = color
        self.o_color = opponent_color
        self.depth_limit = depth_limit

    def getMove(self, board):
        #bboard,score,move= Minimax_tracker.minimax(board,0,self.depth_limit,1)
        move = ABTracker.alpha_beta_pruning(board, 0, self.depth_limit, 1)
        if move == None:
            print(self.color, "Lost!")
            board.player_has_no_moves(self.color)
            #print(board.gameWon)
            return
        board.computer_move(move[0], move[1])


# Decides moves based on the amount of moves that would be avaliable in the posistion
class ComputerCastlePlayer():
    def __init__(self, color, opponent_color, depth_limit):
        name = "Computer_Castle_Player"
        self.color = color
        self.o_color = opponent_color
        self.depth_limit = depth_limit

    def getMove(self, board):
        #bboard, score, move = Minimax_tracker.minimax(board, 0, self.depth_limit, 2)
        move = ABTracker.alpha_beta_pruning(board, 0, self.depth_limit, 2)
        print("Move:", move)
        if move == None:
            print(self.color, "GAME LOSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            board.player_has_no_moves(self.color)
            print(board.gameWon)

            return
        board.computer_move(move[0], move[1])


# Decides moves based on the amount of moves that the opponent will have avaliable in the posistion
class ComputerEliminatorPlayer():
    def __init__(self, color, opponent_color, depth_limit):
        name = "Computer_Eliminator_Player"
        self.color = color
        self.o_color = opponent_color
        self.depth_limit = depth_limit

    def getMove(self, board):
        #bboard, score, move = Minimax_tracker.minimax(board, 0, self.depth_limit, 3)
        move = ABTracker.alpha_beta_pruning(board, 0, self.depth_limit,3 )
        print("Move:", move)
        if move == None:
            print(self.color, "GAME LOSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            board.player_has_no_moves(self.color)
            print(board.gameWon)
            return
        board.computer_move(move[0], move[1])


# Decides moves based on the ratio between the amount of moves that the you and your opponent will have avaliable in the posistion
class ComputerAttritionPlayer():
    def __init__(self, color, opponent_color, depth_limit):
        name = "Computer_Attrition_Player"
        self.color = color
        self.o_color = opponent_color
        self.depth_limit = depth_limit

    def getMove(self, board):
        #bboard,score,move= Minimax_tracker.minimax(board,0,self.depth_limit,4)
        move = ABTracker.alpha_beta_pruning(board, 0, self.depth_limit, 4)
        #print("Move:", move)
        if move == None:
            # No move made so we don't count it towards its total moves
            print(self.color, "Lost!")
            board.player_has_no_moves(self.color)
            #print(board.gameWon)
            return
        board.computer_move(move[0], move[1])
