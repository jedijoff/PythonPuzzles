#!/usr/bin/env python3

def get_tic_tac_toe_winner(board):
    """
    Function returns the winner of a Tic Tac Toe game.

    :param board: a list of lists representing the
                  Tic Tac Toe board.
    :return: the winner of the game.
    """
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


# Example function calls:
print(get_tic_tac_toe_winner([['X', 'O', 'X'],
                              ['O', 'O', 'X'],
                              ['X', 'X', 'O']]))
print(get_tic_tac_toe_winner([['X', 'O', 'X'],
                              ['O', 'O', 'X'],
                              ['X', 'X', 'X']]))
print(get_tic_tac_toe_winner([['O', 'O', 'X'],
                              ['X', 'O', 'O'],
                              ['X', 'X', 'O']]))
print(get_tic_tac_toe_winner([['O', 'O', 'X'],
                              ['X', 'X', 'X'],
                              ['O', 'X', 'O']]))


