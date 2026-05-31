"""
# GCD Using Euclidean Algorithm

## Problem
Find the Greatest Common Divisor, also called GCD, of two numbers.
The GCD is the largest number that divides both numbers completely.

## Logic

The Euclidean Algorithm works by repeatedly reducing the larger number.
Instead of subtracting the smaller number again and again, we use modulo `%`.
Modulo gives the remainder after division.
So:
a % b
means we remove as many `b`s as possible from `a` and keep only the leftover.
This makes the algorithm faster than repeated subtraction.

## IMP

Use `%` to get the remainder.
Modulo is the optimized version of repeated subtraction.
The loop continues until one number becomes 0.
When one number becomes 0, the other number is the GCD.

To find the GCD of n1 and n2 where n1 > n2:
1. Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
2. Once one becomes 0, the other is the GCD of the original numbers.

Example:
n1 = 20, n2 = 15

gcd(20, 15) = gcd(20 - 15, 15) = gcd(5, 15)
gcd(5, 15)  = gcd(15 - 5, 5)  = gcd(10, 5)
gcd(10, 5)  = gcd(10 - 5, 5) = gcd(5, 5)
gcd(5, 5)   = gcd(5 - 5, 5)  = gcd(0, 5)

Hence, return 5 as the GCD.
    

## Complexity

Time Complexity: O(min(N1, N2))
Because modulo reduces the numbers quickly.

Space Complexity: O(1)
Because we only use a constant number of variables.
"""
def find_gcd(a, b):
    while a > 0 and b > 0:
        if a > b :
            a = a % b
        else:
            b = b % a 
    if a == 0:
        return b
    elif b == 0 :
        return a     

# Example usage
def main():
    n1 = 20
    n2 = 15

    # Find the GCD of n1 and n2
    gcd = find_gcd(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")

if __name__ == "__main__":
    main()