"""
Count all subsequences with sum K

Given an array nums and an integer k.Return the number of non-empty 
subsequences of nums such that the sum of all elements in the 
subsequence is equal to k.

Example 1:
Input : nums = [4, 9, 2, 5, 1] , k = 10
Output : 2
Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].

Example 2:
Input : nums = [4, 2, 10, 5, 1, 3] , k = 5
Output : 3
Explanation : The possible subsets with sum k are [4, 1] , [2, 3] , [5].
"""
class Solution:
    def countSubsequences(self, nums, k):
        n = len(nums)

        def helper(index, current_sum):

            # No elements left to decide on
            if index == n:
                return 1 if current_sum == k else 0

            # Choice 1: include nums[index]
            include = helper(index + 1, current_sum + nums[index])

            # Choice 2: skip nums[index]
            skip = helper(index + 1, current_sum)

            return include + skip

        return helper(0, 0)