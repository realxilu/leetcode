class Solution:
    def hammingWeight(self, n):
        c = 0
        while n:
            n &= n - 1
            c += 1
        
        return c

# Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. 
# n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1

    def hammingWeight(self, n):
        return bin(n).count('1')
