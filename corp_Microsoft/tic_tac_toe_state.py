#  When turns is 1, X moved.When turns is 0, O moved.rows stores the number of X or O in each row.
#  cols stores the number of X or O in each column.
#  diag stores the number of X or O in diagonal.
#  antidiag stores the number of X or O in antidiagonal.
#  When any of the value gets to 3, it means X wins.
#  When any of the value gets to - 3, it means O wins.

#  When X wins, O cannot move anymore, so turns must be 1.
#  When O wins, X cannot move anymore, so turns must be 0.
#  Finally, when we return, turns must be either 0 or 1, and X and O cannot win at same time.


class Solution:
    def validTicTacToe(self, board):
        turns, diag, antidiag = 0, 0, 0
        rows, cols = [0, 0, 0], [0, 0, 0]
        x_win, o_win = False, False

        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    turns += 1
                    rows[i] += 1
                    cols[j] += 1
                    if i == j:
                        diag += 1
                    if i + j == 2:
                        antidiag += 1
                elif board[i][j] == 'O':
                    turns -= 1
                    rows[i] -= 1
                    cols[j] -= 1
                    if i == j:
                        diag -= 1
                    if i + j == 2:
                        antidiag -= 1

        x_win = rows[0] == 3 or rows[1] == 3 or rows[2] == 3 or \
                cols[0] == 3 or cols[1] == 3 or cols[2] == 3 or \
                diag == 3 or antidiag == 3

        o_win = rows[0] == -3 or rows[1] == -3 or rows[2] == -3 or \
                cols[0] == -3 or cols[1] == -3 or cols[2] == -3 or \
                diag == -3 or antidiag == -3

        if x_win and turns == 0 or o_win and turns == 1:
            return False

        return (turns == 0 or turns == 1) and (not x_win or not o_win)
