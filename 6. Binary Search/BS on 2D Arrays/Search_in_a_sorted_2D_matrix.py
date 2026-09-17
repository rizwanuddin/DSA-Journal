"""
Search in a sorted 2D matrix
Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

Examples
Input :mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
Output :True.
Explanation :The target = 8 exists in the 'mat' at index (1, 3).
Input :mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ], target = 78
Output :false.
Explanation :The target = 78 does not exist in the 'mat'. Therefore in the output, we see 'false'.



SEARCH IN A SORTED 2D MATRIX — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
2D matrix where each row is sorted, and the first element of each row
is greater than the last element of the previous row.

I need to determine whether the target exists in the matrix.

If it exists, I'll return True. Otherwise, I'll return False."


2. BRUTE FORCE

"The straightforward approach would be to go through every element in
the matrix and compare it with the target.

This would work, but for N rows and M columns, it would take O(N * M)
time in the worst case."


3. OPTIMIZE

"Since the entire matrix is sorted, I can treat it like one imaginary
sorted 1D array and apply binary search.

I don't actually need to create a new flattened array. I can convert
any imaginary 1D index back into its row and column in the matrix."


4. KEY OBSERVATION

"The key observation is that the matrix contains N * M total elements,
so I can imagine its indices going from 0 to N * M - 1.

For any imaginary 1D index mid, I can find its position in the matrix
using:

row = mid // M
col = mid % M

Dividing by M tells me which row I'm in, and taking the remainder tells
me which column I'm in.

Then I can access the value using mat[row][col] and perform normal
binary search."


5. APPROACH

"I'll calculate the number of rows N and columns M.

I'll treat the matrix as an imaginary array containing N * M elements.

I'll initialize low to 0 and high to N * M - 1.

While low is less than or equal to high, I'll calculate mid.

I'll convert mid into its matrix row and column.

Then I'll compare mat[row][col] with the target.

If it equals the target, I'll return True.

If it's smaller than the target, I'll search the right half.

If it's greater than the target, I'll search the left half.

If the search space becomes empty, I'll return False."


6. WHILE CODING

"I'm calculating the total number of elements using N * M."

total_ele = N * M

"I'm performing binary search over the imaginary flattened indices."

low = 0
high = total_ele - 1

"Now I need to convert my 1D mid index into a matrix position."

row = mid // M
col = mid % M

"mid divided by the number of columns gives me the row, and the
remainder gives me the column."

"I'm accessing that element directly without actually flattening the
matrix."

mid_value = mat[row][col]

"From here, it's normal binary search."

if mid_value == target:
    return True

elif mid_value < target:
    low = mid + 1

else:
    high = mid - 1


7. EDGE CASES

"If the matrix could be empty, I should handle that before accessing
mat[0]."

if not mat or not mat[0]:
    return False

"If the matrix contains only one element, the normal binary search
logic still works."

"If the target is smaller than the first element or larger than the
last element, I could optionally return False immediately."

if target < mat[0][0] or target > mat[-1][-1]:
    return False


8. COMPLEXITY

"There are N * M total elements in the matrix, and I'm performing
binary search over those elements.

So the time complexity is O(log(N * M)).

The space complexity is O(1) because I don't actually create a
flattened array. I only calculate the row and column when needed."
"""
class Solution:

    def search(self, mat, target):

        N = len(mat)       # Number of rows
        M = len(mat[0])    # Number of columns

        total_ele = N * M

        low = 0
        high = total_ele - 1

        while low <= high:

            mid = (low + high) // 2

            # Convert imaginary 1D index to 2D matrix position
            row = mid // M
            col = mid % M

            mid_value = mat[row][col]

            if mid_value == target:
                return True

            elif mid_value < target:
                low = mid + 1

            else:
                high = mid - 1

        return False