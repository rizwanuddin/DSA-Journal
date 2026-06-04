"""
# Armstrong Number Checker

## Problem
Check whether a given number is an Armstrong number.

An Armstrong number is a number where the sum of each digit raised to the power of the total number of digits is equal to the original number.

## Logic

First, count how many digits are in the number.

Then, take each digit one by one.

For each digit:
- Get the last digit using `% 10`
- Raise that digit to the power of the total number of digits
- Add it to the sum
- Remove the last digit using `/ 10`

At the end, compare the sum with the original number.

If both are equal, the number is an Armstrong number.

## Short Example

For 153:

Total digits = 3

1^3 + 5^3 + 3^3 = 153

So 153 is an Armstrong number.

## IMP

Use `% 10` to get the last digit.
Use `/ 10` in Java to remove the last digit from an integer.
`String.valueOf(num).length()` is used to count the number of digits.
`Math.pow(ld, k)` is used to calculate digit power.
`Math.pow()` returns a double, but Java can still add it to `sum` with `+=` because compound assignment automatically casts it back to int.

## Complexity

Time Complexity: O(log n)
Because we process each digit once.
Space Complexity: O(1)
Because we only use a few variables.
"""

class ArmstrongChecker:
    @staticmethod
    def is_armstrong_number(n):
        str_n = len(str(n))
        sum = 0
        while n > 0 :
            last_digit = n % 10
            sum += last_digit ** str_n
            n = n // 10
            return sum == n
        
# Example usage
number = 153
if ArmstrongChecker.is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
