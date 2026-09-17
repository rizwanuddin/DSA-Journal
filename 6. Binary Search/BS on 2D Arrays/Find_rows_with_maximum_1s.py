"""
Find the row with maximum number of 1's
Problem Statement: You have been given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s. All the rows are sorted in ascending order. Your task is to find the index of the row with the maximum number of ones. Note: If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1
Examples

Example 1:
Input Format: n = 3, m = 3, 
mat[] = 
1 1 1
0 0 1
0 0 0
Result: 0
Explanation: The row with the maximum number of ones is 0 (0 - indexed).
Example 2:
Input Format: n = 2, m = 2 , 
mat[] = 
0 0
0 0
Result: -1
Explanation:  The matrix does not contain any 1. So, -1 is the answer.


KTH ELEMENT OF TWO SORTED ARRAYS — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given two
sorted arrays and a value k.

I need to find the kth smallest element if both arrays were merged into
one sorted array.

I want to do this without actually merging the arrays."


2. BRUTE FORCE

"The straightforward approach would be to merge both sorted arrays and
then return the element at index k - 1.

That would take O(n1 + n2) time and O(n1 + n2) extra space.

Since both arrays are already sorted, I can do better."


3. OPTIMIZE

"We can optimize this using binary search and partitioning.

Instead of merging the arrays, I'll divide both arrays into a LEFT AREA
and a RIGHT AREA.

I want the LEFT AREA to contain exactly k elements.

Once I find a correct partition, the largest element in the LEFT AREA
will be the kth smallest element."


4. KEY OBSERVATION

"The key observation is that if I take cut1 elements from array a, then
I must take:

cut2 = k - cut1

elements from array b.

That guarantees that the LEFT AREA contains exactly k elements.

Then I only need to check the values around the two cuts.

The partition is correct when:

left1 <= right2

and

left2 <= right1

That means every element in the LEFT AREA is less than or equal to every
element in the RIGHT AREA.

Since the LEFT AREA has exactly k elements, the largest element in that
area is the kth smallest element."


5. APPROACH

"First, I'll always binary search the smaller array to keep the time
complexity low.

I'll calculate the valid binary search range for cut1.

The minimum number of elements I can take from a is:

max(0, k - n2)

because if I take fewer than that, I would need more elements from b
than b actually contains.

The maximum number of elements I can take from a is:

min(k, n1)

because I cannot take more than k total elements or more than n1
elements from a.

Then I'll calculate cut1 using binary search and set:

cut2 = k - cut1

I'll find the four values around the cuts.

If the partition is correct, I'll return max(left1, left2).

If left1 > right2, I've taken too many elements from a, so I'll move
the cut left.

Otherwise, I've taken too few elements from a, so I'll move the cut
right."


6. WHILE CODING

"I'm first making sure a is the smaller array because I want to binary
search the smaller search space."

if len(a) > len(b):
    return self.kth_element(b, a, k)

"I'm setting the smallest possible cut1."

low = max(0, k - n2)

"This prevents cut2 from becoming larger than n2."

"I'm setting the largest possible cut1."

high = min(k, n1)

"This prevents me from taking more than k elements or more elements
than array a contains."

"Now cut1 tells me how many elements I'm taking from a."

cut1 = (low + high) // 2

"And cut2 automatically gives me the remaining elements I need from b."

cut2 = k - cut1

"I'm using negative and positive infinity for cuts at the boundaries
so I don't go outside the arrays."

if cut1 == 0:
    left1 = float("-inf")

if cut1 == n1:
    right1 = float("inf")

"I'm checking whether the partition is valid."

if left1 <= right2 and left2 <= right1:

"If it is valid, the LEFT AREA contains exactly k elements, so the
largest value on the left is the kth smallest element."

return max(left1, left2)

"If left1 > right2, I've taken too many elements from a, so I move
left."

high = cut1 - 1

"Otherwise, I've taken too few elements from a, so I move right."

low = cut1 + 1


7. EDGE CASES

"If k is outside the valid range, there is no kth element."

if k < 1 or k > len(a) + len(b):
    return -1

"If one array is larger than the other, I swap them so I always binary
search the smaller array."

if len(a) > len(b):
    return self.kth_element(b, a, k)

"If a cut takes zero elements from one side, I use negative infinity
for the left value."

if cut1 == 0:
    left1 = float("-inf")

if cut2 == 0:
    left2 = float("-inf")

"If a cut takes every element from an array, I use positive infinity
for the right value."

if cut1 == n1:
    right1 = float("inf")

if cut2 == n2:
    right2 = float("inf")


8. COMPLEXITY

"Let n1 be the size of the smaller array and n2 be the size of the
larger array.

The time complexity is O(log(min(n1, n2))) because I binary search only
the smaller array.

The space complexity is O(1) because I only use a constant number of
variables."
"""

class Solution:
    def row_with_max_ones(self, mat):
        n = len(mat) # No. of rows
        m = len(mat[0]) # No. of Columns

        max_ones = 0
        row_index = -1

        for i in range(n):

            low = 0
            high = m - 1
            first_one = m

            while low <= high:
                mid = (low + high) // 2

                if mat[i][mid] == 1:
                    first_one = mid
                    high = mid - 1
                else:
                    low = mid + 1

            ones = m - first_one

            if ones > max_ones:
                max_ones = ones
                row_index = i

        return row_index


# Driver code
mat = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]

obj = Solution()
result = obj.row_with_max_ones(mat)

print("Row with maximum 1s:", result)



"""
MATRIX INDEXING — PYTHON

mat[i][j]    → element at row i, column j

len(mat)     → number of ROWS

len(mat[0])  → number of COLUMNS

Remember:
i = row
j = column
Indexing starts from 0
"""