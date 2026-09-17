"""
Find Peak Element (2D Matrix)
Problem Statement: Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the array [i, j]. A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.
Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

Note: As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.
Examples

Example 1:
Input:
 mat = [[5, 10, 8], [4, 25, 7], [3, 9, 6]]
Output:
 [1, 1]
Explanation:
 The value at index [1, 1] is 25, which is a peak because all its neighbors (10, 7, 4, 9) are smaller.
Example 2:
Input:
 mat = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
Output:
 [2, 2]
Explanation:
 The value at index [2, 2] is 9, which is a peak as it is greater than its neighbors (8, 4).

 
 

 FIND PEAK ELEMENT IN 2D MATRIX — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
2D matrix.

I need to find a peak element and return its row and column.

A peak element should be greater than its neighboring elements."


2. BRUTE FORCE

"The straightforward approach would be to check every element in the
matrix and compare it with its neighbors.

This would work, but with N rows and M columns, it would take
O(N * M) time."


3. OPTIMIZE

"We can optimize this using binary search on the columns.

Instead of checking every column, I'll choose a middle column and find
the largest element in that column.

Then I'll use its left and right neighbors to decide which direction
to continue searching."


4. KEY OBSERVATION

"The key observation is that after choosing a middle column, I find the
largest element in that entire column.

Because it is already the largest value in its column, I only need to
compare it with its left and right neighbors.

If it is greater than both, I've found a peak.

If the left neighbor is larger, I know I can continue searching toward
the left.

If the right neighbor is larger, I continue searching toward the
right."


5. APPROACH

"I'll binary search over the columns, so low starts at 0 and high starts
at M - 1.

For each middle column, I'll go through all the rows and find the row
containing the maximum value in that column.

That gives me my possible peak.

Then I'll get its left and right neighbors.

If the current value is greater than both neighbors, I'll return its
row and column.

If the left neighbor is greater, I'll search the columns to the left.

Otherwise, I'll search the columns to the right.

I'll continue until I find a peak."


6. WHILE CODING

"I'm binary searching over the columns."

low = 0
high = M - 1

"For each middle column, I'm finding the maximum element in that
column."

max_row = 0

for row in range(1, N):
    if mat[row][mid] > mat[max_row][mid]:
        max_row = row

"Since this is already the maximum element in its column, I now only
need to compare it with its horizontal neighbors."

current = mat[max_row][mid]

"If there is no left or right neighbor, I'm treating that side as
negative infinity."

"If current is greater than both sides, I've found my peak."

if current > left and current > right:
    return [max_row, mid]

"If the left neighbor is bigger, I'm searching left."

elif left > current:
    high = mid - 1

"Otherwise, I'm searching right."

else:
    low = mid + 1


7. EDGE CASES

"If the matrix could be empty, I should handle that before accessing
mat[0]."

if not mat or not mat[0]:
    return [-1, -1]

"If the middle column is the first column, there is no left neighbor,
so I treat it as negative infinity."

if mid - 1 >= 0:
    left = mat[max_row][mid - 1]
else:
    left = float("-inf")

"If the middle column is the last column, there is no right neighbor,
so I also treat it as negative infinity."

if mid + 1 < M:
    right = mat[max_row][mid + 1]
else:
    right = float("-inf")


8. COMPLEXITY

"Binary search over M columns takes O(log M) iterations.

For every middle column, I scan all N rows to find the maximum element.

So the total time complexity is O(N log M).

The space complexity is O(1) because I only use a constant number of
extra variables."
"""
class Solution:
    def find_peak(self, mat):

        N = len(mat)       # Number of rows
        M = len(mat[0])    # Number of columns

        # Binary search on columns
        low = 0
        high = M - 1

        while low <= high:

            # Pick middle column
            mid = (low + high) // 2

            # Find the largest element in the middle column
            max_row = 0

            for row in range(1, N):
                if mat[row][mid] > mat[max_row][mid]:
                    max_row = row

            # Our possible peak
            current = mat[max_row][mid]

            # Get left neighbor
            if mid - 1 >= 0:
                left = mat[max_row][mid - 1]
            else:
                left = -1

            # Get right neighbor
            if mid + 1 < M:
                right = mat[max_row][mid + 1]
            else:
                right = -1

            # Current is greater than both sides → peak found
            if current > left and current > right:
                return [max_row, mid]

            # Left neighbor is bigger → search left columns
            elif left > current:
                high = mid - 1

            # Right neighbor is bigger → search right columns
            else:
                low = mid + 1

        return [-1, -1]


# Driver code
mat = [
    [40, 10, 5],
    [30, 25, 12],
    [18, 9, 7]
]

obj = Solution()

result = obj.find_peak(mat)

print("Peak index:", result)

            