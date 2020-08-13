class Solution:
    def hamming_distance(self, x, y):
        return bin(x ^ y).count('1')
