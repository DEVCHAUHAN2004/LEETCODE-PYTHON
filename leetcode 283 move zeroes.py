nums = [1,0,2,4,0,3,0,0,3,5,1]

def move_zeroes(nums):
    n = len(nums)
    res = []
    # Step 1: Collect all non-zero elements
    for i in range(n):
        if nums[i] != 0:
            res.append(nums[i])    # [1, 2, 4, 3, 3, 5, 1]

    m = len(res)
    # Step 2: Copy non-zero elements back to nums
    for i in range(m):
        nums[i] = res[i]
    # Step 3: Fill the rest with zeros
    for i in range(m, n):
        nums[i] = 0

move_zeroes(nums)
print(nums)
# [1, 2, 4, 3, 3, 5, 1, 0, 0, 0, 0]
