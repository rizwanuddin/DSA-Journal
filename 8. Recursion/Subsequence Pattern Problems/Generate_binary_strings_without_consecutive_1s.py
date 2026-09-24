"""
Generate Binary Strings Without Consecutive 1s

Given an integer n, return all binary strings of length n that do 
not contain consecutive 1s. Return the result in lexicographically 
increasing order.A binary string is a string consisting only of 
characters '0' and '1'.

Example 1:
Input: n = 3
Output: ["000", "001", "010", "100", "101"]
Explanation: All strings are of length 3 and do not contain 
consecutive 1s.

Example 2:
Input: n = 2
Output: ["00", "01", "10"]




# GENERATE BINARY STRINGS WITHOUT CONSECUTIVE 1s — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I need to generate every
binary string of length n that never has two 1s next to each other,
returned in lexicographically increasing order."

## 2. BRUTE FORCE

"The brute-force way is to generate every possible binary string of
length n, which is 2^n of them, then filter out the ones with
consecutive 1s. That works but does wasted work building strings
we'll just throw away."

## 3. OPTIMIZE

"Instead of generating everything and filtering after, I can avoid
ever building an invalid string in the first place, by only allowing
a '1' to be placed when the previous digit wasn't already a '1'."

## 4. KEY OBSERVATION

"This is the same include or skip structure as every other
subsequence problem, except the choice isn't free anymore — placing a
'0' is always allowed, but placing a '1' depends on what the last
digit was. So my recursive function needs to track one extra piece of
state: what digit was placed last."

## 5. APPROACH

"I'll create a helper function that tracks the current index, the
string built so far, and the last digit placed.

If the index reaches n, the string is complete and valid by
construction, so I save it.

Otherwise, I always try placing a '0', since that's never restricted.

Then, separately, I try placing a '1', but only if the last digit
wasn't already '1'.

I start the recursion at index 0, with an empty string, treating the
starting state as if the last digit were '0' so a '1' is allowed
first."

## 6. WHILE CODING

"First, I set up a list to collect valid strings."

result = []

"My helper tracks index, the string built so far, and the last digit
placed."

def helper(index, current, last_digit):

"If I've placed n digits, the string is complete and already valid,
so I save it."

    if index == n:
        result.append(current)
        return

"Placing a '0' is always safe, so I always try it."

    helper(index + 1, current + "0", "0")

"Placing a '1' is only safe if the last digit wasn't already '1', so
I guard this call with a condition."

    if last_digit != "1":
        helper(index + 1, current + "1", "1")

"I kick off the recursion at index 0 with an empty string, treating
the start as if the last digit were '0'."

helper(0, "", "0")
return result

## 7. EDGE CASES

"If n is 1, the valid strings are just '0' and '1', since there's no
second digit to conflict with the first.

Since '0' is always tried before '1' at every step, the results come
out in lexicographic order naturally, with no extra sorting needed."

## 8. COMPLEXITY

"Time complexity is bounded by O(2^n) in the worst case, though it's
actually smaller in practice since invalid branches are never
explored.

Space complexity is O(n) for the recursion stack depth, plus the
space needed to store all the valid output strings."
"""
class Solution:
    def validStrings(self, n):
        result = []

        def helper(index, current, last_digit):
            if index == n:
                result.append(current)
                return

            # always allowed: place a 0
            helper(index + 1, current + "0", "0")

            # only allowed if last digit wasn't 1
            if last_digit != "1":
                helper(index + 1, current + "1", "1")

        helper(0, "", "0")
        return result