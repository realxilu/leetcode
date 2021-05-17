# [BINARY SEARCH]
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1

        while start <= end:
            mid = (start + end) // 2

            if target == matrix[mid // n][mid % n]:
                return True

            if target > matrix[mid // n][mid % n]:
                start = mid + 1
            else:
                end = mid - 1

        return False

# [KEY] index manipulation. 
# Work on linear array then convert 'mid' to the appropriate positions in the matrix
# row = mid // n
# col = mid % n
