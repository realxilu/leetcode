class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1

        while start <= end:
            mid = (start + end) // 2

            if matrix[mid // n][mid % n] == target:
                return True

            if matrix[mid // n][mid % n] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False

# [BINARY SEARCH]
# [KEY] index conversion
