class Solution:
    def generateMatrix(self, n):
        row_i, row_j = 0, n - 1
        col_i, col_j = 0, n - 1
        res = [[0 for i in range(n)] for j in range(n)]

        count = 1
        while True:
            for j in range(col_i, col_j + 1):
                res[row_i][j] = count
                count += 1
            row_i += 1
            if row_i > row_j:
                break

            for i in range(row_i, row_j + 1):
                res[i][col_j] = count
                count += 1
            col_j -= 1
            if col_i > col_j:
                break

            for j in range(col_j, col_i - 1, -1):
                res[row_j][j] = count
                count += 1
            row_j -= 1
            if row_i > row_j:
                break

            for i in range(row_j, row_i - 1, -1):
                res[i][col_i] = count
                count += 1
            col_i += 1
            if col_i > col_j:
                break

        return res

# [SIMILAR] to corp_Microsoft\spiral_matrix.py
# use 'range(col_j, col_i - 1, -1)' instead of reversed(range, col_i, col_j + 1)
