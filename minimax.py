from copy import deepcopy

def minimax(board,depth,depth_limit):
    best_board=None
    best_move=None
    print(depth,"depth level")
    current_depth=depth+1

    if current_depth==depth_limit:
        return board,board.evaluate_board_desiarbility(),None

    if board.turn==0:
        best_score=float('-inf')
        piece,move,turn=board.first_two_moves_picker(0)
        best_board=deepcopy(board)
        best_board.move_piece_computer(str(piece.x)+str(piece.y),move)
        best_move=str(piece.x)+str(piece.y),move

    if board.turn==1:
        best_score=float('inf')
        piece,move,turn=board.first_two_moves_picker(0)
        best_board=deepcopy(board)
        best_board.move_piece_computer(str(piece.x)+str(piece.y),move)
        best_move=str(piece.x)+str(piece.y),move



    elif board.turn%2==1 and board.turn != 1:
        best_score=float('inf')
        print('white turn')
        print(board.turn)
        for piece,move in board.expand_white_moves():
            best_board=deepcopy(board)
            best_board.move_piece_computer(str(piece.x)+str(piece.y),move[1])
            minimax_board,minimax_returned_score,minimax_move = minimax(best_board,current_depth,depth_limit)
            print("minmax: ",minimax_returned_score )
            if minimax_returned_score < best_score:
                best_move=str(piece.x)+str(piece.y),move[1]
                best_score=minimax_returned_score

    else:
        print('black turn')
        best_score=float('-inf')

        for piece,move in board.expand_black_moves():
            best_board=deepcopy(board)
            best_board.move_piece_computer(str(piece.x)+str(piece.y),move[1])
            minimax_board,minimax_returned_score,minimax_move= minimax(best_board,current_depth,depth_limit)
            if minimax_returned_score > best_score:
                best_move=str(piece.x)+str(piece.y),move[1]
                best_score=minimax_returned_score

    return best_board,best_score,best_move

