class Solution:
    def findClosestElements(self, A, k, x):
        i, j = 0, len(A) - k
        
        while i < j:
            mid = (i + j) // 2
            if x - A[mid] > A[mid + k] - x:
                i = mid + 1
            else:
                j = mid

        return A[i:i + k] # [start index = i, stop index = i + k - 1]

# [KEY] the key is to provide analysis
# case 1: x - A[mid] < A[mid + k] - x, need to move window go left
# -------x----A[mid]-----------------A[mid + k]----------

# case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
# -------A[mid]----x-----------------A[mid + k]----------

# case 3: x - A[mid] > A[mid + k] - x, need to move window go right
# -------A[mid]------------------x---A[mid + k]----------

# case 4: x - A[mid] > A[mid + k] - x, need to move window go right
# -------A[mid]---------------------A[mid + k]----x------

# If x - A[mid] > A[mid + k] - x,
# it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
# and we have mid smaller than the right i.
# So assign i = mid + 1.
