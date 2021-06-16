class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1, hold2 = float('-inf'), float('-inf')
        release1, release2 = 0, 0

        for p in prices:
            release2 = max(release2, hold2 + p)
            hold2 = max(hold2, release1 - p)
            release1 = max(release1, hold1 + p)
            hold1 = max(hold1, - p)

        return release2
