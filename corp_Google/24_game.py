import itertools

class Solution(object):
    def judgePoint24(self, nums):
        ops = list(itertools.product([add, sub, mul, div], repeat = 3))
        
        for num in set(itertools.permutations(nums)):
            for op in ops:
                # (Z op (Y op (W op X)))
                res = op[0](num[0], num[1])
                res = op[1](num[2], res)
                res = op[2](num[3], res)
                if 23.99 < res < 24.01:
                    return True

                # ((W op X) op (Y op Z))
                res1 = op[0](num[0], num[1])
                res2 = op[1](num[2], num[3])
                res = op[2](res1, res2)
                if 23.99 < res < 24.01:
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
