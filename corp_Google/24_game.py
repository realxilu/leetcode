import itertools

class Solution(object):
    def judgePoint24(self, nums):
        Ops = list(itertools.product([add, sub, mul, div], repeat = 3))
        
        for num in set(itertools.permutations(nums)):
            for op in Ops:
                # (Z op (Y op (W op X)))
                result = op[0](num[0], num[1])
                result = op[1](num[2], result)
                result = op[2](num[3], result)
                if 23.99 < result < 24.01:
                    return True

                # ((W op X) op (Y op Z))
                result1 = op[0](num[0], num[1])
                result2 = op[1](num[2], num[3])
                result = op[2](result1, result2)
                if 23.99 < result < 24.01:
                    return True
        
        return False

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return 0 # this is accpetable since 0 would yield wrong answer anyways
    
    return a / float(b)

# [KEY] itertool
# Learn backtracking method to handle pesky interviewers
