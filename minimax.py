from copy import deepcopy
class Minimax_tracker():
    total_branches=0
    total_cut_offs=0
    total_evauls=0
    total_parents=0

    #1= pieces on board eval 2=number of ally moves eval 3= number of enemy moves eval 4=ally-enemy moves evaul
    def minimax(board,depth,depth_limit,eval):
        best_board = None
        best_move = None
        #print(depth,"depth level")
        current_depth=depth+1


        if current_depth==depth_limit:
            Minimax_tracker.total_cut_offs+=1
            return Minimax_tracker.board_check(board,eval)


        if board.turn==0:
            Minimax_tracker.total_branches+=4
            best_score=float('-inf')
            piece,move,turn=board.first_two_moves_picker(0)
            best_board=deepcopy(board)
            best_board.computer_move(str(piece.x)+str(piece.y), move)
            best_move=str(piece.x)+str(piece.y), move

        if board.turn==1:
            Minimax_tracker.total_branches+=4
            best_score=float('inf')
            piece,move,turn=board.first_two_moves_picker(0)
            best_board=deepcopy(board)
            best_board.computer_move(str(piece.x)+str(piece.y), move)
            best_move=str(piece.x)+str(piece.y), move


        # After first 2 pieces have been removed
        elif board.turn%2==1 and board.turn != 1:
            best_score = float('inf')
            bboard,score,move=Minimax_tracker.board_check(board,eval)
            if score == float('inf') or score == float('-inf') :
                print("bummmmmmmmmmmm")

                return bboard,score,move

            #print('white turn')
            #print(board.turn)
            for piece,move in board.expand_white_moves():
                Minimax_tracker.total_branches+=1

                #print(piece.x,piece.y,move[1],"Depth",current_depth)

                best_board = deepcopy(board)
                best_board.computer_move(str(piece.x)+str(piece.y), move[1])
                minimax_board,minimax_returned_score,minimax_move = Minimax_tracker.minimax(best_board,current_depth,depth_limit,eval)
                #print("minmax: ",minimax_returned_score )
                if minimax_returned_score <= best_score:
                    best_move = str(piece.x)+str(piece.y), move[1]
                    best_score = minimax_returned_score

        elif board.turn%2==0 and board.turn != 0:
            #print('black turn')
            #print(board.turn)
            best_score = float('-inf')
            bboard,score,move=Minimax_tracker.board_check(board,eval)
            if score == float('inf') or score == float('-inf') :
                print("yummmmmmmmmmmm")
                return bboard,score,move


            #print("Depth:::::::::::", current_depth)
            for piece,move in board.expand_black_moves():
                Minimax_tracker.total_branches+=1
                #print(piece.x,piece.y,move[1],"Depth",current_depth)
                best_board=deepcopy(board)
                best_board.computer_move(str(piece.x)+str(piece.y), move[1])
                minimax_board,minimax_returned_score,minimax_move = Minimax_tracker.minimax(best_board,current_depth,depth_limit,eval)
                if minimax_returned_score >= best_score:
                    best_move=str(piece.x)+str(piece.y), move[1]
                    best_score=minimax_returned_score
            #print("Depth]]]]]]]]]]]]]]]]", current_depth)


        Minimax_tracker.total_parents+=1
        return best_board, best_score, best_move
    @classmethod
    def board_check(self,board,eval):
        Minimax_tracker.total_evauls+=1
        return board,board.utility(eval), None

