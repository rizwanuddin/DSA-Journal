"""
Binary Search - Explanation

You are given an array of distinct integers nums, sorted in ascending 
order, and an integer target.Implement a function to search for target 
within nums. If it exists, then return its index, otherwise, return -1.
Your solution must run in O(logn) time.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Example 2:
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1



## Binary Search

**Clarify:**
- Array is sorted ascending, all distinct integers
- Return index of target if found, else -1
- Must run in O(log n)

**Brute force:**
- Linear scan through every element, check for match
- O(n) time — doesn't meet the required complexity

**Optimize:**
- Binary search — repeatedly cut the search space in half using the sorted property
- O(log n) time

**Key observation:**
- Since the array is sorted, comparing the middle element to target tells you which HALF the target must be in (if it's there at all) — no need to check the other half at all
- Each comparison eliminates half the remaining search space, which is what gives the log n time

**Approach:**
- left = 0, right = len(nums) - 1
- while left <= right:
  - mid = (left + right) // 2
  - if nums[mid] == target: found it, return mid
  - if nums[mid] > target: target must be in the left half, right = mid - 1
  - if nums[mid] < target: target must be in the right half, left = mid + 1
- if loop ends with no match: return -1

**While coding:**
- Loop condition must be left <= right, not left < right — otherwise the last remaining candidate (when left == right) never gets checked
- Must actually update left (left = mid+1) when searching the right half — forgetting this leaves left stuck, loop never converges correctly

**Edge cases:**
- Target not in array at all → loop naturally shrinks until left > right, returns -1
- Target is the first or last element → still found correctly, no special-casing needed
- Array with 1 element → left == right == 0 immediately, one comparison decides it

**Complexity:**
- Time: O(log n) — search space halves every iteration
- Space: O(1) — just a few variables
"""
class Solution:
    def Binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
