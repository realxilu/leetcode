class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([]) # list of lists

        for x in nums:
            _len = len(res) # [KEY] record the current res length BEFORE making modifications
            for i in range(_len):
                # res is a list of list [[1, 2, 3], [3, 4], [7, 2, 3]]
                # [PY] res[i].copy() of above will produce [[1, 2, 3], [3, 4], [7, 2, 3], [1, 2, 3], [3, 4], [7, 2, 3]]
                res.append(res[i].copy())
            for i in range(_len):
                # append the new element to the list
                # for example if x = 0, then [[1, 2, 3, 0], [3, 4, 0], [7, 2, 3, 0], [1, 2, 3], [3, 4], [7, 2, 3]]
                res[i].append(x)

        return res

# an example of the copy function
# a = [1, 2, 3]
# b = a.copy() # array copy but not deep copy
# # modify the original 'a' list
# a = [4 ,5, 6]
# print(a) # [4, 5, 6]
# print(b) # [1, 2, 3]
