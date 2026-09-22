"""
Reverse Words in a String

Problem Statement: Given an input string, containing upper-case and lower-case letters, 
digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The 
words in s are separated by at least one space. Return a string with the words in reverse
order, concatenated by a single space.

Examples
Input: s = "welcome to the jungle"
Output: "jungle the to welcome"
Explanation: The words in the input string are "welcome", "to", "the", and "jungle". 
Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output
string should have exactly one space between each word.

Input: s = " amazing coding skills "
Output: "skills coding amazing"
Explanation: The input string has leading and trailing spaces, as well as multiple spaces
 between the words "amazing", "coding", and "skills". After trimming the leading and 
 trailing spaces and reducing the multiple spaces between words to a single space, the 
 words are "amazing", "coding", and "skills". Reversing the order of these words gives 
 "skills", "coding", and "amazing". The output string should not have any leading or 
 trailing spaces and should have exactly one space between each word.



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
    def reverse_words(self, s):

        result = []
        i = len(s) - 1

        while i >= 0:

            # Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            # No words left
            if i < 0:
                break

            # Save the END of the word
            end = i

            # Move left until we reach a space
            while i >= 0 and s[i] != " ":
                i -= 1

            # Word starts one position after the space
            start = i + 1

            # Pull the whole word from the original string
            word = s[start:end + 1]

            result.append(word)

        return " ".join(result)


s = "welcome to the jungle"

obj = Solution()
print(obj.reverse_words(s))



"""
REVERSE WORDS IN A STRING — IDEA

1. Start from the END of the string.
2. Skip any spaces.
3. Save the end index of the word.
4. Move left until we reach a space.
5. Extract the word using its start/end indexes.
6. Append the word to result.
7. Repeat until the string is finished.
8. Join all words with exactly ONE space.

Extra spaces are ignored.

Example:
"   amazing coding skills "

→ ["skills", "coding", "amazing"]
→ "skills coding amazing"

Time: O(n)
Space: O(n)
"""