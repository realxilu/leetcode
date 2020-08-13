def print_star(n):
    for i in range(n):
        print('*', end='')
    print()


def print_stars(n):
    for i in range(1, n + 1):
        print_star(i)


print_stars(3)
