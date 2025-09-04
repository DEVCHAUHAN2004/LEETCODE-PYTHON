
# 75. Sort Colors
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for i in range(n):   # outer loop
            swapped = False
            for j in range(0, n - i - 1):   # inner loop
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            # check after finishing one full pass
            if not swapped:
                break


        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
 