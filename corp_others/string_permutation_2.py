def permute(string):
    res = []

    if len(string) == 1:
        res.append(string)
        return res

    for i, _ in enumerate(string):
        first = string[i]
        rest = string[:i] + string[i + 1:]

        perms = permute(rest)
        for perm in perms:
            res.append(first + perm)

    return res


print(permute('ABC'))
