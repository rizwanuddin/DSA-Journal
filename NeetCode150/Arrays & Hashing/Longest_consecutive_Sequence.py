"""
Longest Consecutive Sequence - Explanation

Given an array of integers nums, return the length of the longest 
consecutive sequence of elements that can be formed.A consecutive 
sequence is a sequence of elements in which each element is 
exactly 1 greater than the previous element. The elements do not 
have to be consecutive in the original array.You must write an 
algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7



# LONGEST CONSECUTIVE SEQUENCE — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given an array of
integers, and I need to find the length of the longest run of
consecutive numbers that can be formed, where each number is exactly
one greater than the previous. The numbers don't need to be
consecutive in the original array, just present somewhere in it. I
need to do this in O(n) time."

## 2. BRUTE FORCE

"The brute-force way is, for every number, repeatedly check if the
next number exists in the array, extending the streak as far as
possible. That works, but if I do this starting from every single
number, I end up re-walking the same sequence multiple times, which
makes it O(n^2) in the worst case."

## 3. OPTIMIZE

"I can avoid the repeated work by only starting a count from numbers
that are actually the beginning of a sequence. A number is the start
of a sequence if the number one less than it doesn't exist in the
array. That way, each sequence only ever gets counted once, from its
true starting point."

## 4. KEY OBSERVATION

"Frequency of numbers doesn't matter here, only whether a number is
present. So a set works, not a hashmap. And checking num minus one
before starting a count is what keeps the whole thing O(n), since
every number is only ever walked as part of one sequence, never
recounted from the middle."

## 5. APPROACH

"I'll put every number into a set for fast lookup.

For each number in the set, I'll check if one less than it exists in
the set. If it does, this number isn't the start of a sequence, so I
skip it.

If it's not there, this number is a genuine starting point, so I
count forward, checking num plus 1, num plus 2, and so on, as long as
each next number exists in the set.

I'll track the longest streak found across all valid starting
points, and return that."

## 6. WHILE CODING

"First, I put all the numbers into a set for O(1) lookups."

num_set = set(nums)
longest = 0

"I loop through each unique number."

for num in num_set:

"I only start counting if this number is the beginning of a
sequence, meaning one less than it isn't in the set."

    if (num - 1) not in num_set:
        length = 1

"I extend the streak forward as long as the next number exists."

        while (num + length) in num_set:
            length += 1

"I update the longest streak found so far."

        longest = max(longest, length)

return longest

## 7. EDGE CASES

"If the array is empty, the loop never runs, and I correctly return
0.

If the array has duplicate numbers, the set naturally collapses them,
so duplicates don't affect the result at all.

If there's no consecutive sequence longer than 1, every number acts
as its own starting point with length 1, so the answer correctly
becomes 1."

## 8. COMPLEXITY

"Time complexity is O(n). Even though there's a while loop inside a
for loop, each number is only ever visited as part of one sequence's
walk, since we only start counting from true sequence beginnings, so
the total work across all iterations adds up to O(n), not O(n^2).

Space complexity is O(n), for storing all the numbers in the set."
"""
class Solution:
    def longest_sequence(self, nums):
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longset = max(longest, length)
        return longest
