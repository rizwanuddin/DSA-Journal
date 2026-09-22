"""
Check if one string is rotation of another

Problem Statement: Given two strings s and goal, return true if and only if s can become goal 
after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position. For 
example, if s = "abcde", then it will be "bcdea" after one shift.

Examples       
Example 1:
Input:
 s = "rotation", goal = "tionrota"
Output:
 true
Explanation:
 After multiple left shifts on "rotation", we get:
    1st shift → "otationr"
    2nd shift → "tationro"
    3rd shift → "ationrot"
    4th shift → "tionrota"
    So the goal string can be obtained by rotating the original string.

Example 2:
Input:
 s = "hello", goal = "lohelx"
Output:
 false
Explanation:
Even after all possible rotations of "hello", we cannot form "lohelx" due to the presence of an 
extra character 'x'. Hence, it's not possible.
            

ROTATE STRING — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given two
strings, s and goal.

I need to determine whether I can repeatedly move the first character
of s to the end and eventually make s equal to goal.

If I can, I'll return True. Otherwise, I'll return False."


2. BRUTE FORCE

"The straightforward approach would be to actually rotate s one
position at a time.

After every rotation, I could compare the new string with goal.

This would work, but I may perform up to n rotations, and each string
comparison can take O(n), giving O(n^2) time."


3. OPTIMIZE

"We can avoid manually creating every rotation.

If I concatenate s with itself, the doubled string contains every
possible rotation of s as a substring.

So I only need to check whether goal exists inside s + s."


4. KEY OBSERVATION

"The key observation is that every rotation of s appears inside s
concatenated with itself.

So if goal has the same length as s and goal appears inside s + s,
then goal must be a valid rotation of s.

The length check is important because otherwise a different-length
substring could incorrectly pass the containment check."


5. APPROACH

"First, I'll check whether s and goal have the same length.

If they don't, I'll immediately return False because rotation never
changes the length of a string.

Then I'll create a doubled version of s by concatenating it with itself.

Finally, I'll check whether goal appears inside that doubled string.

If it does, I'll return True. Otherwise, I'll return False."


6. WHILE CODING

"First, I'm checking the lengths because rotating a string never changes
its number of characters."

if len(s) != len(goal):
    return False

"Now I'm doubling s because this contains all possible rotations of s."

s_double = s * 2

"Finally, I'm checking whether goal appears inside the doubled string."

if goal in s_double:
    return True
else:
    return False


7. EDGE CASES

"If the strings have different lengths, they can never be rotations of
each other."

if len(s) != len(goal):
    return False

"If both strings are empty, their lengths are equal and goal is found
inside the doubled empty string, so the function correctly returns
True."

"If s and goal are already equal, goal will naturally appear inside
s_double, so the same logic handles it."

if goal in s_double:
    return True


8. COMPLEXITY

"Creating s_double takes O(n) time and O(n) extra space.

The substring search depends on the underlying string-search
implementation, but with an efficient substring search it can be O(n)
time.

So we typically describe the overall time complexity as O(n) and the
space complexity as O(n) because of the doubled string."
"""
class Solution:
    def rotate_string(self, s, goal):
        if len(s) != len(goal):
            return False
        s_double = s * 2
        if goal in s_double:
            return True
        else:
            return False