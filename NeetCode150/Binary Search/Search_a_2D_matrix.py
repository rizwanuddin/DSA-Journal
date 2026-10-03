"""
Search a 2D Matrix - Explanation

You are given an m x n 2-D integer array matrix and an integer target.
Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.
Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false



## Search a 2D Matrix

**Clarify:**
- so each row in the matrix is sorted, and the first number of a row is bigger than the last number of the row before it
- that basically means if I flatten the whole matrix into one line, it would be fully sorted
- I need to return True if target is somewhere in there, False if not
- and it needs to run in O(log(m*n)) time

**Brute force:**
- the easy way is just check every single cell one by one
- that's O(m*n) time, which is too slow for what they're asking

**Optimize:**
- since the matrix is basically one big sorted line if you flatten it, I can just do normal binary search on it
- that gets me O(log(m*n))

**Key observation:**
- I don't actually need to flatten it for real
- if I treat every cell like it has one single index from 0 to m*n-1, I can always get back its real row and column using row = index divided by number of columns, and col = index mod number of columns
- so I just binary search on these fake indices and convert each time

**Approach:**
- first get m, the number of rows, and n, the number of columns
- set low to 0 and high to m*n minus 1
- keep looping while low is less than or equal to high
- find the middle index, then convert it to row and col
- compare the value there to target, and shrink low or high like normal binary search
- if nothing found, return False

**While coding:**
- first I make a class called Solution
- then a function called search_matrix that takes in matrix and target
- I get m as len(matrix), that's my row count
- I get n as len(matrix[0]), that's my column count
- then I set low to 0 and high to m times n minus 1
- I start a while loop, runs as long as low is less than or equal to high
- inside, I get mid as low plus high, divided by 2
- then I convert mid into row and col — row is mid divided by n, col is mid mod n
- I check if matrix at that row and col equals target, if yes I return True
- if that value is bigger than target, I bring high down to mid minus 1
- otherwise I push low up to mid plus 1
- if the loop ends without finding it, I return False

**Edge cases:**
- if it's just one row or one column, this still works the same way
- if target is smaller or bigger than everything in the matrix, the loop just shrinks down and returns False
- if the matrix is empty, I'd want to check that before starting, so it doesn't break

**Complexity:**
- time is O(log(m*n)) since I'm binary searching the whole thing like one array
- space is O(1), I'm not using any extra structures, just a few variables
"""
class Solution:
    def search_matrix(self, matrix, target):
        m = len(matrix) # No of Rows
        n = len(matrix[0]) # # No of Columns

        low = 0
        high = (m * n) - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // n 
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else :
                low = mid + 1
        return False

        