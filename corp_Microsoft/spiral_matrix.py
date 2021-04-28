# [KEY] maintain corner indices that record the outmost boundary of the 'box'
# [tip] while true + break
# note that row_i, row_j, col_i and col_j are indices not the length
class Solution:
    def spiralOrder(self, matrix):
        row_i, row_j = 0, len(matrix) - 1
        col_i, col_j = 0, len(matrix[0]) - 1
        res = []

        while True:
            # note col_j + 1
            for j in range(col_i, col_j + 1):
                res.append(matrix[row_i][j])
            row_i += 1
            if row_i > row_j:
                break

            for i in range(row_i, row_j + 1):
                res.append(matrix[i][col_j])
            col_j -= 1
            if col_i > col_j:
                break

            # note the last arg in 'range' is -1
            for j in range(col_j, col_i - 1, -1):
                res.append(matrix[row_j][j])
            row_j -= 1
            if row_i > row_j:
                break

            for i in range(row_j, row_i - 1, -1):
                res.append(matrix[i][col_i])
            col_i += 1
            if col_i > col_j:
                break

        return res

