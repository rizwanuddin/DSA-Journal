# Count Digits of a Number
#
# Problem
#
# Count how many digits are present in a number.
#
# Example
#
# Input:
#
# 329823
#
# Output:
#
# 6
#
# Formula
#
# digits = int(log10(n) + 1)
#
# Explanation
#
# log10(n) gives the power of 10 for the number.
#
# We add 1 because the digit count is always one more than the power.
#
# Example:
#
# log10(329823) = 5.518
#
# 5.518 + 1 = 6.518
#
# int(6.518) = 6
#
# So, 329823 has 6 digits.
#
# Python
#
# Use math.log10(n) to calculate the number of digits.
#
# For 0, return 1.
#
# For negative numbers, convert the number to positive using abs(n).
#
# Java
#
# Use Math.log10(n) to calculate the number of digits.
#
# For 0, return 1.
#
# For negative numbers, convert the number to positive using Math.abs(n).
#
# Complexity
#
# Time Complexity: O(1)
#
# Space Complexity: O(1)