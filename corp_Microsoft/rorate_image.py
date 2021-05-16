class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        if m == 0 or m == 1:
            return matrix

        self._reverse(matrix)

        for i in range(m):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def _reverse(self, arr):
        i, j = 0, len(arr) - 1

        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

# [KEY] obserave mathmatical property
