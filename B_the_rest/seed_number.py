# Input: n = 138
# Output: 23

# Input: n = 4977
# Output: 79 711

# Input: n = 738
# Output: 123


def get_product(n):
    prod = 1
    while n > 1:
        prod *= n % 10
        n = n // 10

    return prod


def get_seed(num):
    res = []
    for i in range(num // 2):
        if i * get_product(i) == num:
            res.append(i)

    return res if len(res) else None


test = get_seed(4977)
print(test)
