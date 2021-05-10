# let boxRow = 3 * parseInt(i / 3) + parseInt(j / 3)
# let boxCol = 3 * (i % 3) + j % 3

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for i in range(n):
            row_set, col_set, box_set = set(), set(), set()
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

                # [KEY] index transformation is paramount to this problem
                box_i = 3 * (i // 3) + (j // 3)
                box_j = 3 * (i % 3) + (j % 3)

                if board[box_i][box_j] != '.':
                    if board[box_i][box_j] in box_set:
                        return False
                    box_set.add(board[box_i][box_j])

        return True
