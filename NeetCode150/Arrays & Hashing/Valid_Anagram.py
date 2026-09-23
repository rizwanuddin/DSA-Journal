"""
Valid Anagram - Explanation

Given two strings s and t, return true if the two strings are anagrams of 
each other, otherwise return false.Two strings are anagrams if they contain
the same characters, with each character appearing the same number of 
times, regardless of order.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false



# VALID ANAGRAM — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given two strings, s
and t, and I need to return True if they're anagrams — same
characters, same counts, just possibly in a different order —
otherwise False."

## 2. BRUTE FORCE

"The brute-force way is to sort both strings and compare them
directly. If they're anagrams, sorting puts both into the same order,
so they'd be equal. That's O(n log n) because of the sort."

## 3. OPTIMIZE

"I can do better with a frequency count instead of sorting. If I count
how many times each character appears in s, then subtract using t,
everything should cancel out to zero if they're anagrams. That's
O(n) instead of O(n log n)."

## 4. KEY OBSERVATION

"First, if the lengths of s and t are different, they can't possibly
be anagrams, so I can return False immediately without doing any
counting.

Otherwise, I build a frequency map from s, then walk through t and
decrement. Two things can go wrong while decrementing: t might have a
character that never appeared in s at all, or a character's count
might go negative, meaning t used it more times than s did. Either
one means it's not an anagram."

## 5. APPROACH

"First, I'll check if the lengths match. If not, return False right
away.

Then I'll build a frequency dictionary counting every character in s.

Then I'll loop through t. For each character, I'll check if it exists
in my frequency map. If it doesn't, return False.

If it does exist, I'll decrement its count. If that count drops below
zero, return False.

If I get through the whole loop without any of that happening, I
return True."

## 6. WHILE CODING

"First, I check if the lengths are different, since that's a free way
to rule out non-anagrams early."

if len(s) != len(t):
    return False

"Now I build a frequency count of every character in s."

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

"Now I go through t and decrement using the same map."

for char in t:

"First I check if this character even exists in my map."

    if char not in freq:
        return False

"If it exists, I decrement its count."

    freq[char] -= 1

"If the count goes negative, t used this character more times than s
did, so it's not an anagram."

    if freq[char] < 0:
        return False

"If I make it through the whole loop with no issues, everything
matched up, so I return True."

return True

## 7. EDGE CASES

"If both strings are empty, the length check passes since 0 equals 0,
and both loops just don't run, so I correctly return True."

"If s and t are identical strings, every count decrements back to
exactly zero, so I return True."

"If t has a character not in s, my 'char not in freq' check catches
that immediately."

## 8. COMPLEXITY

"Time complexity is O(n), since I make one pass to build the
frequency map and one pass to decrement it.

Space complexity is O(n) in the worst case, if every character in s
is unique, since that gives me n entries in the frequency map."
"""
class Solution:
    def isAnagram(self, s, t):

        # Different lengths can never be anagrams
        if len(s) != len(t):
            return False

        freq = {}

        # Count frequency of each character in s
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Decrement frequency using characters in t
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1
            if freq[char] < 0:
                return False

        return True

"""
Can you use sorting for Valid Anagram like how we did in group anagrams? 
Yes.
Two strings are anagrams exactly when their sorted letters are identical, 
so sorted(s) == sorted(t) is a completely valid check.

Why you might still prefer the hashmap version:
Sorting costs O(n log n)
Hashmap frequency count costs O(n)
Same correctness, hashmap is just asymptotically faster
"""
        