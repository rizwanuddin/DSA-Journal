"""
Longest Substring Without Repeating Characters - Explanation

Given a string s, find the length of the longest substring without 
duplicate characters.A substring is a contiguous sequence of 
characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1




## Longest Substring Without Repeating Characters

**Clarify:**
- Find the length of the longest substring (contiguous) with no repeated characters
- Return just the length, not the substring itself

**Brute force:**
- Check every possible substring, verify no duplicates, track the max length
- O(n³) or O(n²) depending on how duplicate-checking is done — slow

**Optimize:**
- Sliding window with a set — expand right, shrink left only when a duplicate shows up
- O(n) time

**Key observation:**
- A repeat only matters if it's INSIDE the current window — once a character leaves the window (because left moved past it), it's no longer a conflict
- Since left only ever moves forward, you don't need to search the whole window to find the duplicate — just keep removing from the left, one at a time, until the duplicate itself is gone

**Approach:**
- left = 0, window = empty set, max_len = 0
- for right in range(len(s)):
  - while s[right] is already in window: remove s[left] from window, move left forward
  - add s[right] to window
  - update max_len with right - left + 1

**While coding:**
- The while loop (not if) matters — one removal might not clear the duplicate if it's deeper inside the window, so keep checking after every removal
- right - left + 1 because both pointers are included in the current valid window

**Edge cases:**
- Empty string → loop never runs, max_len stays 0
- All identical characters (e.g. "xxxx") → window shrinks to size 1 every time, max_len = 1
- All unique characters → window never shrinks, max_len = len(s)

**Complexity:**
- Time: O(n) — left and right each move forward at most n times total, never backward
- Space: O(min(n, charset size)) — window holds at most one of each unique character
"""
class Solution:
    def longset_substring(self, s):
        left = 0
        window = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len