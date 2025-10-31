class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1    

        while left < right:          
            x = numbers[left] + numbers[right]  

            if x == target:
                return [left + 1, right + 1]  # 1-based index

            elif x < target:
                left += 1
            else:
                right -= 1


# -----------------------------
# Example to run in VS Code
# -----------------------------
numbers = [2, 7, 11, 15]
target = 9

sol = Solution()
result = sol.twoSum(numbers, target)
print("Indices:", result)
