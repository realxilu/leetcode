from collections import deque

# accumuatlive a number


def build_num(n):
    pass


# get digits
def get_digits(n):
    res = deque([])
    while n:
        res.appendleft(n % 10)
        n = n // 10

    print(list(res))


get_digits(100)
