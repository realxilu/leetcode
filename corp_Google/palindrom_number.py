class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        save, num = x, 0
        while x:
            num = 10 * num + x % 10
            x //= 10

        return save == num
