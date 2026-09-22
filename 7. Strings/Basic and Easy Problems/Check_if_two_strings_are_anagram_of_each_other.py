'''
Check if two Strings are anagrams of each other

Problem Statement: Given two strings, check if two strings are anagrams of 
each other or not.

Examples
Example 1:
Input: CAT, ACT
Output: true
Explanation: Since the count of every letter of both strings are equal.

Example 2:
Input: RULES, LESRT 
Output: false
Explanation: Since the count of U and T  is not equal in both strings.

VALID ANAGRAM — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given two
strings s and t.

I need to determine whether t is an anagram of s.

For them to be anagrams, they must contain exactly the same characters
with exactly the same frequencies, but the order of the characters
doesn't matter."


2. BRUTE FORCE

"The straightforward approach would be to sort both strings and compare
them.

If the sorted strings are equal, they are anagrams.

This would work, but sorting would take O(n log n) time."


3. OPTIMIZE

"We can do better using a hash map to count character frequencies.

I'll count how many times each character appears in s.

Then I'll go through t and subtract those frequencies.

If both strings contain exactly the same characters the same number of
times, every frequency should end at zero."


4. KEY OBSERVATION

"The key observation is that anagrams must have the same character
frequencies.

So I can add frequencies while processing s and subtract frequencies
while processing t.

If t contains a character that wasn't in s, I can immediately return
False.

After processing both strings, every frequency must be zero."


5. APPROACH

"First, I'll check whether the strings have the same length.

If their lengths are different, they cannot be anagrams.

Then I'll create a dictionary called count.

I'll go through s and store the frequency of every character.

Next, I'll go through t.

If the current character exists in the dictionary, I'll subtract one
from its frequency.

If it doesn't exist, I'll immediately return False.

Finally, I'll check all the values in the dictionary.

If any frequency is not zero, the strings are not anagrams.

Otherwise, I'll return True."


6. WHILE CODING

"First, I'm checking the lengths because anagrams must contain the same
number of characters."

if len(s) != len(t):
    return False

"Now I'm building the frequency map for s."

count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

"Now I'm processing t and subtracting from those frequencies."

for char in t:
    if char in count:
        count[char] -= 1
    else:
        return False

"If t contains a character that wasn't present in s, they cannot be
anagrams, so I return False immediately."

"Finally, I'm checking that every character frequency returned to zero."

for value in count.values():
    if value != 0:
        return False

"If all frequencies are zero, the strings are anagrams."

return True


7. EDGE CASES

"If the strings have different lengths, they cannot be anagrams."

if len(s) != len(t):
    return False

"If t contains a character that doesn't exist in s, I'll immediately
return False."

if char not in count:
    return False

"If a character occurs a different number of times, its final frequency
will not be zero."

for value in count.values():
    if value != 0:
        return False

"If both strings are empty, the loops don't run and the function
correctly returns True."


8. COMPLEXITY

"Let n be the length of the strings.

The time complexity is O(n) because I go through s once, t once, and
then check the frequency map.

The space complexity is O(n) in the general case because the dictionary
may contain up to n different characters."
'''
class Solution:
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True
