from copy import deepcopy


class Minimax_tracker():
    total_branches = 0  # The total amount of moves in the game possible
    total_cut_offs = 0  # The number of times the depth limit is reached
    total_evals = 0  # The number of times the board is evaluated
    total_non_leafs = 0  # The number of posistions we branch off from used to calculate avg branching factor

    # Eval=utility function used: 1=pieces on board eval 2=number of ally moves eval 3= number of enemy moves eval
    # 4=ally-enemy moves eval
    def minimax(board, depth, depth_limit, eval):
        best_board = None
        best_move = None
        current_depth = depth + 1

        if current_depth == depth_limit:
            Minimax_tracker.total_cut_offs += 1
            return Minimax_tracker.board_check(board, eval)

        if board.turn == 0:
            Minimax_tracker.total_branches += 4
            best_score = float('-inf')
            piece, move, turn = board.first_two_moves_picker(0)
            best_board = deepcopy(board)
            best_board.computer_move(str(piece.x) + str(piece.y), move)
            best_move = str(piece.x) + str(piece.y), move
            return best_board, best_score, best_move

        if board.turn == 1:
            Minimax_tracker.total_branches += 4
            best_score = float('inf')
            piece, move, turn = board.first_two_moves_picker(0)
            best_board = deepcopy(board)
            best_board.computer_move(str(piece.x) + str(piece.y), move)
            best_move = str(piece.x) + str(piece.y), move
            return best_board, best_score, best_move

        # After first 2 pieces have been removed

        # Whites Turn
        elif board.turn % 2 == 1 and board.turn != 1:
            best_score = float('inf')
            bboard, score, move = Minimax_tracker.board_check(board, eval)
            if score == 100000000000 or score == -100000000000:  # Checks for terminal state
                return bboard, score, move

            for piece, move in board.expand_white_moves():
                Minimax_tracker.total_branches += 1

                best_board = deepcopy(board)
                best_board.computer_move(str(piece.x) + str(piece.y), move[1])
                minimax_board, minimax_returned_score, minimax_move = Minimax_tracker.minimax(best_board, current_depth,
                                                                                              depth_limit, eval)
                if minimax_returned_score < best_score:
                    best_move = str(piece.x) + str(piece.y), move[1]
                    best_score = minimax_returned_score

        # Blacks Turn
        elif board.turn % 2 == 0 and board.turn != 0:
            best_score = float('-inf')
            bboard, score, move = Minimax_tracker.board_check(board, eval)
            if score == 100000000000 or score == -100000000000:  # Checks for terminal state
                return bboard, score, move

            for piece, move in board.expand_black_moves():
                Minimax_tracker.total_branches += 1
                # print(piece.x,piece.y,move[1],"Depth",current_depth)
                best_board = deepcopy(board)
                best_board.computer_move(str(piece.x) + str(piece.y), move[1])
                minimax_board, minimax_returned_score, minimax_move = Minimax_tracker.minimax(best_board, current_depth,
                                                                                              depth_limit, eval)
                if minimax_returned_score > best_score:
                    best_move = str(piece.x) + str(piece.y), move[1]
                    best_score = minimax_returned_score

        Minimax_tracker.total_non_leafs += 1
        return best_board, best_score, best_move

    # Checks the eval score of the given board
    @classmethod
    def board_check(self, board, eval):
        Minimax_tracker.total_evals += 1
        return board, board.utility(eval), None
