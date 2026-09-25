"""
3Sum - Explanation

Given an integer array nums, return all the triplets [nums[i], 
nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the 
indices i, j and k are all distinct.The output should not contain 
any duplicate triplets. You may return the output and the triplets 
in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.




## 3Sum

**Clarify:**
- Return all unique triplets [a, b, c] from nums where a + b + c == 0
- Indices must be distinct (can't reuse the same element)
- No duplicate triplets in the output, order doesn't matter

**Brute force:**
- Three nested loops, check every triplet, dedupe with a set
- O(n³) time — too slow, and dedup is messy

**Optimize:**
- Sort the array first — this enables two-pointer AND makes duplicate-skipping easy
- Fix one number with an outer loop, then use Two Sum II's two-pointer trick on the rest
- O(n²) time instead of O(n³)

**Key observation:**
- Sorting turns "find a triplet summing to 0" into "fix one number, find a pair summing to -that number" — which is just Two Sum II nested inside a loop
- Once sorted, duplicate values sit next to each other — so duplicates can be skipped by comparing to the previous element
- left always starts at i+1, never goes backward — every triplet including an earlier index was already covered when the loop was at that earlier index

**Approach:**
- Sort nums
- for i in range(len(nums) - 2):
  - skip i if nums[i] == nums[i-1] (avoids duplicate triplets from the fixed number)
  - left = i + 1, right = len(nums) - 1
  - while left < right:
    - current_sum = nums[i] + nums[left] + nums[right]
    - if current_sum == 0: save triplet, move both pointers, then skip duplicates for left and right
    - if current_sum < 0: left += 1 (need bigger)
    - if current_sum > 0: right -= 1 (need smaller)

**While coding:**
- Duplicate skip has to happen at THREE spots: skipping i, skipping left after a match, skipping right after a match
- Skip check for i: `if i > 0 and nums[i] == nums[i-1]: continue`
- After finding a match, before moving on: skip past any repeated values at left and right too, or you'll get the same triplet again
- Outer loop goes to len(nums) - 2, not len(nums) — need room for left and right after i

**Edge cases:**
- Array with fewer than 3 elements → no triplets possible, return []
- All zeros → one triplet [0,0,0], duplicate-skipping must not eliminate it entirely
- No triplet sums to 0 → return []

**Complexity:**
- Time: O(n²) — outer loop O(n), inner two-pointer O(n) each time
- Space: O(1) extra (not counting the output list), O(n) or O(log n) for the sort itself depending on implementation
"""
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right] + nums[i]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return result



"""
## 3Sum — Detailed Breakdown

**Sort first:**
- Two-pointer only works correctly on a sorted array (that's how you know which direction shrinks/grows the sum)
- Sorting also makes duplicate values sit next to each other, which is what makes duplicate-skipping possible at all

**Outer loop — `for i in range(len(nums) - 2)`:**
- `i` fixes one number as the "first" element of the triplet
- Stops at `len(nums) - 2` because `left` and `right` both need room to exist after `i` — no point running `i` past that

**Duplicate skip for `i` — `if i > 0 and nums[i] == nums[i-1]: continue`:**
- If this value is the same as the one right before it, every triplet starting with this value was already fully explored in the previous iteration
- Skipping it avoids generating the exact same triplet twice

**Two pointers — `left = i + 1`, `right = len(nums) - 1`:**
- `left` starts right after `i` (can't reuse `i` itself)
- `right` starts at the far end
- `while left < right:` keeps running as long as there's still a gap between them to search — once they meet or cross, every possible pair for this `i` has been checked

**Sum comparisons:**
- `current_sum < 0` → the total is too small → move `left` right to pick up a bigger number (array is sorted ascending, so this always increases the sum)
- `current_sum > 0` → the total is too big → move `right` left to pick up a smaller number
- `current_sum == 0` → found a valid triplet

**The two inner `while` loops after a match:**
- `while left < right and nums[left] == nums[left-1]: left += 1` — after finding a match, if the next `left` value is identical to the one you just used, skip it too — otherwise you'd form the exact same triplet again with a duplicate value
- `while left < right and nums[right] == nums[right+1]: right -= 1` — same idea, but for `right`
- Both loops still check `left < right` first, so they never run past the point where the pointers meet — same bounds-safety reason as in Valid Palindrome

**Return:**
- `result` holds every unique triplet found — return it once the outer loop finishes
"""

