class TicTacToe:
    def __init__(self, n):
        self.rows, self.cols = [0] * n, [0] * n
        self.diag, self.antidiag = 0, 0
        self.n = n

    # the player places stone on grid (i, j)
    def move(self, i, j, player):
        n = self.n

        add_one = 1 if player == 1 else -1

        self.rows[i] += add_one

        self.cols[j] += add_one

        if i == j:
            self.diag += add_one

        if i + j == n - 1:  # anti-diagnal
            self.antidiag = add_one

        if abs(self.rows[i]) == n or abs(self.cols[j]) == n or abs(self.diag) == n or abs(self.antidiag) == n:
            return player

        return 0
