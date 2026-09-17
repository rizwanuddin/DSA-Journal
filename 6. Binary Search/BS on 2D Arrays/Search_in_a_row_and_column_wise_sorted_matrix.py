"""
OPTIMAL SOLUTION NOT BINARY SEARCH - THIS IS PART 2 OF SEARCH IN A SORTED 2D MATRIX

Search in a row and column-wise sorted matrix
Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row and each column are sorted in non-decreasing order. But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists). You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.
Examples

Example 1:
Matrix=
1   4   7   11
2   5   8   12
3   6   9   16
10 13  14  17
Target: 9
Output: Found at (2,2) (0-indexed)
Example 2:
Matrix=
5   10  15
6   12  18
8   16  20
Target: 7
Output: Not Found



SEARCH IN ROW-WISE AND COLUMN-WISE SORTED MATRIX — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
matrix where every row is sorted from left to right and every column
is sorted from top to bottom.

I need to determine whether the target exists in the matrix.

If it exists, I'll return True. Otherwise, I'll return False."


2. BRUTE FORCE

"The straightforward approach would be to go through every element in
the matrix and compare it with the target.

This would work, but with N rows and M columns, it would take
O(N * M) time."


3. OPTIMIZE

"Since both the rows and columns are sorted, I can take advantage of
that ordering.

I'll start from the top-right corner because from that position I have
two useful directions.

Moving left gives me smaller values, while moving down gives me larger
values."


4. KEY OBSERVATION

"The key observation is that starting from the top-right corner lets me
eliminate either a row or a column after every comparison.

If the current value is smaller than the target, everything to its left
in that row is also smaller, so I can eliminate that entire row and
move down.

If the current value is greater than the target, everything below it in
that column is also greater, so I can eliminate that entire column and
move left."


5. APPROACH

"I'll start at the top-right corner of the matrix.

So row starts at 0 and col starts at M - 1.

While row is still inside the matrix and col has not gone past the
left side, I'll compare the current value with the target.

If the current value equals the target, I'll return True.

If the current value is smaller than the target, I'll move down because
I need a larger value.

If the current value is greater than the target, I'll move left because
I need a smaller value.

If I leave the matrix without finding the target, I'll return False."


6. WHILE CODING

"I'm starting from the top-right corner."

row = 0
col = M - 1

"I'm continuing while my row and column are still inside the matrix."

while row < N and col >= 0:

"If the current value equals the target, I've found it."

if current == target:
    return True

"If the current value is too small, I need something larger, so I'm
moving down."

elif current < target:
    row += 1

"If the current value is too large, I need something smaller, so I'm
moving left."

else:
    col -= 1


7. EDGE CASES

"If the matrix could be empty, I should handle that before accessing
mat[0]."

if not mat or not mat[0]:
    return False

"If the target is smaller than the smallest element or larger than the
largest element, I can optionally return False immediately."

if target < mat[0][0] or target > mat[-1][-1]:
    return False

"If the matrix has only one row or one column, the same movement logic
still works."


8. COMPLEXITY

"The time complexity is O(N + M).

This is because I can move down at most N times and left at most M
times.

The space complexity is O(1) because I only use the row, col, and
current variables."
"""
class Solution:
    def search(self, mat, target):

        N = len(mat)       # Number of rows
        M = len(mat[0])    # Number of columns

        # Start at top-right corner
        row = 0
        col = M - 1

        while row < N and col >= 0:

            current = mat[row][col]

            if current == target:
                return True

            # Current is too small → move DOWN
            elif current < target:
                row += 1

            # Current is too large → move LEFT
            else:
                col -= 1

        return False


if __name__ == "__main__":

    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    target = 8

    obj = Solution()

    found = obj.search(matrix, target)

    print(found)