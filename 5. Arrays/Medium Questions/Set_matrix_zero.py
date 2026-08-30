"""
OPTIMAL APPROACH - SET MATRIX ZEROES
Time Complexity: O(m * n)
Space Complexity: O(1)

IDEA:
Instead of creating separate arrays to remember which rows and columns
need to become zero, we use the matrix's FIRST ROW and FIRST COLUMN
as our marker storage.

Think of it like:

    matrix[i][0]  -> tells us whether ROW i should become zero
    matrix[0][j]  -> tells us whether COLUMN j should become zero


STEP 1: SAVE FIRST ROW/COLUMN STATUS
-------------------------------------
Before using the first row and first column as markers, we need to
remember whether they ORIGINALLY contained a zero.

    first_row_zero = True/False
    first_col_zero = True/False

We save this information because we're about to modify the first
row/column and use them as marker storage.

IMPORTANT:
We do NOT zero the first row/column yet.
We only save their original status.


STEP 2: MARK
-------------
Traverse only the INNER matrix (starting from row 1 and column 1).

If we find:

    matrix[i][j] == 0

then mark its row and column:

    matrix[i][0] = 0   # ROW i needs to become zero
    matrix[0][j] = 0   # COLUMN j needs to become zero

So instead of having:

    rows_to_zero[i]
    cols_to_zero[j]

we use:

    matrix[i][0]
    matrix[0][j]


STEP 3: ZERO USING THE MARKERS
-------------------------------
Traverse the inner matrix again.

For every matrix[i][j], check:

    matrix[i][0] == 0   -> Is my row marked?

                OR

    matrix[0][j] == 0   -> Is my column marked?

If either is true:

    matrix[i][j] = 0


STEP 4: FINISH THE FIRST ROW/COLUMN
------------------------------------
Now use the information we saved in Step 1.

If:

    first_row_zero == True

zero the entire first row.

If:

    first_col_zero == True

zero the entire first column.


EASY WAY TO REMEMBER:

    1. SAVE
       First row/column original zero status

            ↓

    2. MARK
       Use first row/column as marker arrays

            ↓

    3. ZERO
       Use those markers to modify the inner matrix

            ↓

    4. FINISH
       Use the saved flags to handle first row/column


WHY IS THIS OPTIMAL?

Normal marker approach:
    Time  -> O(m * n)
    Space -> O(m + n)

Optimal approach:
    Time  -> O(m * n)
    Space -> O(1)

We achieve O(1) extra space because the matrix itself stores
the row/column markers.


I’m using an in-place matrix marking approach so I can set the required rows and columns to zero without using extra row and column arrays. First, I check whether the first row and first 
column originally contain any zero and save that information in first_row_zero and first_col_zero, because I’m going to reuse the first row and first column as markers. Then I go through 
the rest of the matrix starting from index 1,1, and whenever I find a 0 at matrix[i][j], I mark its entire row by setting matrix[i][0] = 0 and mark its entire column by setting 
matrix[0][j] = 0. After that, I traverse the inner matrix again, and if either the row marker matrix[i][0] or the column marker matrix[0][j] is zero, I set that current cell to zero. 
Finally, I use the two saved boolean values to decide whether the original first row or first column also need to be turned completely into zeroes. The important idea is that I’m using the 
first row and first column themselves as storage for the markers, which lets me avoid extra O(m + n) space. The time complexity is O(m × n) because I traverse the matrix a constant number 
of times, and the space complexity is O(1) because I only use a few extra variables.
"""
class Solution:
    # Function to set entire row and column to 0
    # if an element in the matrix is 0
    def setZeroes(self, matrix):

        # Get number of rows and columns
        m = len(matrix)
        n = len(matrix[0])

        # -----------------------------------
        # STEP 1: SAVE
        # -----------------------------------

        # Check if the first row originally contains a zero
        first_row_zero = False

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if the first column originally contains a zero
        first_col_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # -----------------------------------
        # STEP 2: MARK
        # -----------------------------------

        # Traverse the inner matrix.
        # Use first column to mark rows.
        # Use first row to mark columns.
        for i in range(1, m):
            for j in range(1, n):

                if matrix[i][j] == 0:

                    # Mark row i
                    matrix[i][0] = 0

                    # Mark column j
                    matrix[0][j] = 0

        # -----------------------------------
        # STEP 3: ZERO
        # -----------------------------------

        # Use the markers to zero the inner matrix
        for i in range(1, m):
            for j in range(1, n):

                # If the row OR column is marked,
                # make the current element zero
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # -----------------------------------
        # STEP 4: FINISH
        # -----------------------------------

        # Zero the first row if it originally had a zero
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column if it originally had a zero
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# Driver code
matrix = [
    [1, 0, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create Solution object
obj = Solution()

# Modify matrix
obj.setZeroes(matrix)

# Print final matrix
print("Matrix after setting zeroes:")

for row in matrix:
    print(row)