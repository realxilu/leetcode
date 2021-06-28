# [ATTENTION] Two pointer method does NOT work here!
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sum, count = 0, 0
        dic = {0: 1}

        for x in nums:
            # prev_sum is a running sum and by this point it has jumped up by x
            prev_sum += x
            # whenever the prev_sum has increased by a value of k
            # if prev_sum (by now it has added x in already due to the prev line) has jumped by by value of k
            count += dic.get(prev_sum - k, 0)
            dic[prev_sum] = dic.get(prev_sum, 0) + 1

        return count

# [KEY] whenever the sums has increased by a value of k, we've found a subarray of sums = k.
# Example: Let's say our elements are [1, 2, 1, 3] and k = 3. sums = [1, 3, 4, 7]
# Now, if you notice the running sums array, from 1->4, there is increase of k and from 4 -> 7, 
# there is an increase of k. So, we've found 2 subarrays of sums = k.

# But, if you look at the original array, there are 3 subarrays of sums == k. Now, you'll understand why 0 comes in the picture.

# In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays.
# However, if sums == k, it should've been 3 - 0 = k. 
# But 0 is not present in the array. To account for this case, we include the 0.
# Now the modified sums array will look like [0, 1, 3, 4, 7]. Now, try to see for the increase of k.

# 0 -> 3
# 1 -> 4
# 4 -> 7
# Hence, 3 sub arrays of sums = k
