class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        limit = len(candyType) // 2
        s = set(candyType)
        s_len = len(s)

        return s_len if s_len < limit else limit
