# num: current number to be built
# x:   current digit used to construct num
# k:   counter to keep track of length of num


def print_well_ordered(k):
    _print_well_ordered(0, 0, k)


def _print_well_ordered(num, x, k):
    if k == 0:
        print(num)
        return

    for i in range(x + 1, 10):
        _print_well_ordered(num * 10 + i, i, k - 1)


print_well_ordered(7)
