'''
Problem Statement: Given two strings s and t, determine if they are isomorphic. Two strings s and 
t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order 
of characters. No two characters may map to the same character, but a character may map to itself.

Examples
Example 1
Input:
 s = "paper", t = "title"
Output:
 true
Explanation:
 The characters in "s" can be mapped one-to-one to characters in "t": 
'p' → 't', 'a' → 'i', 'e' → 'l', 'r' → 'e'
Since the mapping is consistent and unique for each character, the strings are isomorphic.

Example 2
Input:
 s = "foo", t = "bar"
Output:
 false
Explanation:
 'f' → 'b' is fine, 'o' → 'a' for the first 'o', But the second 'o' in "s" would need to map to 
 'r' in "t", which conflicts with the earlier mapping of 'o' → 'a'
This inconsistency makes it impossible to convert "s" to "t" using a one-to-one character mapping.
            


ISOMORPHIC STRINGS — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given two
strings s and t.

I need to determine whether the characters in s can be consistently
mapped to the characters in t.

Each character in s must always map to the same character in t, and
two different characters cannot map to the same character.

If the strings are isomorphic, I'll return True. Otherwise, I'll return
False."


2. BRUTE FORCE

"The straightforward approach would be to repeatedly compare character
patterns and search through the strings to make sure every mapping is
consistent.

This could require repeatedly scanning the strings.

Instead, I can store the mappings as I process the characters."


3. OPTIMIZE

"I can use two hash maps to store the character mappings.

The first map stores mappings from s to t.

The second map stores mappings from t back to s.

Using both directions makes sure the mapping is one-to-one."


4. KEY OBSERVATION

"The key observation is that I need to check the mapping in BOTH
directions.

For example, if a character in s was already mapped to something, it
must map to that same character every time.

But I also need to make sure that two different characters from s
don't map to the same character in t.

That's why I use:

mapST → s to t
mapTS → t to s

Both mappings must stay consistent."


5. APPROACH

"First, I'll check whether the strings have the same length. If they
don't, they cannot be isomorphic.

Then I'll create two dictionaries.

I'll go through both strings together using zip, so charS and charT
represent characters at the same position.

For the s to t mapping, if charS already exists in mapST, I'll check
whether it maps to charT.

If it maps to something different, I'll return False.

Otherwise, if charS hasn't been seen before, I'll create the mapping.

Then I'll do the same check in the opposite direction using mapTS.

If I finish processing every character without finding an invalid
mapping, I'll return True."


6. WHILE CODING

"First, I'm checking that both strings have the same length."

if len(s) != len(t):
    return False

"I'm creating two dictionaries because I need to guarantee a one-to-one
mapping in both directions."

mapST = {}
mapTS = {}

"I'm using zip to process the characters at the same position in both
strings."

for charS, charT in zip(s, t):

"First, I'm checking the mapping from s to t.

If charS has already been seen, it must still map to charT."

if charS in mapST:
    if mapST[charS] != charT:
        return False
else:
    mapST[charS] = charT

"Now I'm checking the reverse mapping.

If charT has already been seen, it must still map back to charS."

if charT in mapTS:
    if mapTS[charT] != charS:
        return False
else:
    mapTS[charT] = charS

"If every mapping stays consistent, the strings are isomorphic."

return True


7. EDGE CASES

"If the strings have different lengths, they cannot be isomorphic."

if len(s) != len(t):
    return False

"If one character tries to map to two different characters, the first
dictionary catches it."

if charS in mapST:
    if mapST[charS] != charT:
        return False

"If two different characters try to map to the same character, the
reverse dictionary catches it."

if charT in mapTS:
    if mapTS[charT] != charS:
        return False

"If both strings are empty, the loop doesn't run and the function
correctly returns True."


8. COMPLEXITY

"The time complexity is O(n) because I go through both strings once,
and dictionary lookups and insertions take O(1) average time.

The space complexity is O(n) in the general case because the two hash
maps may store mappings for the characters in the strings."
'''

class Solution:
    def is_isomorphic(self, s, t):

        if len(s) != len(t):
            return False

        mapST = {}
        mapTS = {}

        for charS, charT in zip(s, t):

            # Check s -> t mapping
            if charS in mapST:
                if mapST[charS] != charT:
                    return False
            else:
                mapST[charS] = charT

            # Check t -> s mapping
            if charT in mapTS:
                if mapTS[charT] != charS:
                    return False
            else:
                mapTS[charT] = charS

        return True


# Driver code
s = "paper"
t = "title"

obj = Solution()
print(obj.is_isomorphic(s, t))
        








'''
-----------------
 for i in range(len(s)): .....can do this way but there's a cleaner version 
    charS = s[i]
    charT = t[i]
----------------
For each pair s[i], t[i]:

1. If s[i] already has a mapping:
   → it MUST equal t[i]
   → otherwise False

2. If t[i] is already mapped from another character:
   → it MUST map back to s[i]
   → otherwise False

3. Otherwise:
   → store both mappings

If we finish everything:
→ True
'''