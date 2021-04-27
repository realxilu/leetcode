from heapq import *
# [PRIORITY-QUEUE]

def connect_rope(arr):
    _sum = 0
    heapify(arr)
    while arr:
        try:
            a = heappop(arr)
            b = heappop(arr)
            c = a + b
            _sum += c
            heappush(arr, c)
        except:
            pass

    return _sum

# [MAIN]
l = connect_rope([8, 4, 6, 12]) # 58
# l = connect_rope([20, 4, 8, 2]) # 54
# l = connect_rope([1, 2, 5, 10, 35, 89]) # 224
# l = connect_rope([2, 2, 3, 3])  # 20
print(l)
