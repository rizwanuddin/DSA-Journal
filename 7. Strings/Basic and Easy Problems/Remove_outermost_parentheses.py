"""
Remove Outermost Parentheses
Problem Statement: A valid parentheses string is defined by the following rules:
It is the empty string "".
If A is a valid parentheses string, then so is "(" + A + ")".
If A and B are valid parentheses strings, then A + B is also valid.

A primitive valid parentheses string is a non-empty valid string that cannot be split 
into two or more non-empty valid parentheses strings.
Given a valid parentheses string s, your task is to remove the outermost parentheses from
 every primitive component of s and return the resulting string.

Examples
Example 1:
Input:
 s = "((()))"
Output:
 "(())"
Explanation:
 The input string is a single primitive: "((()))".  
Removing the outermost layer yields: "(())".
Example 2:
Input:
 s = "()(()())(())"
Output:
 "()()()"
Explanation:
 Primitive decomposition: "()" + "(()())" + "(())"  
After removing outermost parentheses: "" + "()()" + "()"
Final result: "()()()".



REMOVE OUTERMOST PARENTHESES — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
valid parentheses string made up of one or more primitive parentheses
groups.

For every primitive group, I need to remove its outermost opening and
closing parentheses and return the remaining string."


2. BRUTE FORCE

"The straightforward approach would be to first separate the string
into its primitive groups.

Then for every group, I could remove its first and last parentheses
and combine the results.

This would work, but I don't actually need to create and store all the
primitive groups separately."


3. OPTIMIZE

"I can solve this in one pass by keeping track of the current nesting
depth using a counter.

Whenever I see an opening parenthesis, I increase the depth.

Whenever I see a closing parenthesis, I decrease the depth.

The counter lets me recognize whether a parenthesis is an outermost
one or an inner one."


4. KEY OBSERVATION

"The key observation is that an outermost opening parenthesis is the
one we see when the current count is 0.

So for an opening parenthesis, I check the count BEFORE increasing it.

If count is greater than 0, it is an inner parenthesis, so I keep it.

For a closing parenthesis, I first decrease the count.

If the count becomes 0, that closing parenthesis was the outermost
closing parenthesis, so I don't keep it.

So openings are checked BEFORE changing count, while closings are
checked AFTER changing count."


5. APPROACH

"I'll initialize count to 0 to represent the current nesting depth and
use a list called result to build the answer.

I'll go through every character in the string.

If I find an opening parenthesis, I'll first check whether count is
greater than 0.

If it is, this isn't the outermost opening parenthesis, so I'll add it
to result.

Then I'll increment count.

If I find a closing parenthesis, I'll first decrement count.

Then, if count is still greater than 0, this isn't the outermost closing
parenthesis, so I'll add it to result.

Finally, I'll join the result list into a string and return it."


6. WHILE CODING

"I'm using count to keep track of how deeply nested I currently am."

count = 0

"For an opening parenthesis, I check count before incrementing it.

If count is 0, this is the outermost opening parenthesis, so I skip it.

Otherwise, I keep it."

if char == "(":
    if count > 0:
        result.append(char)
    count += 1

"For a closing parenthesis, I do the opposite order.

I decrement count first."

count -= 1

"If count becomes 0, this was the outermost closing parenthesis, so I
skip it.

If count is still greater than 0, it's an inner closing parenthesis, so
I keep it."

if count > 0:
    result.append(char)


7. EDGE CASES

"If the input is empty, the loop won't execute and joining the empty
result correctly returns an empty string."

result = []
return "".join(result)

"If a primitive is just (), removing its outermost parentheses leaves
nothing, and the current logic handles that automatically."

if char == "(":
    if count > 0:
        result.append(char)

"If the input contains multiple primitive groups, count returns to 0
after each primitive, so the next opening parenthesis is automatically
treated as a new outermost parenthesis."


8. COMPLEXITY

"The time complexity is O(n) because I go through every character in
the string exactly once.

The space complexity is O(n) because the result list can contain up to
O(n) characters."
"""
class Solution:
    def remove_para(self, s):
        count = 0
        result = []
        for char in s:
            if char == "(":
                if count > 0 :
                    result.append(char)
                count += 1
            else:
                count -= 1
                if count > 0 :
                    result.append(char)
        return "".join(result)

"""
REMOVE OUTERMOST PARENTHESES — IDEA

Use a count variable to track how deep we are inside the parentheses.

For "(":
→ If count == 0, it is an outermost opening → SKIP
→ Otherwise, keep it
→ Then increase count

For ")":
→ First decrease count
→ If count == 0, it is an outermost closing → SKIP
→ Otherwise, keep it

Whenever count returns to 0, one primitive has ended.

Time: O(n)
Space: O(n)
"""