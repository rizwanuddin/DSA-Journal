"""
Valid Palindrome - Explanation

Given a string s, return true if it is a palindrome, otherwise 
return false.A palindrome is a string that reads the same forward 
and backward. It is also case-insensitive and ignores all 
non-alphanumeric characters.Note: Alphanumeric characters consist 
of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we 
have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false




## Valid Palindrome

**Clarify:**
- Check if a string is a palindrome, considering only alphanumeric characters
- Ignore case — treat uppercase and lowercase as the same
- Empty string / all-non-alphanumeric string counts as a valid palindrome

**Brute force:**
- Build a new string with only lowercase alphanumeric chars, then compare it to its reverse
- Works, but uses O(n) extra space for the cleaned string

**Optimize:**
- We don't need to build a new string at all
- Two pointers, one from each end, moving inward — skip non-alphanumeric chars as we go, compare in place
- This gets us O(1) space instead of O(n)

**Key observation:**
- A palindrome reads the same forwards and backwards, so comparing from both ends inward is the natural structure
- Non-alphanumeric chars (spaces, punctuation) just get skipped — they don't count toward the comparison at all
- Case doesn't matter, so lowercase both chars before comparing

**Approach:**
- left = 0, right = len(s) - 1
- Loop while left < right:
  - Skip left forward while s[left] isn't alphanumeric
  - Skip right backward while s[right] isn't alphanumeric
  - Compare s[left].lower() == s[right].lower() — if not equal, return False
  - Move both pointers inward

**While coding:**
- The inner skip-loops each need their own `left < right` bounds check, or you risk indexing out of range if the string is all punctuation
- `and` short-circuits, so bounds check must come before the isalnum() check in the while condition
- Use isalnum() to test "is this a letter or digit", lower() to normalize case

**Edge cases:**
- Empty string → loop never runs → returns True
- String with only punctuation/spaces → both pointers skip all the way through → loop ends → returns True
- Single character → left == right immediately → loop never runs → returns True

**Complexity:**
- Time: O(n) — each pointer moves inward at most n/2 times total
- Space: O(1) — no extra string built, just two pointers
"""
class Solution:
    def isPalindrome(self, s):
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            while left < right and not s[left].isalnum:
                left += 1
            while left < right and not s[right].isalnum:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True