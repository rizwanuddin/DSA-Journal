"""
# Reverse a Number

## Problem
Reverse the digits of a given number.

## Example
Input:
12345
Output:
54321

## Logic

n = 123

# % gives the remainder
# Here, it gives the last digit
last_digit = n % 10
print(last_digit)   # 3

# // does floor division
# Here, it removes the last digit
remaining_number = n // 10
print(remaining_number)   # 12

# / does normal division
# It gives a decimal answer
normal_division = n / 10
print(normal_division)   # 12.3

IMP:
Use `// 10` in Python to remove the last digit.
Use `/ 10` in Java to remove the last digit.

## Complexity

Time Complexity: O(log n)
Space Complexity: O(1)
"""
def reverse_digits(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_number = 0
    while n > 0:
        last_digit = n % 10
        reversed_number = reversed_number * 10 + last_digit
        n = n // 10
    return sign * reversed_number

# Example usage
number = 123
print(reverse_digits(number))  # Output: 321

number = -123
print(reverse_digits(number))  # Output: -321
