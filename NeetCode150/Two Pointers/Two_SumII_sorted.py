"""
Two Sum II Input Array Is Sorted - Explanation

Given an array of integers numbers that is sorted in non-decreasing
order.

Return the indices (1-indexed) of two numbers, [index1, index2], 
such that they add up to a given target number target and 
index1 < index2. Note that index1 and index2 cannot be equal, 
therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1)O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, 
index1 = 1, index2 = 2. We return [1, 2].

## Two Sum II - Input Array Is Sorted

**Clarify:**
- Array is already sorted in non-decreasing order
- Return 1-indexed positions [index1, index2], index1 < index2
- Exactly one valid solution guaranteed
- Must use O(1) extra space

**Brute force:**
- Check every pair with two nested loops
- O(n²) time, O(1) space
- Doesn't use the fact that the array is sorted at all

**Optimize:**
- A hashmap (regular Two Sum trick) would get O(n) time but uses O(n) space — violates the constraint
- Binary search per element gets O(n log n) — works but not optimal
- Two pointers gets O(n) time AND O(1) space — best fit, and it uses the sorted property directly

**Key observation:**
- Start one pointer at the smallest value (left end), one at the largest value (right end)
- If sum is too big → the right pointer is contributing too much → move it left for a smaller value
- If sum is too small → the left pointer is contributing too little → move it right for a bigger value
- Sortedness guarantees these moves always shift the sum in the direction you want

**Approach:**
- left = 0, right = len(numbers) - 1
- Loop while left < right:
  - current_sum = numbers[left] + numbers[right]
  - if current_sum == target: return [left+1, right+1] (1-indexed)
  - if current_sum < target: left += 1
  - if current_sum > target: right -= 1

**While coding:**
- Don't forget +1 for 1-indexing on the return
- No duplicate-index check needed — left and right are always different positions

**Edge cases:**
- Smallest array is size 2 — loop still runs correctly once
- Guaranteed exactly one solution, so no "not found" case to handle

**Complexity:**
- Time: O(n) — left and right combined move at most n steps total
- Space: O(1) — just two pointers
"""
class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left + 1, right + 1] 
        return [-1, -1]
