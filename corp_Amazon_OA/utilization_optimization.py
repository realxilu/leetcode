# [TWO-POINTER] 'a', 'b' are two arrays
def two_sum_closest(a, b, target):
    i, j, _min = 0, len(b) - 1, float('inf')

    # find min
    while i < len(a) and j >= 0:
        diff = abs(target - a[i][1] - b[j][1])
        _min = min(_min, diff)

        if a[i][1] + b[j][1] > target:
            j -= 1
        else:
            i += 1

    # reverse dict
    dic = {x[1]: x[0] for x in b}

    for x, y in a:
        if target - _min - y in dic:
            return x, dic[target - _min - y]

    return -1

## MAIN -----------------------------------------------------------
# testcase 1: solution is (3, 1)
# explanation [3, 14] from 'a' and [1, 5] from 'b', 14 + 5 = 19 closest to 20
# target = 20
# a = [[1, 8], [2, 7], [3, 14]]
# b = [[1, 5], [2, 10], [3, 14]]

# testcase 2: solution is (2, 4) 
# explanation [2, 5] from 'a' and [4, 5] from 'b', 5 + 5 = 10  
target = 10
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]

s = two_sum_closest(a, b, target)
print(s)
