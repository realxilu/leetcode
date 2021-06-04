class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            # universal case: we need to know if the previous digit is bigger than current, if so remove the prev. For this we need stack. 
            while stack and stack[-1] > c and k:
                stack.pop()
                k -= 1

            # case: '0000000045' in this case we don't ever want to push leading 0s
            if stack or c != '0':
                stack.append(c)

        # case: '1234567' in the case of digits are strickly ascending, we never popped anything in the first for loop, so pop k of them as required
        while stack and k:
            stack.pop()
            k -= 1

        return ''.join(stack) if stack else '0'

# [KEY][STACK] if we need to have information for something happened before the current element, we need stack to retain such info
# If the digit is in front of the current one and it is bigger, then we pop it. 
