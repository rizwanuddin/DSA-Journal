'''
Sort characters by frequency

Problem Statement: You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.
If two or more characters have same frequency then arrange them in alphabetic order.

Examples  
Example 1:
Input:
 s = "tree"
Output:
 ['e', 'r', 't']
Explanation:
e → 2
r → 1
t → 1
Since 'r' and 't' have the same frequency, they are sorted alphabetically → 'r' comes before 't'.

Example 2:
Input:
 s = "raaaajj"
Output:
 ['a', 'j', 'r']
Explanation:
a → 4
j → 2
r → 1
Characters are sorted by decreasing frequency. In case of ties, alphabetically.
            




SORT CHARACTERS BY FREQUENCY — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
string s.

I need to return the unique characters sorted by their frequency.

Characters with a higher frequency should come first.

If two characters have the same frequency, I'll place them in
alphabetical order."


2. BRUTE FORCE

"The straightforward approach would be to take every unique character
and repeatedly scan the entire string to calculate its frequency.

Then I could sort the characters based on those frequencies.

This would work, but repeatedly scanning the string would be
unnecessary."


3. OPTIMIZE

"I can optimize this by using a hash map.

I'll traverse the string once and store the frequency of every
character.

Then I'll sort only the unique characters using the frequencies stored
in the hash map."


4. KEY OBSERVATION

"The key observation is that I need to sort using two conditions.

First, I want higher frequencies to come first.

Second, if two characters have the same frequency, I want alphabetical
order.

So my sorting key will be:

(-freq[char], char)

The negative frequency makes larger frequencies come first, while char
keeps equal-frequency characters in alphabetical order."


5. APPROACH

"First, I'll create a frequency dictionary.

I'll go through the string and count how many times each character
appears.

Then I'll get all the unique characters from the dictionary keys.

I'll sort those characters using their negative frequency first and
the character itself second.

Finally, I'll return the sorted list of unique characters."


6. WHILE CODING

"I'm first creating a frequency map for all the characters."

freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

"Now I'm getting only the unique characters because dictionary keys
already represent each character once."

chars = list(freq.keys())

"Now I'm sorting using two conditions."

chars.sort(key=lambda char: (-freq[char], char))

"The negative frequency gives me descending frequency order.

The character itself gives me alphabetical order when two frequencies
are equal."

"Finally, I'll return the sorted characters."

return chars


7. EDGE CASES

"If the string is empty, the frequency dictionary and chars list will
both remain empty, so the function correctly returns an empty list."

freq = {}
chars = list(freq.keys())

"If the string contains only one unique character, the list will contain
just that character and sorting still works normally."

"If multiple characters have the same frequency, this part of the
sorting key handles the tie alphabetically."

chars.sort(key=lambda char: (-freq[char], char))


8. COMPLEXITY

"Let n be the length of the string and k be the number of unique
characters.

Building the frequency map takes O(n).

Sorting the k unique characters takes O(k log k).

So the total time complexity is O(n + k log k).

The space complexity is O(k) because I store the frequency map and the
list of unique characters."
'''
class Solution:
    def frequency_sort(self, s):

        # Count frequency of each character
        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Get all unique characters
        chars = list(freq.keys())

        # Sort by:
        # 1. Higher frequency first
        # 2. Alphabetical order if frequency is same
        chars.sort(key=lambda char: (-freq[char], char))

        return chars


if __name__ == "__main__":

    s = "tree"

    sol = Solution()

    result = sol.frequency_sort(s)

    print(result)




"""
chars.sort(key=lambda char: (-freq[char], char))

key=
→ Tells Python WHAT rule to sort by.

lambda char:
→ A small temporary function applied to each character.

-freq[char]
→ Sorts frequency from HIGHEST to LOWEST.
→ Negative is used because Python normally sorts smallest to largest.

char
→ If two characters have the same frequency,
  sort them alphabetically.

Example:

e → (-2, 'e')
r → (-1, 'r')
t → (-1, 't')

Result → ['e', 'r', 't']
"""