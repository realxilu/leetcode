class Solution:
    def spiralOrder(self, matrix):
        row_i, row_j = 0, len(matrix) - 1
        col_i, col_j = 0, len(matrix[0]) - 1
        res = []

        while True:
            for x in range(col_i, col_j + 1):
                res.append(matrix[row_i][x])
            row_i += 1
            if row_i > row_j:
                break

            for x in range(row_i, row_j + 1):
                res.append(matrix[x][col_j])
            col_j -= 1
            if col_i > col_j:
                break

            for x in range(col_j, col_i - 1, -1):
                res.append(matrix[row_j][x])
            row_j -= 1
            if row_i > row_j:
                break

            for x in range(row_j, row_i - 1, -1):
                res.append(matrix[x][col_i])
            col_i += 1
            if col_i > col_j:
                break

        return res
