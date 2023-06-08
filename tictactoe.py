"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0
    for line in board:
        for state in line:
            if state == X:
                num_x += 1
            elif state == O:
                num_o += 1
    if num_x == num_o:
        return X
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i=0
    j=0
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acts.add((i,j))
    return acts
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0], action[1]] != EMPTY:
        raise Exception("Invalid action!!!")
    
    new_board = copy.deepcopy(board)
    board[action[0], action[1]] == player(board)
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # case (0, 0) 
    if board[0][0] != EMPTY:
        symbol = board[0][0]
        if board[0][1] == board[0][2] == board[0][0] or board[1][0] == board[2][0] == board[0][0] or board[1][1] == board[2][2] == board[0][0]:
            return symbol
    # case (0, 1)
    if board[0][1] != EMPTY:
        symbol = board[0][1]
        if board[1][1] == board[2][1] == board[0][1]:
            return symbol
    # case (0, 2)
    if board[0][2] != EMPTY:
        symbol = board[0][2]
        if board[1][2] == board[2][2] == board[0][2] or board[2][0] == board[1][1] == board[0][2]:
            return symbol
    # case (1, 0)
    if board[1][0] != EMPTY:
        symbol = board[1][0]
        if board[1][1] == board[1][2] == board[1][0]:
            return symbol
    # case (2, 0)
    if board[2][0] != EMPTY:
        symbol = board[2][0]
        if board[2][1] == board[2][2] == board[2][0]:
            return symbol
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win:
        return True
    else:
        for line in board:
            for state in line:
                if state == EMPTY:
                    return False
        return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1 
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if ternimal(board):
        return utility(board)
    # who play?
    if player(board) == O:
        acts = actions(board)
        for act in acts:  
            minimax(result(board, act))
    if player(board) == X:
        acts = actions(board)
        for act in acts:  
            minimax(result(board, act))
    raise NotImplementedError
