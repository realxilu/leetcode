class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self._reverse(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def _reverse(self, a):
        i, j = 0, len(a) - 1
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
