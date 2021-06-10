class Solution:
    def convertToTitle(self, num: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        res = []

        while num:
            res.append(capitals[(num - 1) % 26])
            num = (num - 1) // 26

        return ''.join(res)[::-1]

# ord: convert alphabet to number
# chr: convert number to alphabet
