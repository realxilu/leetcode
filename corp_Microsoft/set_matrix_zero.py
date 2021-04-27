class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        # if the 1st col has 0 col0 will be set to 0
        col0 = 1

        # scan through row (up -> down)
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            # scan through col (left -> right)
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # why visit in reverse order?
        for i in reversed(range(m)):
            for j in reversed(range(1, n)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            # [!!] BE CAREFUL ABOUT INDENTATION [!!]
            if col0 == 0:
                matrix[i][0] = 0