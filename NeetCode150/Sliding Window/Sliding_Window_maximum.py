"""
Sliding Window Maximum - Explanation

You are given an array of integers nums and an integer k. There is 
a sliding window of size k that starts at the left edge of the 
array. The window slides one position to the right until it 
reaches the right edge of the array.Return a list that contains 
the maximum element in the window at each step.

Example 1:
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]
Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        result = []
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right) # stores only the index
            if q[0] <= right - k:
                q.popleft()
            if right >= k - 1:
                result.append(nums[q[0]])
        return result 

"""
BACK  → remove elements that are TOO SMALL
FRONT → remove elements that are TOO OLD
FRONT → also gives us the MAXIMUM
"""