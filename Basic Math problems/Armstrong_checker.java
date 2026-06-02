/*
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
*/


public class Armstrong_checker {

    // Static method to check if a number is an Armstrong number
    public static boolean isArmstrong(int num) {
        int k = String.valueOf(num).length(); // Get number of digits
        int sum = 0;
        int n = num;

        while (n > 0) {
            int ld = n % 10;             // Last digit
            sum += Math.pow(ld, k);      // Add ld^k
            n /= 10;                     // Remove digit
        }

        return sum == num;
    }

    public static void main(String[] args) {
        int number = 153;

        // Use class method to check
        if (isArmstrong(number)) {
            System.out.println(number + " is an Armstrong number.");
        } else {
            System.out.println(number + " is not an Armstrong number.");
        }
    }
}
