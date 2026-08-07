"""Find the single non-repeating element in an array using XOR.

Problem:
    Every number in the list appears exactly twice except for one number.
    Find and return that unique number.

Example:
    arr = [4, 1, 2, 1, 2]
    Output: 4

Key XOR properties:
    - x ^ x = 0
    - x ^ 0 = x
    - XOR is commutative and associative

XOR example:
    Since XOR is commutative and associative, we can rearrange the expression.

    4 ^ 1 ^ 2 ^ 1 ^ 2
    = 4 ^ (1 ^ 1) ^ (2 ^ 2)
    = 4 ^ 0 ^ 0
    = 4

Algorithm:
    1. Set result = 0.
    2. XOR every number in the array with result.
    3. Paired duplicates cancel out, leaving the unique number.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    # Function to find the single non-repeating element using XOR
    def getSingleElement(self, arr):
        xorr = 0

        # XOR all elements — duplicates cancel out
        for num in arr:
            xorr ^= num

        return xorr

# Driver code
arr = [4, 1, 2, 1, 2]
obj = Solution()
ans = obj.getSingleElement(arr)
print("The single element is:", ans)