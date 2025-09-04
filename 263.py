# 263. Ugly Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
 class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1):
            return True
        if(n<=0):
            return False
        while(n>1):
            for i in [2,3,5]:
                if n % i ==0:
                    n //= i
                    break
            else:
                return False 
        return True                   
        