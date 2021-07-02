class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp = 0
            while num:
                tmp += num % 10
                num //= 10
            num = tmp  # reassign tmp back to num

        return num
