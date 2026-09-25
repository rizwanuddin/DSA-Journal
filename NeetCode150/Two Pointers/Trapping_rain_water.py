"""
Trapping Rain Water - Explanation

You are given an array of non-negative integers height which 
represent an elevation map. Each value height[i] represents the 
height of a bar, which has a width of 1.Return the total amount of 
water that can be trapped between the bars.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9



## Trapping Rain Water

**Clarify:**
- height[i] = height of bar i, width of each bar is 1
- Return total water trapped across the whole array
- Water at each bar is capped by the shorter of (tallest bar to its left, tallest bar to its right)

**Brute force:**
- For every index, scan left for the max, scan right for the max, compute water there
- O(n) work per index × n indices = O(n²) time, O(1) space
- Correct but slow

**Optimize:**
- Precompute left_max and right_max for every index ONCE, using two arrays, before the main loop
- Then it's just one pass to sum up the water — O(n) time, O(n) space
- (Even better O(1) space version exists with two pointers, but the two-array version is the clearer starting point)

**Key observation:**
- left_max[i] = the max of everything from index 0 to i (inclusive)
- right_max[i] = the max of everything from index i to the end (inclusive)
- Both of these can be built with a single left-to-right pass and a single right-to-left pass — no need to rescan the whole array for every index

**Approach:**
- Build left_max array: left_max[i] = max(height[i], left_max[i-1])
- Build right_max array: right_max[i] = max(height[i], right_max[i+1])
- For each index i: water += min(left_max[i], right_max[i]) - height[i]

**While coding:**
- left_max[0] = height[0] (nothing to its left, so it's just its own height)
- right_max[last] = height[last] (nothing to its right)
- min(left_max[i], right_max[i]) will always be >= height[i] once built correctly, since height[i] is included in both max calculations — so the subtraction never actually needs a max(0, ...) guard, but it's safe to add for clarity

**Edge cases:**
- Array with fewer than 3 bars → can't trap any water, return 0
- All bars same height → no dips, water = 0 everywhere

**Complexity:**
- Time: O(n) — three separate O(n) passes (left_max, right_max, sum)
- Space: O(n) — two extra arrays of size n
"""
class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        total_water = 0
        for i in range(n):
            total_water += min(left_max, right_max) - height[i]
        return total_water

"""
## How the summing loop actually finds trapped water

- Think of water being poured over the whole elevation map and settling into the dips — at any single bar, there's either a little column of water sitting on top of it, or nothing at all if it's a high point
- To know how much water sits at one specific bar, you need to know how high the water is ALLOWED to rise at that exact spot — that's the "water surface level"
- The water surface level at index i is decided by whichever wall is SHORTER: left_max[i] or right_max[i] — because water spills over the shorter side the moment it tries to rise past that height, no matter how tall the other wall is
- That's exactly why the code uses min(left_max[i], right_max[i]) — it's picking the shorter of the two walls, which is the true ceiling for water at that position
- Once you know the water surface level, you subtract height[i] — because the bar itself already fills up space from the ground up to its own height, and only the empty gap ABOVE the bar, up to the water surface, is actual trapped water
- If the bar's own height is already equal to or taller than that surface level, the subtraction comes out to zero or negative, meaning no water sits there — makes sense, since a tall bar can't have water resting on top of it if there's nothing higher on both sides to hold it in
- The loop does this calculation independently for every single index — each index is treated like its own little isolated puddle problem, using only its own left_max, right_max, and height
- Since these are separate puddles at separate locations, the only way to get the TOTAL water trapped across the whole map is to add every individual puddle's amount together — that's what total_water += ... does on every iteration, accumulating one puddle's worth of water into the running total each time
- By the time the loop finishes, total_water holds the sum of every puddle across the entire array, which is exactly what the problem is asking for
"""
