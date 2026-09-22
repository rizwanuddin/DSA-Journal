"""
Check if there exists a subsequence with sum K

Given an array nums and an integer k. R﻿eturn true if there exist subsequences such that the sum 
of all elements in subsequences is equal to k else false.

Example 1:
Input : nums = [1, 2, 3, 4, 5] , k = 8
Output : Yes
Explanation : The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

Example 2:
Input : nums = [4, 3, 9, 2] , k = 10
Output : No
Explanation : No subsequence can sum up to 10.



CHECK IF A SUBSEQUENCE SUMS TO K — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array nums and a target k.

I need to determine whether there is at least one subsequence whose
elements add up to k.

For every element, I can either include it in the subsequence or skip
it.

I only need to return True or False."


2. BRUTE FORCE

"The brute-force idea is to generate every possible subsequence and
calculate its sum.

Since every element has two choices, include or skip, there can be
2^n different subsequences.

Instead of explicitly storing all of them, I can explore those choices
using recursion."


3. OPTIMIZE

"I can use recursive backtracking and keep track of the running sum.

This way, I don't need to actually build and store each subsequence.

Also, since I only need to know whether one valid subsequence exists,
I can immediately return True as soon as I find one."


4. KEY OBSERVATION

"The key observation is that for every element I have two choices:

1. INCLUDE nums[index]
2. SKIP nums[index]

If I include it, I add nums[index] to current_sum.

If I skip it, current_sum stays the same.

Then in both cases, I move to index + 1.

If current_sum ever becomes equal to k, I've found a valid subsequence
and can immediately return True."


5. APPROACH

"I'll create a recursive helper function that keeps track of:

index       → which element I'm currently deciding on
current_sum → sum of the elements I've chosen so far

First, I'll check whether current_sum equals k.

If it does, I'll immediately return True.

If I've reached the end of the array without finding the target sum,
I'll return False.

Otherwise, I'll first explore the INCLUDE choice by adding nums[index]
to current_sum and moving to the next index.

If that path returns True, I can immediately return True without
checking anything else.

Otherwise, I'll explore the SKIP choice by moving to the next index
without changing current_sum.

Finally, I'll start the recursion at index 0 with a sum of 0."


6. WHILE CODING

"My helper function keeps track of the current index and the running
sum."

def helper(index, current_sum):

"First, I'm checking whether I've already reached the target."

if current_sum == k:
    return True

"If I've used all the elements without reaching k, this path failed."

if index == n:
    return False

"Now I'm exploring my first choice: INCLUDE the current number."

if helper(index + 1, current_sum + nums[index]):
    return True

"If including the current number eventually finds a valid subsequence,
I immediately return True because I only need one solution."

"Otherwise, I'm exploring the second choice: SKIP the current number."

return helper(index + 1, current_sum)

"Finally, I'll start at index 0 with a current sum of 0."

return helper(0, 0)


7. EDGE CASES

"If k is 0, the current code immediately returns True because the empty
subsequence has a sum of 0."

if current_sum == k:
    return True

"If the problem requires a NON-EMPTY subsequence, then I would need to
track whether I've selected at least one element before returning True."

"If nums is empty, the result depends on k.

If k is 0, the empty subsequence works.

Otherwise, index reaches n and I return False."

if current_sum == k:
    return True

if index == n:
    return False

"If negative numbers are allowed, I should NOT add a condition like:

if current_sum > k:
    return False

because a negative number later could bring the sum back down."


8. COMPLEXITY

"In the worst case, every element gives me two recursive choices:
include or skip.

So the time complexity is O(2^n).

The recursion can go at most n levels deep, so the auxiliary space
complexity is O(n) because of the recursion stack.

Since I'm only tracking current_sum instead of storing the actual
subsequence, I don't use additional space for building subsets."
"""
class Solution:
    def checkSubsequenceSum(self, nums, k):
        n = len(nums)

        def helper(index, current_sum):

            # Found a subsequence that sums to k
            if current_sum == k:
                return True

            # No elements left, and sum never hit k
            if index == n:
                return False

            # Choice 1: include nums[index]
            if helper(index + 1, current_sum + nums[index]):
                return True

            # Choice 2: skip nums[index]
            return helper(index + 1, current_sum)

        return helper(0, 0)
