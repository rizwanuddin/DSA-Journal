/* 
# Palindrome Number

## Problem
Check whether a given number is a palindrome.

A palindrome number reads the same forward and backward.

## Example
Input:
4554

Output:
4554 is a palindrome.

Another Example:
Input:
123

Output:
123 is not a palindrome.

## Logic

n = 4554

We reverse the number and compare it with the original number.

Example:

n = 4554

Step 1:
last_digit = n % 10
last_digit = 4

reverse = 0 * 10 + 4
reverse = 4

n = n // 10
n = 455

Step 2:
last_digit = 455 % 10
last_digit = 5

reverse = 4 * 10 + 5
reverse = 45

n = 455 // 10
n = 45

Step 3:
last_digit = 45 % 10
last_digit = 5

reverse = 45 * 10 + 5
reverse = 455

n = 45 // 10
n = 4

Step 4:
last_digit = 4 % 10
last_digit = 4

reverse = 455 * 10 + 4
reverse = 4554

n = 4 // 10
n = 0

Now compare:

original number = 4554
reversed number = 4554

Since both are equal, the number is a palindrome.

IMP:
Use `% 10` to get the last digit.
Use `// 10` in Python to remove the last digit.
Use `/ 10` in Java with integers to remove the last digit.

## Complexity

Time Complexity: O(log n)

Because we divide the number by 10 in every loop iteration.
The number of digits in a number is approximately log10(n).

Space Complexity: O(1)
*/

public class Palindrome_digits {
    public static boolean palindrome(int n) {

        int originalNumber = n;
        int reversedNumber = 0;

        while (n > 0) {
            int lastDigit = n % 10;
            reversedNumber = reversedNumber * 10 + lastDigit;
            n = n / 10;
        }

        return originalNumber == reversedNumber;
    }

    public static void main(String[] args) {
        int number = 4554;
        if (palindrome(number)) {
            System.out.println(number + " is a palindrome.");
        } else {
            System.out.println(number + " is not a palindrome.");
        }
    }
}