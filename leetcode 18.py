nums = [1,0,-1,0,-2,2]
target = 0

def four_sum(nums, target):
    n = len(nums)
    my_set = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:  # use target
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))

    return [list(ans) for ans in my_set]

print(four_sum(nums, target))
# [[-2, -1, 1, 2], [-1, 0, 0, 1], [-2, 0, 0, 2]]