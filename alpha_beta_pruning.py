from copy import deepcopy


# For this method we need to compute the action a from the list of actions that has
# the minimum utility value

def alpha_beta_pruning(board_state, depth, depth_limit):
    action = None
    # In case we are black
    if board_state.turn == 0:
        piece, move, turn = board_state.first_two_moves_picker(0)
        action = str(piece.x)+str(piece.y), move
        print("We are black!")
        return action
    # In case we are white
    if board_state.turn == 1:
        piece, move, turn = board_state.first_two_moves_picker(0)
        action = str(piece.x)+str(piece.y), move
        return action
    # As soon as this starts we are going down to depth 1
    # Initially alpha and beta are -infinity and +infinity respectively
    if board_state.turn % 2 == 0:
        # This means we are starting with a black move
        v, action = max_value(board_state, depth + 1, depth_limit, float('-inf'), float('inf'))
    elif board_state.turn % 2 == 1:
        # This means that we are starting with a white move
        v, action = min_value(board_state, depth + 1, depth_limit, float('-inf'), float('inf'))

    # We have to return the action that has the same value of v
    return action


# If its checking max_value then we are looking at black

def max_value(board_state, depth, depth_limit, alpha, beta):
    # Our primary action would only be None if we hit a leaf node
    primary_action = None

    # First check if black is in a terminal state
    resulting_state = deepcopy(board_state)
    terminal_check = resulting_state.terminal_state(resulting_state.BLACK_ICON)
    if terminal_check or depth > depth_limit:
        return resulting_state.utility(2), primary_action
    # Otherwise run through the algorithm
    v = float('-inf')
    old_v = v
    for p, a in board_state.expand_black_moves():
        # Compute the resulting board state after applying this possible move
        resulting_state.computer_move(str(p.x) + str(p.y), a[1])
        # Each max_value will return an action associated with its chosen v
        possible_v, result_action = min_value(resulting_state, depth + 1, depth_limit, alpha, beta)
        # Go back to the original board
        resulting_state = deepcopy(board_state)
        v = max(v, possible_v)
        # Detect if v was updated this round, if so update primary action
        if not old_v == v:
            primary_action = str(p.x) + str(p.y), a[1]
            old_v = v
        if v >= beta:
            return v, primary_action
        alpha = max(alpha, v)
    return v, primary_action


# If its checking min_value then we are looking at white

def min_value(board_state, depth, depth_limit, alpha, beta):
    # Our primary action would only be None if we hit a leaf node
    primary_action = None

    resulting_state = deepcopy(board_state)
    terminal_check = resulting_state.terminal_state(resulting_state.WHITE_ICON)
    if terminal_check or depth > depth_limit:
        return resulting_state.utility(2), primary_action
    # Otherwise run the algorithm
    v = float('inf')
    old_v = v
    for p, a in board_state.expand_white_moves():
        # Compute the resulting board state after applying the possible move
        resulting_state.computer_move(str(p.x) + str(p.y), a[1])
        possible_v, result_action = max_value(resulting_state, depth + 1, depth_limit, alpha, beta)
        # Go back to the original board
        resulting_state = deepcopy(board_state)
        v = min(v, possible_v)
        # Detect if v has changed or not
        if not old_v == v:
            # If v changed then we gotta change the primary action to the one attached to this v
            primary_action = str(p.x) + str(p.y), a[1]
            old_v = v
        if v <= alpha:
            return v, primary_action
        beta = min(beta, v)
    return v, primary_action
