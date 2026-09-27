"""
Valid Parentheses - Explanation

You are given a string s consisting of the following characters: 
'(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the 
    same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.




## Valid Parentheses

**Clarify:**
- String contains only (), {}, []
- Valid means: every open bracket matches its corresponding close bracket, AND they close in the correct nested order

**Brute force:**
- Could try repeatedly removing matched adjacent pairs like "()" or "[]" until nothing changes, check if string is empty
- Messy, inefficient, hard to reason about correctness

**Optimize:**
- Stack — last opened bracket must be the first one closed, which is exactly LIFO behavior
- O(n) time, single pass

**Key observation:**
- Every time you see a closing bracket, it MUST match whatever open bracket is currently on top of the stack — if it doesn't, the order is wrong
- A stack naturally enforces "most recent unclosed thing gets checked first," which is exactly what "correct order" means here

**Approach:**
- stack = [], matching = dict mapping each closing bracket to its correct opening bracket
- for each character:
  - if it's an opening bracket: push it onto the stack
  - if it's a closing bracket:
    - if stack is empty: invalid, nothing to match against
    - if top of stack isn't the matching open bracket: invalid
    - otherwise: pop the stack (that pair is now resolved)
- after the loop: valid only if the stack is completely empty (nothing left unclosed)

**While coding:**
- Check `if not stack` BEFORE checking `stack[-1]` — trying to peek an empty stack would crash
- Final check `len(stack) == 0` matters — a string like "(((" would pass every character check but leave unclosed brackets behind

**Edge cases:**
- Empty string → valid (stack stays empty, trivially true)
- Only opening brackets → stack never empties, returns False
- Only closing brackets → first character immediately fails the empty-stack check

**Complexity:**
- Time: O(n) — one pass through the string
- Space: O(n) — worst case, all characters are opening brackets and go onto the stack
"""
class Solution:
    def isValid(self, s):
        stack = []
        matching = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != matching[char]:
                    return False
                stack.pop()
        return len(stack) == 0

"""
Opening bracket → PUSH

Closing bracket:
→ stack empty? FALSE
→ top doesn't match? FALSE
→ otherwise POP

End:
stack empty → TRUE
stack not empty → FALSE
"""