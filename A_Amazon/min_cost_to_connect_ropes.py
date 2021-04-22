from heapq import *
# [PRIORITY QUEUE]

def connect_rope(arr):
    if not arr:
        return 0

    sum_ = 0
    heapify(arr)
    while arr:
        try:
            a = heappop(arr)
            b = heappop(arr)
            c = a + b
            sum_ += c
            heappush(arr, c)
        except:
            pass

    return sum_


list_ = connect_rope([8, 4, 6, 12]) # 58
# list_ = connect_rope([20, 4, 8, 2]) # 54
# list_ = connect_rope([1, 2, 5, 10, 35, 89]) # 224
# list_ = connect_rope([2, 2, 3, 3])  # 20
print(list_)
