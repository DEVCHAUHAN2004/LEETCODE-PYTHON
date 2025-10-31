class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = [0,1,0,3,1,2]
        n = len(nums)
        if n <= 1:
            return  # nothing to do for empty or single-element array

        i = 0  # next position for non-zero
        for j in range(n):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        # Fill remaining positions with zero
        for k in range(i, n):
            nums[k] = 0
