# [WARM-UP]
def remove_duplicates(arr):
    # 'i' is the index of the next non-duplicate element
    # note both pointers are starting at the 2nd position
    i, j = 1, 1

    while j < len(arr):
        if arr[i - 1] != arr[j]:
            arr[i] = arr[j]
            i += 1
        j += 1

    # debug point
    print(list(arr[:i]))

    return i

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # [2, 3, 6, 9]
print(remove_duplicates([2, 2, 2, 11])) # [2, 11]
