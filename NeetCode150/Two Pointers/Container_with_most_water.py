"""
Container With Most Water - Explanation

You are given an integer array heights where heights[i] represents 
the height of the ithith bar.You may choose any two bars to form a 
container. Return the maximum amount of water a container can 
store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36
Explanation: The bars at indices 1 and 7 have heights 7 and 6. The 
container has width 7 - 1 = 6 and height min(7, 6) = 6, so it can 
store 6 * 6 = 36 units of water. This is the maximum possible area.

Example 2:
Input: height = [2,2,2]
Output: 4




## Container With Most Water

**Clarify:**
- heights[i] is the height of bar i, pick any two bars to form a container
- Water level is capped by the shorter of the two chosen bars
- Return the max possible area (width × height)

**Brute force:**
- Check every pair (i, j), compute area, track the max
- O(n²) time, O(1) space
- Works but ignores any structure that could speed it up

**Optimize:**
- Two pointers starting at both ends gives the maximum possible width immediately
- Every move after that only shrinks width — so the only way to potentially beat the current area is to move the pointer that has a chance of increasing height
- O(n) time instead of O(n²)

**Key observation:**
- Area = width × min(height[left], height[right]) — height is always bottlenecked by the shorter bar, the taller one is irrelevant
- Moving the taller pointer can never help — width shrinks and height either stays the same or gets worse
- Moving the shorter pointer is the only move that has a chance of increasing height, which is the only way to possibly increase area despite the shrinking width

**Approach:**
- left = 0, right = len(heights) - 1, max_area = 0
- while left < right:
  - width = right - left
  - height = min(heights[left], heights[right])
  - max_area = max(max_area, width * height)
  - if heights[left] < heights[right]: move left forward
  - else: move right backward

**While coding:**
- Don't forget to compute area BEFORE moving either pointer — you're measuring the container as it currently stands
- Use max() to update max_area each iteration rather than an if-check, cleaner

**Edge cases:**
- Only 2 bars → one single area calculation, loop runs once
- All bars equal height → doesn't matter which pointer moves, height stays the same either way, width still shrinks correctly

**Complexity:**
- Time: O(n) — left and right combined move at most n steps total
- Space: O(1) — just a few variables
"""
class Solution:
    def maxArea(self, heights):
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            height = min(heights[left],heights[right])
            width = right - left
            max_area = max(height * width, max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

        