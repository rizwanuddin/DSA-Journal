"""
Pow(x,n)

Implement the power function pow(x, n) , which calculates the x raised to n 
i.e. xn.

Note : In output print 6 digits places after decimal point.

Example 1:
Input : x = 2.0000 , n = 10
Output : 1024.0000
Explanation : Answer = 2^10 => 1024.

Example 2:
Input : x = 2.0000 , n = -2
Output : 0.2500
Explanation : Answer = 2^(-2) = 1/4 => 0.25.




POW(X, N) / FAST POWER — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
number x and an integer exponent n.

I need to calculate x raised to the power n.

The exponent can be positive, zero, or negative."


2. BRUTE FORCE

"The straightforward approach would be to multiply x by itself n times.

For example, for x^5, I could calculate:

x * x * x * x * x

This works, but it takes O(n) time for a positive exponent."


3. OPTIMIZE

"We can optimize this using recursion and exponentiation by squaring.

Instead of reducing n by 1 each time, I'll divide the exponent by 2.

I'll recursively calculate x^(n // 2) once and store it in half.

Then I can use that result to build the final answer."


4. KEY OBSERVATION

"The key observation is that powers can be broken into smaller powers.

If n is even:

x^n = x^(n/2) * x^(n/2)

So once I calculate half, I can return:

half * half

If n is odd, one extra x remains:

x^n = x * x^(n//2) * x^(n//2)

So I return:

x * half * half

This allows me to divide the exponent by 2 at every recursive call."


5. APPROACH

"First, I'll handle the base case.

If n is 0, I'll return 1 because any non-zero number raised to the
power 0 is 1.

If n is negative, I'll use the negative exponent rule:

x^(-n) = (1/x)^n

So I'll change x to 1/x and make the exponent positive.

Once n is positive, I'll recursively calculate x raised to n // 2 and
store it in half.

If n is even, I'll return half times half.

If n is odd, I'll return x times half times half."


6. WHILE CODING

"First, I'm handling my base case so the recursion knows when to stop."

if n == 0:
    return 1

"Now I'm handling negative exponents.

My recursive algorithm works with a positive exponent, so I'm taking
the reciprocal of x and converting n to positive."

if n < 0:
    return self.myPow(1 / x, -n)

"Instead of recursively calculating n - 1, I'm dividing the exponent
by 2."

half = self.myPow(x, n // 2)

"If n is even, the two halves are equal, so I multiply half by itself."

if n % 2 == 0:
    return half * half

"If n is odd, there is one extra x that isn't included in the two
halves, so I multiply by x one more time."

else:
    return x * half * half


7. EDGE CASES

"If n is zero, I'll immediately return 1."

if n == 0:
    return 1

"If n is negative, I'll take the reciprocal of x and convert the
exponent to positive."

if n < 0:
    return self.myPow(1 / x, -n)

"If x is 0 and n is positive, the recursion correctly returns 0.

However, x = 0 with a negative exponent would require dividing by zero,
so if the problem allows that input I should handle it separately."

if x == 0 and n < 0:
    # undefined / invalid input
    raise ValueError("0 cannot be raised to a negative power")


8. COMPLEXITY

"The time complexity is O(log |n|) because I divide the exponent by 2
at every recursive call.

The space complexity is O(log |n|) because the recursive call stack has
logarithmic depth."
"""
class Solution:
    def myPow(self, x, n):

        # Base case
        if n == 0:
            return 1

        # Negative exponent
        if n < 0:
            return self.myPow(1 / x, -n) #convert to positive since the algorithm is designed to run on positive

        # Calculate x^(n//2)
        half = self.myPow(x, n // 2)

        # EVEN exponent
        if n % 2 == 0:
            return half * half

        # ODD exponent
        else:
            return x * half * half