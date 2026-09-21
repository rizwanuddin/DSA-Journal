"""
Generate Parentheses

Given an integer n.Generate all possible combinations of well-formed 
parentheses of length 2 x N.

Example 1:
Input : n = 3
Output : [ "((()))" , "(()())" , "(())()" , "()(())" , "()()()" ]

Example 2:
Input : 2
Output : [ "(())" , "()()" ]




GENERATE PARENTHESES — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given n
pairs of parentheses.

I need to generate every possible combination of n opening and n
closing parentheses that forms a valid parentheses string."


2. BRUTE FORCE

"The brute-force approach would be to generate every possible string of
length 2 * n using '(' and ')'.

Then I could check each generated string to see whether it is valid.

This would work, but it generates many invalid combinations that I
already know I don't need."


3. OPTIMIZE

"We can optimize this using backtracking.

Instead of generating invalid strings and checking them afterward, I'll
only make choices that can still lead to a valid parentheses string.

I'll keep track of how many opening and closing parentheses I've used."


4. KEY OBSERVATION

"There are two rules that determine whether I can add a parenthesis.

I can add '(' as long as I haven't already used all n opening
parentheses.

So:

open_count < n

I can add ')' only when there are more opening parentheses than closing
parentheses already in my current string.

So:

close_count < open_count

That second rule prevents me from ever creating an invalid prefix like:

())

because I can never close more parentheses than I've opened."


5. APPROACH

"I'll create a backtracking function that keeps track of three things:

current      → the string I'm currently building
open_count   → how many '(' I've used
close_count  → how many ')' I've used

At every recursive call, I'll have up to two choices.

If open_count is less than n, I can add an opening parenthesis and
continue recursively.

If close_count is less than open_count, I can add a closing parenthesis
and continue recursively.

My base case is when the current string reaches length 2 * n.

At that point I've used all n pairs, and because I only allowed valid
choices along the way, the string is valid, so I'll add it to result."


6. WHILE CODING

"I'm creating result to store all of the valid combinations."

result = []

"My recursive function keeps track of the current string and how many
opening and closing parentheses I've used."

def backtrack(current, open_count, close_count):

"My base case is when the string reaches the required length of 2 * n."

if len(current) == 2 * n:
    result.append(current)

"If I still have opening parentheses available, I can choose to add
one."

if open_count < n:
    backtrack(current + "(", open_count + 1, close_count)

"I can only add a closing parenthesis if I currently have an unmatched
opening parenthesis available to close."

if close_count < open_count:
    backtrack(current + ")", open_count, close_count + 1)

"Finally, I'll start with an empty string and zero opening and closing
parentheses."

backtrack("", 0, 0)


7. EDGE CASES

"If n is 0, the initial current string already has length 2 * n, so the
current code adds the empty string to the result."

if len(current) == 2 * n:
    result.append(current)

"If the problem instead expects an empty list for n = 0, I could handle
that separately."

if n == 0:
    return []

"I never allow more than n opening parentheses."

if open_count < n:
    ...

"I also never allow the number of closing parentheses to become greater
than the number of opening parentheses."

if close_count < open_count:
    ...

"Those two conditions prevent invalid combinations from being generated
in the first place."


8. COMPLEXITY

"The number of valid combinations is the nth Catalan number.

So the algorithm generates about Cn valid combinations, and each
combination has length 2 * n.

The time complexity is O(Cn * n).

The recursion depth is O(n), so the auxiliary space complexity is O(n),
not counting the result list.

The result itself requires O(Cn * n) space because we have to store all
of the generated strings."
"""
class Solution:
    def generate_parenthesis(self, n):
        result = []
        def backtrack(current, open_count, close_count):
            # Base case: used all n pairs
            if len(current) == 2 * n:
                result.append(current)
            # Choice 1: add "("
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            # Choice 2: add ")"
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        backtrack("", 0, 0)
        return result