class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        # if the 1st col has 0, col0 will be set to 0
        row0, col0 = False, False

        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True

        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0:
            for j in range(n):
                matrix[0][j] = 0

        if col0:
            for i in range(m):
                matrix[i][0] = 0

# This is my own solution. More intuitive than the most upvoted solution found on leetcode.com.
# [KEY] Use the first row and col to mark if the row or col should be all zero based on matrix[i][j]
# The first row and col are speical though, they needed special flags to mark their status.


