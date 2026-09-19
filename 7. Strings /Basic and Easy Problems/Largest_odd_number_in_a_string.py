"""
Largest Odd Number in a String.
Problem Statement: Given a string s, representing a large integer, the task is to return 
the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have 
leading zero.
Examples
      
Example 1
Input:
 s = "5347"
Output:
 "5347"
Explanation:
 The odd numbers formed by the given string are → 5, 3, 53, 347, 5347. The largest odd 
 number without leading zeroes is 5347.

Example 2
Input:
 s = "0214638"
Output:
 "21463"
Explanation:
 The odd numbers formed by the string are → 1, 3, 21, 63, 463, 1463, 21463. We can't use 
 numbers starting with 0, so the largest valid odd number is 21463.




     REVERSE WORDS IN A STRING — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
string containing words separated by spaces.

I need to reverse the order of the words, not the characters inside
each word.

The final string should have exactly one space between each word."


2. BRUTE FORCE

"The straightforward approach would be to split the string into words,
reverse the list of words, and join them back together.

This would work, but I want to manually process the string and identify
each word myself."


3. OPTIMIZE

"I can traverse the string from right to left.

Since I want the words in reverse order anyway, starting from the end
allows me to find the last word first, then the second-last word, and
continue until I reach the beginning."


4. KEY OBSERVATION

"The key observation is that when traversing from right to left, I first
skip any spaces.

Once I reach a character, I know I've reached the END of a word, so I
save that index.

Then I continue moving left until I reach a space or the beginning of
the string.

At that point, the word starts at i + 1.

So I can extract the word using:

s[start:end + 1]

and add it to my result."


5. APPROACH

"I'll initialize i to the last index of the string and create a result
list.

While i is still inside the string, I'll first skip any spaces.

If i becomes negative, there are no words left, so I'll stop.

Otherwise, I'll save i as the end of the current word.

Then I'll move i left while the characters are not spaces.

Once I stop, the start of the word is i + 1.

I'll extract that word from the original string and append it to result.

Since I'm already finding the words from right to left, result will
automatically contain them in reversed order.

Finally, I'll join the words using a single space."


6. WHILE CODING

"I'm starting i at the last character because I want to process the
words from right to left."

i = len(s) - 1

"First, I'm skipping any spaces until I reach an actual character."

while i >= 0 and s[i] == " ":
    i -= 1

"If I run out of characters, there are no more words to process."

if i < 0:
    break

"Now I'm standing at the last character of a word, so I'm saving its
ending index."

end = i

"I'm moving left until I either find a space or go past the beginning
of the string."

while i >= 0 and s[i] != " ":
    i -= 1

"Since i is now either on a space or at -1, the actual word starts one
position after i."

start = i + 1

"Now I can pull the complete word directly from the original string."

word = s[start:end + 1]

"I'm adding each word as I find it, and because I'm scanning backwards,
the words are already being added in reversed order."

result.append(word)

"Finally, joining with one space automatically removes extra spaces
between the words."

return " ".join(result)


7. EDGE CASES

"If the string is empty, i starts at -1, so the loop never runs and I
return an empty string."

i = len(s) - 1

while i >= 0:
    ...

"If there are spaces at the beginning, end, or multiple spaces between
words, this loop skips all of them."

while i >= 0 and s[i] == " ":
    i -= 1

"If the string contains only spaces, i eventually becomes -1 and I stop
without trying to extract a word."

if i < 0:
    break

"If there is only one word, I'll extract that word normally and return
it unchanged."


8. COMPLEXITY

"The time complexity is O(n) because I move through the string from
right to left and each character is processed a constant number of
times.

The space complexity is O(n) because I store the words in the result
list and create the final output string."      
"""
class Solution:
    def largest_odd(self, s):

        # Find the rightmost odd digit
        end = -1

        for i in range(len(s) - 1, -1, -1):

            if int(s[i]) % 2 == 1:
                end = i
                break

        # No odd digit exists
        if end == -1:
            return ""

        # Skip leading zeros
        start = 0

        while start <= end and s[start] == "0":
            start += 1

        # Return from first non-zero digit to rightmost odd digit
        return s[start:end + 1]
    
# Driver code
s = "0214638"
obj = Solution()
result = obj.largest_odd(s)

print(result)

"""
RIGHT → LEFT
find first odd digit → end

LEFT → RIGHT
skip leading zeros → start

return s[start:end + 1]
"""