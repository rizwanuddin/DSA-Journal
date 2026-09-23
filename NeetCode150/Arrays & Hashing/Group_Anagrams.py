"""
Group Anagrams - Explanation

Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.An anagram is a string that contains 
the exact same characters as another string, but the order of the 
characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]




# GROUP ANAGRAMS — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given an array of
strings, and I need to group all the anagrams together into
sublists. I can return the groups in any order."

## 2. BRUTE FORCE

"The brute-force way is to compare every word against every other
word to check if they're anagrams, similar to the Valid Anagram
problem. That's O(n^2) comparisons, and each comparison itself costs
time to check, so it's expensive."

## 3. OPTIMIZE

"I can do better by giving every word a 'signature' — if I sort a
word's letters, every anagram of that word produces the exact same
sorted result. So instead of comparing words to each other, I can
group words that share the same signature using a hashmap."

## 4. KEY OBSERVATION

"Two words are anagrams if and only if sorting their letters gives
the same result. So I don't need to compare words directly — I just
need to compute each word's sorted signature and use that as a
grouping key."

## 5. APPROACH

"I'll create an empty dictionary called groups, where the key is a
sorted signature and the value is a list of original words that
share it.

For each word in the input, I'll sort its letters and join them back
into a string to get its signature.

If that signature isn't a key in groups yet, I'll create a new empty
list for it.

Either way, I'll append the original word to that signature's list.

At the end, I'll return just the lists of grouped words, dropping the
signature keys."

## 6. WHILE CODING

"First, I create a dictionary to hold my groups."

groups = {}

"I loop through every word in the input."

for word in strs:

"For each word, I sort its letters and join them into a string —
that's the signature."

    key = "".join(sorted(word))

"If I haven't seen this signature before, I start a new empty list
for it."

    if key not in groups:
        groups[key] = []

"Either way, I add the original word into that signature's list."

    groups[key].append(word)

"At the end, I return just the grouped lists, not the signature
keys."

return list(groups.values())

## 7. EDGE CASES

"If the input has just one word, it ends up alone in its own group,
since nothing else shares its signature."

"If the input contains an empty string, sorting it gives an empty
signature too, so all empty strings correctly group together."

"If no two words are anagrams of each other, every word just ends up
in its own separate group, which is still a valid grouping."

## 8. COMPLEXITY

"For time complexity, I sort each word, and sorting a word of length
k costs O(k log k). If there are n words, and the average word length
is k, the total time is O(n * k log k).

For space complexity, I'm storing every word in the dictionary, so
that's O(n * k) in the worst case, to hold all the words across all
the groups."
"""
class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())