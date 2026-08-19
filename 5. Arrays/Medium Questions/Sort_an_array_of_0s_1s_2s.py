"""
Sort an array of 0s, 1s and 2s
Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. 
The sorting must be done in-place, without making a copy of the original array.

I’m using the Dutch National Flag algorithm to sort an array containing only 0s, 1s, and 2s using three 
pointers: low, mid, and high. I start low and mid at the beginning and high at the end, and I basically follow 
three rules. If nums[mid] == 0, I swap nums[mid] with nums[low], then increment both low and mid. If 
nums[mid] == 1, I don’t need to swap anything, so I just increment mid. If nums[mid] == 2, I swap nums[mid] 
with nums[high] and decrement high, but I do not increment mid because the value that just came from the high 
position hasn’t been checked yet, so I need to process it first. I keep applying these three rules while 
mid <= high, and once the loop finishes, the array is sorted. The time complexity is O(n) because I process 
the array in one pass, and the space complexity is O(1) because everything is done in-place using only the 
three pointers.
"""
class Solution:
    # Function to sort list containing 0s, 1s, and 2s using Dutch National Flag Algorithm
    def sortZeroOneTwo(self, nums):
        # Initialize three pointers: low and mid at 0, high at end
        low, mid, high = 0, 0, len(nums) - 1

        # Traverse until mid crosses high
        while mid <= high:
            # If element is 0, swap with low, move both low and mid forward
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # If element is 1, just move mid forward
            elif nums[mid] == 1:
                mid += 1
            # If element is 2, swap with high, move only high backward
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Driver code
nums = [2, 0, 2, 1, 1, 0]
obj = Solution()
obj.sortZeroOneTwo(nums)
print(nums)
