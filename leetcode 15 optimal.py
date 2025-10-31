nums = [-1,0,1,2,-1,-4]

def threesums_optimal(nums):
    n = len(nums)
    ans = []
    nums.sort()  # [-4, -1, -1, 0, 1, 2]

    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue  # skip duplicates for i

        j = i + 1
        k = n - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                # skip duplicates for j and k
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:  # notice k+1
                    k -= 1

    return ans

print(threesums_optimal(nums))
