class Solution(object):
    def decodeString(self, s):
        stack, cur_num, cur_string = [], 0, ''
        
        for c in s:
            if c == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                # reset current string and the current number
                cur_string = ''
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + num * cur_string
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c.isalpha():
                cur_string += c
        
        return cur_string

# [KEY] use stack and reset after append
