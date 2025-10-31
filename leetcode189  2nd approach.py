# leetcode 189
nums = [3, 9, 5, 6, 7, 2]
k = 3

def rotate_array(nums, k):
    n = len(nums)
    k = k % n   # in case k > n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums   # return the rotated list

print(rotate_array(nums, k))
# [6, 7, 2, 3, 9, 5]