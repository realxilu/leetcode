# TODO: BUG!
# const subarraySum = (nums, k) = > {
#     let sum = 0, res = 0
#     let map = new Map()
#     map.set(0, 1)

#     for (let i=0
#          i < nums.length
#          i++) {
#         sum += nums[i]
#         if (map.has(sum - k))
#         res += map.get(sum - k)

#         map.set(sum, (map.get(sum) | | 0) + 1)
#     }

#     return res
# }
