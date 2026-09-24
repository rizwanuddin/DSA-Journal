"""
Encode and Decode Strings - Explanation

Design an algorithm to encode a list of strings to a string. The 
encoded string is then sent over the network and is decoded back 
to the original list of strings.

Machine 1 (sender) has the function:
String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}

Machine 2 (receiver) has the function:
List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}

So Machine 1 does:
String encoded_string = encode(strs);

and Machine 2 does:
List<String> decoded_strs = decode(encoded_string);
decoded_strs in Machine 2 should be the same as the input strs in 
Machine 1.Implement the encode and decode methods.

Example 1:
Input: strs = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2
List<String> decoded_strs = solution.decode(encoded_string);

Example 2:
Input: strs = [""]
Output: [""]




# ENCODE AND DECODE STRINGS — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I need to design two
functions: encode, which takes a list of strings and turns it into
one single string, and decode, which takes that encoded string and
perfectly reconstructs the original list."

## 2. BRUTE FORCE

"The naive idea is to join all the strings together using some
separator character, like a comma. But that breaks if any of the
original strings contain that separator character themselves, since
decoding wouldn't be able to tell a real separator apart from one
that's part of the actual content."

## 3. OPTIMIZE

"Instead of relying on a separator character that could accidentally
appear inside a string, I can use length-prefixing. For each word, I
store its length before the word itself, so decoding knows exactly
how many characters to read, regardless of what those characters
are."

## 4. KEY OBSERVATION

"If I write each word as its length, followed by a delimiter, followed
by the word itself, decoding becomes unambiguous. The delimiter only
marks where the length number ends — after that, I'm just counting
characters, so even if the word contains that same delimiter
character inside it, it's harmless, since I'm not searching for the
delimiter inside the word, only before it."

## 5. APPROACH

"For encoding, I'll loop through each word, and for each one, append
its length, a delimiter, and the word itself onto a growing result
string.

For decoding, I'll use two pointers. One pointer marks where the
current length number starts. I scan forward with a second pointer
until I hit the delimiter, which tells me where the number ends.

I convert that number to an integer, then read exactly that many
characters right after the delimiter — that's the word.

I add the word to my result list, then move my first pointer past the
word entirely, to the start of the next length number, and repeat
until I've consumed the whole string."

## 6. WHILE CODING

"For encoding, I start with an empty result string."

result = ""

"For each word, I append its length, a delimiter, then the word."

for word in strs:
    result += str(len(word)) + "#" + word

return result

"For decoding, I start with an empty list and a pointer at index 0."

result = []
left = 0

"I loop as long as there's more string left to process."

while left < len(s):

"I scan forward to find the delimiter, which marks the end of the
length number."

    right = left
    while s[right] != "#":
        right += 1

"Everything between left and right is the length, so I convert it to
an integer."

    length = int(s[left:right])

"The word starts right after the delimiter."

    word_start = right + 1
    word_end = word_start + length

"I extract exactly that many characters as the word, and add it to my
result."

    result.append(s[word_start:word_end])

"I move my pointer past this word, ready to read the next length
number."

    left = word_end

return result

## 7. EDGE CASES

"If the list contains an empty string, its length is 0, so it
encodes as '0#', and decoding correctly reads a length of 0 and
extracts an empty substring.

If a word contains the delimiter character inside it, decoding still
works correctly, since the delimiter is only meaningful right after
the length number — once I know the length, I just count characters
regardless of what they are."

## 8. COMPLEXITY

"Time complexity is O(n) for both encode and decode, where n is the
total number of characters across all strings, since each character
is processed a constant number of times.

Space complexity is O(n) as well, to store the encoded string or the
decoded list."
"""
#"5#Hello5#World"
class Solution:
    def encode_string(self, strs):
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode_string(self, s):
        result = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1 # right at hash
            length = int(s[left:right]) # got 5
            word_start = right + 1  # right is index 2 here
            word_end = word_start + length

            result.append(s[word_start:word_end])
            left = word_end
        return result
    
# Using the functions
solution = Solution()
strs = ["Hello", "World"]

encoded_string = solution.encode_string(strs)
print(encoded_string)              # "5#Hello5#World"

decoded_strs = solution.decode_string(encoded_string)
print(decoded_strs)                # ["Hello", "World"]