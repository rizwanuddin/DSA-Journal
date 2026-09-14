"""
I’m using the transpose + reverse approach to rotate a square matrix 90 degrees clockwise in-place. First, I transpose the matrix, which means 
I swap matrix[i][j] with matrix[j][i], basically turning the rows into columns. I only loop with j starting from i + 1 because I only need to 
swap the elements above the main diagonal; otherwise, I would swap the same elements twice and undo my changes. After transposing, the matrix 
is not fully rotated yet, so the second step is to reverse every row. Reversing each row moves the elements into the correct positions for a 
90-degree clockwise rotation. For example, the original matrix [[1,2,3],[4,5,6],[7,8,9]] first becomes [[1,4,7],[2,5,8],[3,6,9]] after the 
transpose, and after reversing each row it becomes [[7,4,1],[8,5,2],[9,6,3]], which is the desired clockwise rotation. The time complexity is 
O(n²) because we process the elements of the matrix, and the space complexity is O(1) because the rotation is performed in-place without 
creating another matrix.
"""
class Solution:
    # Function to rotate matrix 90 degrees clockwise in-place
    def rotateClockwise(self, matrix):
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                # Swap element at (i, j) with (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            # Reverse the current row to simulate clockwise rotation
            matrix[i].reverse()

# Driver code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = Solution()
obj.rotateClockwise(matrix)

# Print rotated matrix
for row in matrix:
    print(*row)
