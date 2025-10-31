nums = [1,0,-1,0,-2,2]
target = 0

def four_sum_optimal(nums, target):
    res = []
    n = len(nums)
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:  # skip duplicate i
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:  # skip duplicate j
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    # skip duplicates for k and l
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1

                elif total < target:
                    k += 1
                else:
                    l -= 1
    return res

print(four_sum_optimal(nums, target))
