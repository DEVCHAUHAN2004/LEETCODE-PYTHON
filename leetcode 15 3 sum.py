nums = [-1,0,1,2,-1,-4]

def threesums(nums):
  n = len(nums)
  my_set = set()

  for i in range(0,n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        total = nums[i] + nums[j] + nums[k]
        if total ==  0:
          temp = [nums[i],nums[j],nums[k]]
          temp.sort()
          my_set.add(tuple(temp))
  return [list(ans) for ans in my_set]

x = threesums(nums)
print(x)
# [[-1, 0, 1], [-1, -1, 2]]

