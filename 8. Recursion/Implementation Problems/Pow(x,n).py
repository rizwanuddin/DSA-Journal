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
"""
class Solution:
    def myPow(self, x, n):

        # Base case
        if n == 0:
            return 1

        # Negative exponent
        if n < 0:
            return self.myPow(1 / x, -n)

        # Calculate x^(n//2)
        half = self.myPow(x, n // 2)

        # EVEN exponent
        if n % 2 == 0:
            return half * half

        # ODD exponent
        else:
            return x * half * half