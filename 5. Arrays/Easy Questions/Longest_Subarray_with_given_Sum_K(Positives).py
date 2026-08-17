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

"""SECOND APPROACH - OPTIMAL - TWO POINTERS/SLIDING WINDOW
I'm solving this using a sliding-window approach with two pointers, left and right.

These pointers represent the current subarray I'm considering.

I also maintain a running sum so I don't need to calculate the sum of the entire subarray repeatedly.

I expand the window by moving right forward and adding the new element to the running sum.

If the sum becomes greater than k, I shrink the window from the left by subtracting nums[left] and moving left forward.

Whenever the current sum equals k, I've found a valid subarray, so I calculate its length using right - left + 1 and update maxLen.

I continue this until the right pointer reaches the end of the array.
The time complexity is O(n) because each element is visited at most twice: once when the right pointer includes it and once when the left pointer removes it.”

Time: O(n)

Then:

“The space complexity is O(1) because I'm only using a few variables and not creating another data structure that grows with the input
TIME COMPLEXITY - O(n)
SPACE COMPLEXITY - O(1)
"""
class Solution:
    # Function to find the length of longest subarray having sum k
    def longestSubarray(self, nums, k):
        n = len(nums)
        
        # To store the maximum length of the subarray
        maxLen = 0
        
        # Pointers to mark the start and end of window
        left = 0
        right = 0
        
        # To store the sum of elements in the window
        sum = nums[0]
        
        # Traverse all the elements
        while right < n:
            
            # If the sum exceeds K, shrink the window
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            
            # Store the maximum length
            if sum == k:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
            if right < n:
                sum += nums[right]
        
        return maxLen


nums = [10, 5, 2, 7, 1, 9]
k = 15

# Creating an object of Solution class
sol = Solution()

# Function call to find the length
# of longest subarray having sum k
ans = sol.longestSubarray(nums, k)

print(f"The length of longest subarray having sum k is: {ans}")

