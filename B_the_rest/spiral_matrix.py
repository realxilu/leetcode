class Solution:
    def spiral_order(self, matrix):
        if len(matrix) == 0:
            return []

        row_start, col_start = 0, 0
        row_end, col_end = len(matrix) - 1, len(matrix[0]) - 1
        res = []

        while True:
            for x in range(col_start, col_end + 1):
                res.append(matrix[row_start][x])
            row_start += 1
            if row_start > row_end:
                break

            for x in range(row_start, row_end + 1):
                res.append(matrix[x][col_end])
            col_end -= 1
            if col_start > col_end:
                break

            for x in range(col_end, col_start - 1, -1):
                res.append(matrix[row_end][x])
            row_end -= 1
            if row_start > row_end:
                break

            for x in range(row_end, row_start - 1, -1):
                res.append(matrix[x][col_start])
            col_start += 1
            if col_start > col_end:
                break

        return res
