# i: start
# j: end
def pair_with_targetsum(arr, target_sum):
    i, j = 0, len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == target_sum:
            return [i, j]

        if arr[i] + arr[j] > target_sum:
            j -= 1
        else:
            i += 1

    return -1
