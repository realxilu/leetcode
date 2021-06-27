class Solution(object):
    def addStrings(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []

        while len(num1) or len(num2):
            n1 = ord(num1.pop()) - ord('0') if len(num1) else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) else 0

            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10

        if carry:
            res.append(carry)

        # 'join' only works for strings in arrays, 'i' needs to be converted to string first before joining
        return ''.join([str(i) for i in res])[::-1]
