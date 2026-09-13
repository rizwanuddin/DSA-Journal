"""
Kadane's Algorithm : Maximum Subarray Sum in an Array
Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray. 

I’m using Kadane’s Algorithm to find the maximum sum of a contiguous subarray. I maintain two variables: current_sum, which represents the sum of the subarray I’m currently considering, and maximum, which stores the largest subarray sum 
I’ve found so far. As I go through the array, I add each number to current_sum and then update maximum if this new sum is larger. The key idea is that if current_sum ever becomes negative, there’s no benefit in carrying that negative sum 
into the next subarray because it would only make any future sum smaller, so I reset current_sum back to 0 and effectively start a new subarray from the next element. I initialize maximum to negative infinity instead of 0 so the algorithm 
still works correctly when all the numbers are negative. After processing every element, maximum contains the largest subarray sum. The time complexity is O(n) because I traverse the array only once, and the space complexity is O(1) 
because I only use a couple of variables.

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float("-inf")
        current_sum = 0

        for number in nums:
            current_sum += number
            maximum = max(maximum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return maximum
if __name__ == "__main__":
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
    sol = Solution()
    maxSum = sol.maxSubArray(arr)
    print(f"The maximum subarray sum is: {maxSum}")  



# This is Kadane’s Algorithm with one extra feature: tracking the actual subarray, not just its maximum sum.
"""
I’m using Kadane’s Algorithm, but here I’m also keeping track of the start and end indices of the maximum-sum subarray. I use current_sum to maintain the sum of the subarray I’m currently considering, and maximum stores the best sum found 
so far. As I iterate through the array using enumerate, i gives me the current index and number gives me the current value. I first add the current number to current_sum. If current_sum becomes greater than maximum, I’ve found a better 
subarray, so I update maximum and save its boundaries using ans_start = start and ans_end = i. Here, start represents where my current subarray began, while i represents where it currently ends. If current_sum becomes negative, I reset it 
to 0 because carrying a negative sum forward would only hurt any future subarray, and I set start = i + 1 because if I find a better subarray later, it would begin from the next position. At the end, maximum gives me the maximum sum, while 
ans_start and ans_end tell me exactly which subarray produced that sum. The time complexity is O(n) because I traverse the array once, and the space complexity is O(1) because I only use a few variables.
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float("-inf")
        current_sum = 0

        start = 0
        ans_start = -1
        ans_end = -1

        for i in range(len(nums)):
            current_sum += nums[i]

            # A new maximum-sum subarray was found
            if current_sum > maximum:
                maximum = current_sum
                ans_start = start
                ans_end = i

            # This negative prefix cannot help future subarrays
            if current_sum < 0:
                current_sum = 0
                start = i + 1

        print("Maximum-sum subarray:", nums[ans_start:ans_end + 1])
        return maximum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

sol = Solution()
max_sum = sol.maxSubArray(arr)

print("Maximum subarray sum:", max_sum)

