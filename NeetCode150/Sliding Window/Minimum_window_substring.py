"""
Minimum Window Substring - Explanation

Given two strings s and t, return the shortest substring of s such 
that every character in t, including duplicates, is present in the 
substring. If such a substring does not exist, return an empty 
string "".You may assume that the correct output is always unique.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3:
Input: s = "x", t = "xy"
Output: ""




## Minimum Window Substring

**Clarify:**
- Find the shortest contiguous substring of s that contains every character of t, including duplicate counts
- Order doesn't matter, just needs to include enough of each required character
- Return "" if no such substring exists; assume the correct answer is unique

**Brute force:**
- Check every possible substring of s, verify it contains all of t's characters with correct counts, track the shortest valid one
- O(n²) or worse — very slow, lots of repeated counting

**Optimize:**
- Sliding window where BOTH pointers move independently: right grows until valid, left shrinks while staying valid
- Track validity with a "matched" counter instead of rescanning the whole count dict every time
- O(n) time

**Key observation:**
- Once the window is valid (contains enough of everything needed), shrinking it can only help — you want the smallest valid window, so shrink as far as possible before it breaks
- "matched" tracks how many DISTINCT required characters currently have enough count in the window — not total letters, not every character in s
- matched increases when a character's window count reaches exactly what's needed; matched decreases when a character's count drops below what's needed during shrinking
- Window is fully valid exactly when matched == number of distinct characters required

**Approach:**
- need = frequency dict of t, required = number of distinct chars in need
- window = {}, matched = 0, left = 0, best_len = infinity, best_left = 0
- for right in range(len(s)):
  - add s[right] to window
  - if that character is needed and window count just reached the needed amount: matched += 1
  - while matched == required (window is valid):
    - check if this window is smaller than best found so far, update if so
    - remove s[left] from window
    - if that character is needed and its count just dropped below needed: matched -= 1
    - left += 1
- return the smallest valid window found, or "" if none was ever found

**While coding:**
- Only increment/decrement matched at the EXACT moment a requirement is newly satisfied or newly broken — not on every single add/remove
- The while loop (not if) for shrinking matters — keep shrinking as long as it's still valid, don't stop after one step
- best_len starts at infinity so the very first valid window always updates it

**Edge cases:**
- t longer than s → impossible, but the algorithm naturally returns "" since matched never reaches required
- s == t → whole string is the answer
- t has duplicate characters → need dict naturally handles this since it stores counts, not just presence

**Complexity:**
- Time: O(n) — right moves forward n times total, left moves forward at most n times total across the whole run (never backward)
- Space: O(k) where k = number of distinct characters in t and s combined — small if limited to letters
"""
class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        window = {}
        matched = 0
        required = len(need)

        left = 0
        best_len = float("inf")
        best_left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                matched += 1

            while matched == required:
                if (right - left + 1) < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    matched -= 1
                left += 1
            return "" if best_len == float("inf") else s[best_left:best_left+best_len]