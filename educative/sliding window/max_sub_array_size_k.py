import math


def max_sub_array_of_size_k(k, arr):
  _sum, _max, i, j = 0, -math.inf, 0, 0

  while (j < len(arr)):
    _sum += arr[j]

    if (j >= k - 1):
      _max = max(_max, _sum)
      _sum -= arr[i]
      i += 1

    j += 1

  return _max
