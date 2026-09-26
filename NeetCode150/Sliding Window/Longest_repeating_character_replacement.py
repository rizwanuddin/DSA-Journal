"""
Longest Repeating Character Replacement - Explanation

You are given a string s consisting of only uppercase english 
characters and an integer k. You can choose up to k characters of 
the string and replace them with any other uppercase English 
character.After performing at most k replacements, return the 
length of the longest substring which contains only one distinct 
character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 
'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5




## Longest Repeating Character Replacement

**Clarify:**
- String of uppercase letters, can replace up to k characters (with anything)
- Return the length of the longest substring that could become all-one-character after at most k replacements

**Brute force:**
- Check every substring, count replacements needed (size - most frequent char count), track max valid length
- O(n²) or worse — slow

**Optimize:**
- Sliding window: grow right, track character counts and the highest frequency seen so far (max_freq)
- Window is valid if (window size - max_freq) <= k — that's how many chars would need replacing
- Shrink from left only when invalid
- O(n) time

**Key observation:**
- We never need max_freq to shrink back down when the window shrinks — it can stay "stale" (too high) and still be correct
- Why: we only care about the LONGEST valid window ever found. A stale max_freq only makes the validity check stricter, so it can never falsely report a bigger answer than what's truly achievable — it just makes the window wait until some character's count genuinely catches back up before growing past the previous best

**Approach:**
- left = 0, count = {}, max_freq = 0, max_len = 0
- for right in range(len(s)):
  - count[s[right]] += 1
  - max_freq = max(max_freq, count[s[right]])
  - while (right - left + 1) - max_freq > k: shrink — remove s[left] from count, move left forward
  - max_len = max(max_len, right - left + 1)

**While coding:**
- Update count and max_freq FIRST, then check validity, then shrink if needed — order matters
- Don't recompute max_freq downward after shrinking — leaving it stale is intentional and safe
- window size uses right - left + 1 since both pointers are included

**Edge cases:**
- Empty string → max_len stays 0
- k >= len(s) → entire string can be replaced, max_len = len(s)
- All identical characters → window never needs to shrink, max_len = len(s)

**Complexity:**
- Time: O(n) — left and right each move forward at most n times total
- Space: O(1) — count dict holds at most 26 uppercase letters
"""
class Solution:
    def characterReplacement(self, s, k):
        left = 0
        count = {}
        max_freq = 0
        max_len = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len 