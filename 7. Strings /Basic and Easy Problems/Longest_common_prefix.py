"""
Longest Common Prefix
Problem Statement: Write a function to find the longest common prefix string amongst an 
array of strings. If there is no common prefix, return an empty string "".

Examples
Example 1
Input:
 str = ["flower", "flow", "flight"]
Output:
 "fl"
Explanation:
 All strings in the array begin with the common prefix "fl".

Example 2
Input:
 str = ["apple", "banana", "grape", "mango"]
Output:
 ""
Explanation:
 None of the strings share a common starting sequence, so the result is an empty string.
            
"""
class Solution:
    def longest_common_prefix(self, words):

        shortest = min(len(word) for word in words)

        for i in range(shortest):

            # Character from the first word at index i
            char = words[0][i]

            # Go through every word
            for word in words:

                if word[i] != char:
                    return words[0][:i]

        return words[0][:shortest]




"""
LONGEST COMMON PREFIX — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array of strings.

I need to find the longest prefix that is common to every string.

If the strings don't share any common prefix, I'll return an empty
string."


2. BRUTE FORCE

"The straightforward approach would be to start with the first word as
the prefix and keep shortening it until it matches the beginning of
every other word.

This would work, but I can solve it more directly by comparing the
characters at each position across all the words."


3. OPTIMIZE

"I'll first find the length of the shortest word.

The common prefix can never be longer than the shortest word, so I only
need to check characters up to that length.

Then I'll compare the characters at each index across every word."


4. KEY OBSERVATION

"The key observation is that for an index to be part of the common
prefix, every word must have the same character at that index.

So I'll take the character from the first word at index i and compare
it with the character at index i in every other word.

The moment I find a mismatch, I know the common prefix ends right
before that position."


5. APPROACH

"First, I'll find the length of the shortest word.

Then I'll loop from index 0 up to that length.

For each index, I'll take the character from the first word.

Then I'll go through every word and compare its character at that same
index.

If any character is different, I'll immediately return the part of the
first word before that index.

If I finish checking every position without finding a mismatch, then
the entire shortest length is common, so I'll return that prefix."


6. WHILE CODING

"I'm first finding the shortest word length because I never need to
check beyond it."

shortest = min(len(word) for word in words)

"Now I'm checking each character position up to that length."

for i in range(shortest):

"I'm using the first word's character as the character that every other
word needs to match."

char = words[0][i]

"Now I'm comparing that position across every word."

for word in words:
    if word[i] != char:

"If I find a mismatch, the common prefix ends before index i, so I
return everything from the beginning up to i."

return words[0][:i]

"If I never find a mismatch, the common prefix is the entire shortest
length."

return words[0][:shortest]


7. EDGE CASES

"If the words list could be empty, I need to handle that before finding
the minimum length."

if not words:
    return ""

"If one of the words is empty, shortest becomes 0, so the loop doesn't
run and I correctly return an empty prefix."

shortest = min(len(word) for word in words)

"If the very first characters are different, i will be 0 and this
correctly returns an empty string."

return words[0][:0]

"If there is only one word, every character of that word is naturally
part of the common prefix, so the normal logic returns the entire word."


8. COMPLEXITY

"Let n be the number of words and L be the length of the shortest word.

In the worst case, I compare L character positions across all n words.

So the time complexity is O(n * L).

The extra space complexity is O(1) because I only use a few variables,
not counting the returned substring."
"""