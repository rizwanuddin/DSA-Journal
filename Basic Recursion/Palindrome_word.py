class Palindrome_word:
    def is_palindrome(s):
        start, end = 0, len(s) -1
        while start < end :
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True 
    str = "ABCDCBA"  # String to check for palindrome
    ans = is_palindrome(str)  # Check if the string is a palindrome

    # Output the result
    if ans:
        print("Palindrome")
    else:
        print("Not Palindrome")

## Recursion way to do it
# Function to check if a string is a palindrome using recursion
def palindrome(i, s):
    # Base Condition: If i exceeds half of the string, all the elements have been compared
    # and the string is a palindrome, return True.
    if i >= len(s) // 2:
        return True

    # If the start and end characters are not equal, it's not a palindrome.
    if s[i] != s[len(s) - i - 1]:
        return False

    # If both characters are the same, increment i and check start+1 and end-1.
    return palindrome(i + 1, s)

# Driver code
if __name__ == "__main__":
    s = "madam"  # Example string to check
    
    # Check if the string is a palindrome and output the result
    print(palindrome(0, s))  # Output True if palindrome, False if not
"""
The optimal solution is the iterative two-pointer approach. 
It checks characters from both ends and moves inward. 
It takes O(n) time and O(1) extra space. 
The recursive version also takes O(n) time but uses O(n) stack space,
so it is not more optimal in terms of memory.
Recursion is mainly useful here for demonstrating recursive thinking, 
not for production-quality code."""       