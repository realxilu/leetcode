import heapq
# overall O(n*logk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        # O(n)
        for x in nums:
            dic[x] = dic.get(x, 0) + 1

        heap = [] # no need to heapify
        # O(n*logk)
        for key, val in dic.items():
            heapq.heappush(heap, (key, val))

        # 'key' defines what we use for sort, here we use 'val' in (key, val) as an ordering param
        return [key for key, _ in heapq.nlargest(k, heap, key=lambda x: x[1])]

# [KEY] heapq syntax and lambda expression. The problem is not hard at all conceptually.