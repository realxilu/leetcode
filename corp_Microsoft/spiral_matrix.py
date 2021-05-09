# [KEY] [innovative] maintain corner indices that record the outmost boundary of the 'box'
# [tip] while true + break
# note that row_i, row_j, col_i and col_j are indices not the length
# I also found that clear concise and consistent naming has simplied this problem quite a bit
class Solution:
    def spiralOrder(self, matrix):
        row_i, row_j = 0, len(matrix) - 1
        col_i, col_j = 0, len(matrix[0]) - 1
        res = []

        while True:
            # note row_i, row_j are indices
            # the 2nd param for the 'range' function is length, thus do '+ 1' to translate to length
            for j in range(col_i, col_j + 1):
                res.append(matrix[row_i][j])
            # when finishing traveral from left to right, shrink the top row
            row_i += 1
            # any corner index violates the boundary constraint, exit immediately
            if row_i > row_j:
                break

            for i in range(row_i, row_j + 1):
                res.append(matrix[i][col_j])
            col_j -= 1
            if col_i > col_j:
                break

            # note 1) going backward 2) range(start, stop[, step]) 3) interval is -1 here
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
