# [IN-PLACE][TWO POINTER]
def reverse_arr(arr):
    i, j = 0, len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr

arr = [1,2,3,4]
print(reverse_arr(arr))

# TODO need to write it using another method
