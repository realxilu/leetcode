class TicTacToe(object):

    def __init__(self, n):
        self.row, self.col, self.diag, self.anti_diag, self.n = [
            0] * n, [0] * n, 0, 0, n

    def move(self, row, col, player):
        offset = player * 2 - 3
        self.row[row] += offset
        self.col[col] += offset

        if row == col:
            self.diag += offset

        if row + col == self.n - 1:
            self.anti_diag += offset

        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2

        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1

        return 0
