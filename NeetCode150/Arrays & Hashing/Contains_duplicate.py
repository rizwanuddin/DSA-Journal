"""
Contains Duplicate - Explanation

Given an integer array nums, return true if any value appears more than once in the array, 
otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false


# CONTAINS DUPLICATE — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. We're given an array
nums, and I need to return True if any value appears more than once,
otherwise False."

## 2. BRUTE FORCE

"The brute-force way is to compare every pair of elements and check
if any two match. That's O(n^2) since I'm nesting a loop inside a
loop."

## 3. OPTIMIZE

"I can do better using a set. A set gives me constant-time lookup, so
instead of comparing every pair, I can just check 'have I seen this
number before' as I go."

## 4. KEY OBSERVATION

"For every number, I only need to know one thing: has it shown up
already?

If yes, that's my duplicate, and I can return True right away.
If no, I add it to my set and keep going."

## 5. APPROACH

"I'll create an empty set called seen.

Then I'll loop through nums. For each number, I'll check if it's
already in seen.

If it is, I return True immediately.

If it's not, I add it to seen and move to the next number.

If I finish the loop without ever finding a repeat, I return False."

## 6. WHILE CODING

"First, I create an empty set to track what I've seen."

seen = set()

"Now I loop through every number in the array."

for num in nums:

"For each number, I check if it's already in my set."

    if num in seen:
        return True

"If it's a duplicate, I return True right away, no need to keep
scanning."

"If it's not a duplicate, I add it to the set."

    seen.add(num)

"If I get through the whole array with no repeats, I return False."

return False

## 7. EDGE CASES

"If the array is empty, the loop never runs, so I return False. That's
correct, since there's nothing to duplicate."

"If the array has only one element, same thing — the loop runs once,
nothing's in the set yet, so I return False."

## 8. COMPLEXITY

"Time complexity is O(n), since I make one pass through the array and
each set operation is O(1) on average.

Space complexity is O(n) in the worst case, since if there are no
duplicates, every element ends up stored in the set."
"""
def contains_duplicate(self, nums):
    seen = set()
    for num in nums:
        if num in seen:
            return  True
        else:
            seen.add(num)
    return False

        