class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        
        while j >= 0 and i <= len(matrix) - 1:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1

        return False

# [KEY] observe the given property of the matrix
# i = row index; j = col index
# start from top right and move row index down and col index to the left