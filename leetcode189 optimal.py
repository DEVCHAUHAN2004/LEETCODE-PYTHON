nums = [4, 5, 3, 2, 6, 8, 9, 3, 1, 6, 9]
k = 5

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def rotatearray(nums, k):
    n = len(nums)
    k = k % n  # handle k > n
    
    # Step 1: reverse the entire array
    reverse(nums, 0, n-1)
    # Step 2: reverse first k elements
    reverse(nums, 0, k-1)
    # Step 3: reverse remaining n-k elements
    reverse(nums, k, n-1)
    return nums

print(rotatearray(nums, k))
# [9, 3, 1, 6, 9, 4, 5, 3, 2, 6, 8]
