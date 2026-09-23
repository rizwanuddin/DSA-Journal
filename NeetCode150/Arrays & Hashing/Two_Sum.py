"""
Two Sum - Explanation

Given an array of integers nums and an integer target, return the indices 
i and j such that nums[i] + nums[j] == target and i != j.You may assume that
every input has exactly one pair of indices i and j that satisfy the 
condition.Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]



# TWO SUM — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given an array nums
and a target. I need to find two indices i and j such that
nums[i] + nums[j] equals target, and return those indices with the
smaller one first. There's guaranteed to be exactly one valid pair."

## 2. BRUTE FORCE

"The brute-force way is to check every pair of numbers using two
nested loops, and see if any pair adds up to target. That's O(n^2)
since for each number I'm scanning the rest of the array."

## 3. OPTIMIZE

"I can do better with a hashmap. As I go through the array, for each
number I know exactly what other number I'd need to hit the target —
it's just target minus the current number. So instead of scanning
forward for it, I can check a hashmap in O(1) to see if I've already
passed that number."

## 4. KEY OBSERVATION

"For every number, I calculate what I'd need to complete the pair —
target minus that number. If I've already seen that needed value
earlier in the array, I've found my pair right there. If not, I store
the current number so future numbers can find it."

## 5. APPROACH

"I'll create an empty dictionary called seen, where the key is a
number and the value is its index.

Then I'll loop through nums using enumerate, so I get both the index
and the value at each step.

For each number, I'll calculate remaining as target minus that
number.

I'll check if remaining is already a key in seen. If it is, that
means I've found my pair, so I return the stored index for remaining,
followed by the current index.

If it's not there yet, I store the current number and its index in
seen, and move to the next number."

## 6. WHILE CODING

"First, I create a dictionary to store numbers I've already seen,
along with their index."

seen = {}

"I loop through nums using enumerate, so I get both the index and the
value at once."

for i, num in enumerate(nums):

"For each number, I calculate what value I'd need to complete the
pair."

    remaining = target - num

"Now I check if that value is already in my dictionary."

    if remaining in seen:

"If it is, I've found my pair. The stored index comes first since it
was seen earlier, then the current index."

        return [seen[remaining], i]

"If it's not there, I store the current number and its index for
future lookups."

    seen[num] = i

"The problem guarantees a solution exists, so this line is just a
fallback."

return [-1, -1]

## 7. EDGE CASES

"If the array has fewer than two elements, there's no valid pair, but
the problem guarantees a solution exists, so I don't need to handle
that separately."

"If the same number appears twice and their sum equals target, this
still works correctly, because I check the hashmap before storing the
current number, so I'm never matching a number with itself."

## 8. COMPLEXITY

"Time complexity is O(n), since I make a single pass through the
array and each hashmap operation is O(1) on average.

Space complexity is O(n) in the worst case, since I might end up
storing almost every number in the hashmap before finding the pair."
"""
class Solution:
    def two_Sum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], i]
            seen[num] = i
        return [-1, -1]