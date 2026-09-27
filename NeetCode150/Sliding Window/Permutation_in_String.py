"""
Permutation In String - Explanation

You are given two strings s1 and s2.Return true if s2 contains a 
permutation of s1, or false otherwise. That means if a permutation 
of s1 exists as a substring of s2, then return true.Both strings 
only contain lowercase letters.

Example 1:
Input: s1 = "abc", s2 = "lecabee"
Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:
Input: s1 = "abc", s2 = "lecaabee"
Output: false


## Permutation In String

**Clarify:**
- Return True if any contiguous substring of s2 is a permutation of s1 (same letters, same counts, any order)
- Both strings are lowercase only

**Brute force:**
- Check every substring of s2 with length len(s1), sort both and compare, or build frequency counts and compare
- O(n * m log m) if sorting each window, or O(n * 26) if using frequency counts freshly each time — still redoing work every slide

**Optimize:**
- Fixed-size sliding window (size = len(s1)) across s2
- Maintain a running frequency count for the window — update it incrementally instead of rebuilding from scratch every slide
- O(n) time

**Key observation:**
- A permutation of s1 must be EXACTLY len(s1) characters long — so the window size never changes, it just slides
- Comparing frequency counts of two windows of the same fixed length automatically guarantees contiguity — no separate check needed, since a window is always a real consecutive slice
- Sliding means: remove the character leaving on the left, add the character entering on the right — no need to recompute the whole window's count from scratch each time

**Approach:**
- If len(s1) > len(s2): return False immediately, impossible
- Build s1_count = frequency dict of s1
- Build window_count = frequency dict of the first len(s1) characters of s2
- If they match: return True
- Slide window one step at a time from there:
  - remove s2[left] from window_count, left moves forward
  - add s2[right] to window_count, right moves forward
  - compare window_count to s1_count each time, return True if equal
- If loop finishes with no match: return False

**While coding:**
- Use Counter from collections, or a plain dict with get() — either works for building/comparing frequency counts
- Compare dicts directly with == — Python compares dict equality by key/value pairs automatically
- Window must always start sliding right after the FIRST full window is already built and checked

**Edge cases:**
- len(s1) > len(s2): impossible, return False right away
- s1 and s2 identical: window immediately matches on the first check
- No permutation exists anywhere: loop runs fully, returns False

**Complexity:**
- Time: O(n) where n = len(s2) — window slides one step at a time, O(1) work per slide (26-letter alphabet means dict comparison is effectively constant time)
- Space: O(1) — frequency dicts hold at most 26 keys (lowercase letters)
"""
from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])

        if window_count == s1_count:
            return True

        left = 0
        for right in range(len1, len2):
            window_count[s2[right]] += 1
            left_char = s2[left]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            left += 1

            if window_count == s1_count:
                return True

        return False

        