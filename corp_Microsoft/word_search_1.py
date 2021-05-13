# TODO 
class Solution:
    def exist(self, board, word):
        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True

        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        # all the characters are checked
        if len(word) == 0:
            return True

        # 1) out of bound
        # 2) word not found
        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or word[0] != board[i][j]:
            return False

        # first character is found, check the remaining part
        tmp = board[i][j]
         # avoid visit agian
        board[i][j] = "#"
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
            or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp

        return res

# [KEY] 1) apply dfs on each cell