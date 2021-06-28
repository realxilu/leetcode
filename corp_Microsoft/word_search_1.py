class Solution:
    def exist(self, board, word):
        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True

        return False

    # indices i, j are useful helper params for graph problems
    # start the exploration at position (i, j)
    def dfs(self, board, i, j, word):
        # all the characters are checked
        if len(word) == 0:
            return True

        # 1) out of bound
        # 2) if current character of the word is not found, then the word can't be found
        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or word[0] != board[i][j]:
            return False

        # first character is found, check the remaining part
        saved_val = board[i][j]
        # mark as visisted
        board[i][j] = '#'
        
        # check whether can find 'word' along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or \
              self.dfs(board, i - 1, j, word[1:]) or \
              self.dfs(board, i, j + 1, word[1:]) or \
              self.dfs(board, i, j - 1, word[1:])
        
        # don't forget to recover the position
        board[i][j] = saved_val

        return res

# [KEY][BACKTRACK] 1) run dfs on every cell
