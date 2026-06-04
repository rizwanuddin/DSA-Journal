/* 
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
*/

public class Reverse_digits {
    public static int reverse_digit(int n){
        int reversed = 0;
        int sign = -1;
        if (n<0){
            sign = -1;
        }
        else{
            sign = 1;
        }
        n = Math.abs(n); // if not done, it will give wrong answer for negative numbers
        while (n > 0) {
            int lastDigit = n % 10;
            reversed = reversed * 10 + lastDigit;
            n = n / 10;
        }
        return sign * reversed;
    }
    public static void main(String[] args){
        int n = 12345;
        int result = reverse_digit(n);
        System.out.println(result);  // Output: 54321
    }
}
