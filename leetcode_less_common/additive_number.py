# Note: there is *no* restriction that the first number should be shorter or smaller than the second number
class Solution:
    # KEY: find the first two substrings and then check the remaining
    def is_additive_number(self, num):
        n = len(num)
        # Exhaust all possibilities of the first two substrings
        # 'i' is the beginning index of the second number
        for i in range(1, n // 2 + 1):
            if num[0] == '0' and i >= 2:
                return False
            # 'j' is the beginning index of the remaining numbers
            for j in range(i + 1, min(n - i, (n + i) // 2) + 1):
                if num[i] == '0' and j - i >= 2:
                    '''
                        If the current substring starts with 0, then no need to consider the substring further.
                        But the string could still be valid (as trailing 0) so don't return false
                    '''
                    break

                num1 = num[:i]
                num2 = num[i:j]
                rest = num[j:]

                if self.is_valid(num1, num2, rest):
                    return True

        return False

    def is_valid(self, num1, num2, rest):
        if rest == '':
            return True

        sum_ = str(int(num1) + int(num2))

        if rest.startswith(sum_):
            return self.is_valid(num2, sum_, rest[len(sum_):])

        return False
