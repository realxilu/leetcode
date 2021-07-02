# KEY: derive the general term formula for the algebric sequence
class Solution:
    def consecutive_numbers_sum(self, n):
        res, m = 0, 1

        while True:
            xm = n - m * (m - 1) / 2

            # m (numbers of terms) can never be zero
            if xm <= 0:
                break

            # check if x (the initial term of the sequence is an integer)
            if xm % m == 0:
                res += 1

            m += 1

        return res
