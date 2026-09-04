"""
I’m using a four-boundary approach to traverse the matrix in spiral order. I keep four variables: top, bottom, left, and right, which represent the current boundaries that I still need to 
process. For every layer of the matrix, I follow four steps. First, I traverse the top row from left to right, then increment top because that row is finished. Second, I traverse the right 
column from top to bottom, then decrement right because that column is finished. Third, if top <= bottom, I traverse the bottom row from right to left, then decrement bottom. Fourth, if 
left <= right, I traverse the left column from bottom to top, then increment left. I keep repeating these four directions while top <= bottom and left <= right, which basically moves the 
boundaries inward one layer at a time until the entire matrix has been visited. The two extra checks before traversing the bottom row and left column are important because when the matrix 
gets down to a single remaining row or column, they prevent me from adding the same elements twice. The time complexity is O(m × n) because every element in the matrix is visited exactly 
once, and the space complexity is O(1) auxiliary space because I only use four boundary variables; the result list itself takes O(m × n) space because it stores every matrix element.
"""
class Solution:
    # Function to traverse a matrix in spiral order
    def spiralOrder(self, matrix):

        # Handle empty matrix
        if not matrix:
            return []

        result = []

        # Initialize the four boundaries
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # Continue while valid rows and columns remain
        while top <= bottom and left <= right:

            # -----------------------------------
            # STEP 1: Traverse TOP row
            # Left -> Right
            # -----------------------------------
            for j in range(left, right + 1):
                result.append(matrix[top][j])

            # Top row is finished
            top += 1

            # -----------------------------------
            # STEP 2: Traverse RIGHT column
            # Top -> Bottom
            # -----------------------------------
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])

            # Right column is finished
            right -= 1

            # -----------------------------------
            # STEP 3: Traverse BOTTOM row
            # Right -> Left
            # -----------------------------------
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])

                # Bottom row is finished
                bottom -= 1

            # -----------------------------------
            # STEP 4: Traverse LEFT column
            # Bottom -> Top
            # -----------------------------------
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])

                # Left column is finished
                left += 1

        return result


# Driver code
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Create Solution object
obj = Solution()

# Get spiral traversal
result = obj.spiralOrder(matrix)

print("Spiral traversal:")
print(result)