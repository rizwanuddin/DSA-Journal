"""
Count Good Numbers Using Modular Exponentiation

A digit string is called good if:
    digits at even indices (0, 2, 4, ...) are even, so they can be 0, 2, 4, 6, or 8
    digits at odd indices (1, 3, 5, ...) are prime, so they can be 2, 3, 5, or 7

Given an integer n, return the total number of good digit strings of length n. Since the answer 
can be very large, return it modulo 109 + 7. Leading zeros are allowed in the string.

Example 1
Input: n = 1
Output: 5
Explanation: There is only one position, and it is index 0, which is an even index. So the digit 
can be 0, 2, 4, 6, or 8. That gives 5 valid strings.

Example 2
Input: n = 4
Output: 400
Explanation: Indices 0 and 2 are even, so each of them has 5 choices. Indices 1 and 3 are odd, 
so each of them has 4 choices. So the total number of good strings is: 400




# COUNT GOOD NUMBERS — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I need to build digit
strings of length n where even positions hold even digits and odd
positions hold prime digits, and count how many such strings exist,
returned modulo 10^9 + 7."

## 2. BRUTE FORCE

"The brute-force way would be to actually generate every valid
string and count them, but that's exponential and completely
impractical, since the number of valid strings grows extremely fast."

## 3. OPTIMIZE

"Since each position's choice is independent of every other
position, I don't need to generate anything. I just need to multiply
together how many choices exist at each position."

## 4. KEY OBSERVATION

"Even positions always have exactly 5 valid digits, and odd
positions always have exactly 4 valid digits, regardless of what
digit is chosen elsewhere. Since the positions don't affect each
other, the total count is the product of the choice counts across
every position, not a sum."

## 5. APPROACH

"I'll write a recursive helper that takes the current index.

If the index equals n, I've placed a digit at every position, so I
return 1, since that's the identity value for multiplication and
won't affect the running product.

Otherwise, I determine how many choices this index has: 5 if it's
even, 4 if it's odd.

I multiply that by the result of the recursive call for the rest of
the string, and take the result modulo 10^9 + 7 to keep the number
manageable.

I start the recursion at index 0."

## 6. WHILE CODING

"First, I set up the modulus, since the answer needs to be returned
modulo 10^9 plus 7."

MOD = 10**9 + 7

"My helper function tracks which index I'm currently deciding."

def helper(index):

"If I've placed a digit at every position, there's nothing left to
decide, so I return 1, the multiplicative identity."

    if index == n:
        return 1

"I determine how many valid digits exist at this index — 5 for even
positions, 4 for odd."

    choices = 5 if index % 2 == 0 else 4

"I multiply this position's choices by everything the rest of the
string can produce, applying the modulus to keep the number
manageable."

    return (choices * helper(index + 1)) % MOD

"Finally, I start the recursion at index 0."

return helper(0)

## 7. EDGE CASES

"If n is 1, there's only index 0, which is even, so the answer is
just 5, matching the given example directly.

If n is very large, plain recursion like this becomes too slow,
since it makes one call per position. That's where modular
exponentiation would come in, to compute the result in logarithmic
time instead of linear time."

## 8. COMPLEXITY

"Time complexity is O(n), since I make one recursive call per
position in the string.

Space complexity is O(n) as well, due to the recursion stack depth
matching the string length."
"""
class Solution:
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7
        def helper(index):
            if index == n:
                return 1
            if index % 2 == 0:
                choices = 5
            else:
                choices = 4
            return (choices * helper(index + 1)) % MOD
        return helper(0)