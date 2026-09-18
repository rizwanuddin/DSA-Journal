"""
Median of Row Wise Sorted Matrix
Problem Statement:
Given a row-wise sorted matrix of size M*N, where M is no. of rows and N is 
no. of columns, find the median in the given matrix.
Note: M*N is odd.

Examples
Input: M = 3, N = 3, matrix[][] =
1 4 9 
2 5 6
3 8 7
Output: 5
Explanation: 
If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. 
Therefore, median = 5
Input: M = 3, N = 3, matrix[][] =
1 3 8 
2 3 4
1 2 5
Output: 3
Explanation: 
If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8. 
Therefore, median = 3.



MEDIAN OF A ROW-WISE SORTED MATRIX — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
matrix where every row is individually sorted.

I need to find the median of all the elements in the matrix without
merging all the rows into one sorted array."


2. BRUTE FORCE

"The straightforward approach would be to put all the matrix elements
into one array, sort that array, and return the middle element.

This would work, but sorting all N * M elements would take
O(N * M * log(N * M)) time and also require extra space."


3. OPTIMIZE

"We can optimize this using binary search on the possible median value.

Since every row is sorted, for any value mid, I can efficiently count
how many elements in the entire matrix are less than or equal to mid.

Then I can use that count to decide whether my median should be larger
or smaller."


4. KEY OBSERVATION

"The key observation is that I'm binary searching over VALUES, not
matrix indices.

For every possible value mid, I ask:

How many actual matrix elements are less than or equal to mid?

Since each row is sorted, I can use upper bound in every row to find
the first element greater than mid.

That index also tells me how many elements in that row are less than
or equal to mid.

After adding the counts from all rows, I can determine whether mid is
before or after the median position."


5. APPROACH

"First, I'll find the smallest and largest possible values in the
matrix.

Since every row is sorted, the smallest value in each row is at index
0 and the largest is at index M - 1.

So I'll use those values to create my binary search range.

Then I'll calculate the median index using:

half = (N * M) // 2

For every mid value, I'll go through each row and use upper bound to
count how many elements are less than or equal to mid.

If count <= half, there aren't enough elements on the left yet, so my
median must be larger and I'll search right.

Otherwise, I've reached or passed the median position, so I'll search
left.

When binary search finishes, low will contain the median."


6. WHILE CODING

"I'm first finding the minimum and maximum values in the matrix to
create my binary search range."

low = min(low, mat[row][0])
high = max(high, mat[row][M - 1])

"I'm calculating the middle position among all N * M elements."

half = (N * M) // 2

"Now mid is not an index. It's a possible median VALUE."

mid = (low + high) // 2

"For every row, I'm using upper bound to find the first element greater
than mid."

if mat[row][middle] > mid:
    ans = middle
    right = middle - 1
else:
    left = middle + 1

"Since ans is the index of the first element greater than mid, ans also
equals the number of elements less than or equal to mid in that row."

count += ans

"If count is still less than or equal to the median index, I need a
larger value."

if count <= half:
    low = mid + 1

"Otherwise, I've reached or passed the median position, so I'll search
for a smaller possible value."

else:
    high = mid - 1


7. EDGE CASES

"If the matrix could be empty, I should handle that before accessing
mat[0]."

if not mat or not mat[0]:
    return -1

"If a row has no element less than or equal to mid, upper bound remains
0, which correctly adds zero elements."

ans = M

# Binary search can eventually make:
ans = 0

"If every element in a row is less than or equal to mid, upper bound
remains M, which correctly counts every element in that row."

ans = M

"This implementation assumes the standard problem where N * M is odd,
so there is one middle element."


8. COMPLEXITY

"Let the value range be:

V = maximum value - minimum value

The outer binary search takes O(log V) iterations.

For every possible median value, I process N rows, and upper bound in
each row takes O(log M).

So the total time complexity is O(N * log M * log V).

The space complexity is O(1) because I only use a constant number of
extra variables."
"""
class Solution:
    def median(self, mat):

        N = len(mat)
        M = len(mat[0])

        # Find smallest and largest values in the matrix
        low = float("inf")
        high = float("-inf")

        for row in range(N):
            low = min(low, mat[row][0])
            high = max(high, mat[row][M - 1])

        # Median index
        half = (N * M) // 2

        while low <= high:

            # Guess a possible median value
            mid = (low + high) // 2

            # Count how many elements are <= mid
            count = 0

            for row in range(N):

                # Binary search / upper bound inside this row
                left = 0
                right = M - 1
                ans = M

                while left <= right:

                    middle = (left + right) // 2

                    # Find first element > mid
                    if mat[row][middle] > mid:
                        ans = middle
                        right = middle - 1

                    else:
                        left = middle + 1

                # ans = number of elements <= mid in this row
                count += ans

            # Haven't reached median position yet
            if count <= half:
                low = mid + 1

            # Reached/passed median position
            else:
                high = mid - 1

        return low


# Driver code
mat = [
    [1, 3, 8],
    [2, 3, 4],
    [1, 2, 5]
]

obj = Solution()

result = obj.median(mat)

print("Median:", result)