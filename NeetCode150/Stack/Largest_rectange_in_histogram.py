"""
Largest Rectangle In Histogram - Explanation

You are given an array of integers heights where heights[i] represents the height of a bar.
The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.
Note: This chart is known as a histogram.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8

Example 2:
Input: heights = [1,3,7]
Output: 7



## Largest Rectangle in Histogram

**Clarify:**
- Given bar heights (width 1 each), find the largest rectangular area that can be formed using contiguous bars
- The rectangle's height is limited by the shortest bar it spans

**Brute force:**
- For every pair of bars, find the min height between them, compute area, track the max
- O(n²) or worse

**Optimize:**
- Monotonic stack — store (start_index, height) pairs, keep heights increasing from bottom to top of stack
- O(n) time, each bar pushed and popped at most once

**Key observation:**
- A bar's rectangle can only extend as far left and right as it remains the SHORTEST bar in that range — once a shorter bar shows up, the taller bar's max possible width is now locked in, since it can't extend past that shorter bar
- When a new bar is shorter than what's on top of the stack, every taller bar on the stack that can't survive next to it gets "finalized" — pop them and compute their final area
- The popped bar's width stretches from its own start_index to the current index i (exclusive) — because everything between them was taller than it, so it could have spanned that whole range
- When popping, the new shorter bar absorbs the popped bar's start_index — because the current bar could also have extended back that far (everything in that stretch is >= current height)

**Approach:**
- stack = [] (holds (start_index, height) pairs, heights increasing), maxArea = 0
- for i, h in enumerate(heights):
  - start = i
  - while stack is not empty AND top of stack's height > h:
    - pop (index, height) off the stack
    - compute area = height * (i - index), update maxArea
    - start = index (this bar's range now extends back to where the popped bar started)
  - push (start, h) onto the stack
- after the loop, anything still on the stack never got "cut off" by a shorter bar — resolve them against the end of the array:
  - for i, h in stack: maxArea = max(maxArea, h * (len(heights) - i))

**While coding:**
- Storing (start_index, height) as a pair matters — start_index tracks how far back this bar's potential rectangle could stretch, which changes as shorter bars absorb the start of taller popped bars
- The final loop after the main one is necessary — bars still on the stack at the end are increasing all the way to the end of the array, so they never got resolved inside the main loop, need their width computed against len(heights)

**Edge cases:**
- Strictly increasing heights → nothing gets popped until the final cleanup loop at the end
- Strictly decreasing heights → almost everything pops immediately, width stays small each time
- All bars the same height → one single stack entry effectively represents the whole range once fully processed

**Complexity:**
- Time: O(n) — each index is pushed once and popped at most once
- Space: O(n) — worst case (strictly increasing heights), stack holds every bar
"""
class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
