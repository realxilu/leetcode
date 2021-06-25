class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        # [TRICK] add a '+' at the end
        s = s.strip() + '+'
        stack, sign, tmp = [], '+', 0

        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                tmp = 10 * tmp + int(c)
            else:
                if sign == '+':
                    stack.append(tmp)
                if sign == '-':
                    stack.append(-tmp)
                if sign == '*':
                    stack.append(stack.pop() * tmp)
                if sign == '/':
                    top = stack.pop()
                    # top // tmp will floor the number which is problematic for negative divisions
                    if top // tmp < 0 and top % tmp != 0:
                        # if the divison is negative and has a remainder (ie -1.125), then move the number to the right by 1 unit (-1)
                        stack.append(top // tmp + 1)
                    else:
                        stack.append(top // tmp)
                # reset sign and tmp
                sign, tmp = c, 0

        return sum(stack)

# [KEY] when we hit the current sign, we do calculation based on the previous sign
# 1 + 3 - 4 +5: when we hit '-', we are then doing calculation for '1 + 3' and the sign we are looking at is '+' 
# In the end we have [1, 3, -4, 5] in the stack and then sum them all up and return