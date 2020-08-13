def permute(string):
    return _permute(list(string), 0, len(string) - 1, [])


def _permute(arr, l, r, res):
    if l == r:
        res.append(''.join(arr))
        return

    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]
        _permute(arr, l + 1, r, res)
        arr[l], arr[i] = arr[i], arr[l]  # backtrack

    return res


print('Print permutation:')
print(permute('123'))
