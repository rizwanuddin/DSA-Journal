"""
Product of Array Except Self - Explanation

Given an integer array nums, return an array output where 
output[i] is the product of all the elements of nums except 
nums[i].Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)O(n) time without using the 
division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]




# PRODUCT OF ARRAY EXCEPT SELF — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given an array nums,
and I need to return an array where each position holds the product
of every other element, excluding itself. I also need to do this in
O(n) time without using division."

## 2. BRUTE FORCE

"The brute-force way is, for each index, loop through the entire
array and multiply every element except the one at that index. That
works but costs O(n^2), since it's a nested loop."

## 3. OPTIMIZE

"I can avoid recomputing the product from scratch every time by
splitting the problem into two passes: one that tracks the product of
everything to the left of each index, and one that tracks the product
of everything to the right. Multiplying those two together at each
index gives the answer in O(n) total."

## 4. KEY OBSERVATION

"The product of everything except nums[i] is just the product of
everything to its left, times the product of everything to its
right. If I precompute both of those in single passes, I never need
to loop through the whole array again for each index."

## 5. APPROACH

"I'll build a prefix array, where prefix[i] holds the product of all
elements before index i.

I'll build a suffix array, where suffix[i] holds the product of all
elements after index i.

Then, for each index, I'll multiply prefix[i] and suffix[i] together
to get the final answer for that position."

## 6. WHILE CODING

"First, I set up prefix and suffix arrays, both initialized to 1s,
since 1 is the identity for multiplication and won't affect the
product."

n = len(nums)
prefix = [1] * n
suffix = [1] * n

"I build the prefix array left to right. Each position's prefix is
the previous prefix times the previous number."

for i in range(1, n):
    prefix[i] = prefix[i - 1] * nums[i - 1]

"I build the suffix array right to left, the mirror of the same
idea."

for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1] * nums[i + 1]

"Finally, I combine them — each index's answer is just its prefix
times its suffix."

result = [1] * n
for i in range(n):
    result[i] = prefix[i] * suffix[i]

return result

## 7. EDGE CASES

"If the array contains a single 0, every output position except the
one at that zero's index becomes 0, since every other product
includes that 0. The position of the zero itself ends up holding the
product of everything else, which could be nonzero.

If the array contains two or more zeros, every output position
becomes 0, since every product excluding one zero still includes at
least one other zero."

## 8. COMPLEXITY

"Time complexity is O(n), since I make three separate linear passes
over the array — one for prefix, one for suffix, one to combine.

Space complexity is O(n) for the prefix and suffix arrays, not
counting the output array itself, which the problem doesn't count
against extra space."
"""

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        result = [1] * n
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result