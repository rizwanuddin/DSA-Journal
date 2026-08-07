"""
FIRST APPROACH - BRUTE FORCE (Three nested loops lol)

Find the length of the longest subarray whose sum equals K using brute force.

Problem:Given an array and an integer k, find the length of the longest
contiguous subarray whose elements add up to k.

If no such subarray exists, return 0.

Example:nums = [-1, 1, 1]k = 1

Output: 3

The longest valid subarray is:
    [-1, 1, 1]

Its sum is:
    -1 + 1 + 1 = 1

Tree visualization:Array:[-1, 1, 1]

startIndex = 0
|
|-- endIndex = 0  -> [-1]
|       sum = -1
|
|-- endIndex = 1  -> [-1, 1]
|       sum = 0
|
`-- endIndex = 2  -> [-1, 1, 1]
        sum = 1
        length = 3
        maxLength = 3

startIndex = 1
|
|-- endIndex = 1  -> [1]
|       sum = 1
|       length = 1
|       maxLength = 3
|
`-- endIndex = 2  -> [1, 1]
        sum = 2

startIndex = 2
|
`-- endIndex = 2  -> [1]
        sum = 1
        length = 1
        maxLength = 3

Length formula:length = endIndex - startIndex + 1

The +1 is needed because both the starting index and ending index
are included in the subarray.

Example:startIndex = 0endIndex = 2

Indices included:
    0, 1, 2

length = 2 - 0 + 1
       = 3

Without +1:
    2 - 0 = 2

This gives only the distance between the indices, not the number
of elements.

Loop responsibilities:- First loop:Chooses where the subarray starts.

- Second loop:
    Chooses where the subarray ends.

- Third loop:
    Calculates the sum of the chosen subarray.

Time Complexity: O(n^3)Space Complexity: O(1)"""


class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums) 
        maxLength = 0

        # starting index
        for startIndex in range(n):
            # ending index
            for endIndex in range(startIndex, n):
                # add all the elements of 
                # subarray = nums[startIndex...endIndex]
                currentSum = 0
                for i in range(startIndex, endIndex + 1):
                    currentSum += nums[i]

                if currentSum == k:
                    maxLength = max(maxLength, endIndex - startIndex + 1)

        return maxLength

if __name__ == "__main__":
    nums = [-1, 1, 1]
    k = 1

    # Create an instance of the Solution class
    solution = Solution()
    # Function call to get the result
    length = solution.longestSubarray(nums, k)
    
    print("The length of the longest subarray is:", length)
