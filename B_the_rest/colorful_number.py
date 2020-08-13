def colorful_num(num):
    num_str, s = str(num), set()

    for i in range(len(num_str)):
        for j in range(len(num_str)):
            if i < j + 1:
                cur = num_str[i:j + 1]
                prd = prod(cur)
                if prd in s:
                    return False
                else:
                    s.add(prd)

    return True


def prod(nums):
    prd = 1
    for x in nums:
        prd *= int(x)

    return prd


print(colorful_num(263))
