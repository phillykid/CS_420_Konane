from copy import deepcopy


# Remember the notation argmax a which is an element of S f(a)
# For this implementation we need to compute the element a of set S that has the maximum value of f(a)
# In other words, for this method we need to compute the action a from the list of actions that has
# the minimum utility value


def alpha_beta_pruning(board_state, depth, depth_limit):
    #print("OFFICIAL DEPTH LIMIT: " + str(depth_limit))
    action = None
    # As soon as this starts we are going down to depth 1
    # Initially alpa and beta are -infinity and +infinity respectively
    if board_state.turn % 2 == 0:
        #print("Dealing with black first")
        # This means we are starting with a black move
        v, action = max_value(board_state, depth + 1, depth_limit, float('-inf'), float('inf'))
    elif board_state.turn % 2 == 1:
        #print("Going to white first")
        # This means that we are starting with a white move
        v, action = min_value(board_state, depth + 1, depth_limit, float('-inf'), float('inf'))
    # We have to return the action that has the same value of v
    #print(board_state.turn)
    return action


# If its checking max_value then we are looking at black
def max_value(board_state, depth, depth_limit, alpha, beta):
    # Our primary action would only be None if we hit a leaf node
    primary_action = None

    # First check if black is in a terminal state
    #print("DEPTH AT THIS POINT: " + str(depth))
    resulting_state = deepcopy(board_state)
    terminal_check = resulting_state.terminal_state(resulting_state.BLACK_ICON)
    if terminal_check or depth > depth_limit:
        return resulting_state.utility(), primary_action

    # Otherwise run through the algorithm
    v = float('-inf')
    old_v = v
    for p, a in board_state.expand_black_moves():
        # Compute the resulting board state after applying this possible move
        resulting_state.computer_move(str(p.x) + str(p.y), a[1])
        #print("RESULTING STATE FROM MAX: ")
        #print(resulting_state)

        # Each max_value will return an action associated with its chosen v
        possible_v, result_action = min_value(resulting_state, depth + 1, depth_limit, alpha, beta)
        #print("RESULTING ACTION FOR MAX AT DEPTH: " + str(depth) + str(result_action))

        # Go back to the original board
        resulting_state = deepcopy(board_state)

        #print("CURRENT V: " + str(v) + " v.s POSSIBLE V: " + str(possible_v))
        v = max(v, possible_v)
        # Detect if v was updated this round, if so update primary action
        if not old_v == v:
            primary_action = str(p.x)+str(p.y), a[1]
            old_v = v
        if v >= beta:
            return v, primary_action
        alpha = max(alpha, v)
    return v, primary_action


# If its checking min_value then we are looking at white
def min_value(board_state, depth, depth_limit, alpha, beta):
    # Our primary action would only be None if we hit a leaf node
    primary_action = None

    # First check if White is in a terminal position
    #print("DEPTH AT THIS POINT: " + str(depth))
    resulting_state = deepcopy(board_state)
    terminal_check = resulting_state.terminal_state(resulting_state.WHITE_ICON)
    if terminal_check or depth > depth_limit:
        return resulting_state.utility(), primary_action

    # Otherwise run the algorithm
    v = float('inf')
    old_v = v
    for p, a in board_state.expand_white_moves():
        # Compute the resulting board state after applying the possible move
        resulting_state.computer_move(str(p.x) + str(p.y), a[1])
        #print("RESULTING STATE FROM MIN: ")
        #print(resulting_state)

        possible_v, result_action = max_value(resulting_state, depth + 1, depth_limit, alpha, beta)
        #print("RESULTING ACTION FOR MIN AT DEPTH: " + str(depth) + str(result_action))
        #print("CURRENT V: " + str(v) + " v.s POSSIBLE V: " + str(possible_v))

        # Go back to the original board
        resulting_state = deepcopy(board_state)
        v = min(v, possible_v)
        # Detect if v has changed or not
        if not old_v == v:
            # If v changed then we gotta change the primary action to the one attached to this v
            primary_action = str(p.x)+str(p.y), a[1]
            old_v = v
        if v <= alpha:
            return v, primary_action
        beta = min(beta, v)
    return v, primary_action
