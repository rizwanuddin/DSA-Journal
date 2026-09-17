"""
Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays.
The median is defined as the middle value of a sorted list of numbers. 
In case the length of the list is even, the median is the average of the two middle elements.

Example 1
Input: arr1 = [2, 4, 6], arr2 = [1, 3, 5]
Output: 3.5
Explanation: The array after merging arr1 and arr2 will be [ 1, 2, 3, 4, 5, 6 ]. As the length of the merged list is even, 
the median is the average of the two middle elements. Here two medians are 3 and 4. 
So the median will be the average of 3 and 4, which is 3.5.
Example 2
Input: arr1 = [2, 4, 6], arr2 = [1, 3]
Output: 3.0
Explanation: The array after merging arr1 and arr2 will be [ 1, 2, 3, 4, 6 ]. The median is simply 3.      
"""
class Solution:
    def find_median(self, arr1, arr2):

        # Always use the smaller array for binary search
        if len(arr1) > len(arr2):
            return self.find_median(arr2, arr1)

        n1 = len(arr1)
        n2 = len(arr2)

        low = 0
        high = n1

        # How many total elements should be in LEFT AREA
        left_size = (n1 + n2 + 1) // 2

        while low <= high:

            # How many elements we take from each array
            cut1 = (low + high) // 2
            cut2 = left_size - cut1

            # -------- ARR1 CUT --------

            if cut1 == 0:
                left1 = float("-inf")
            else:
                left1 = arr1[cut1 - 1]

            if cut1 == n1:
                right1 = float("inf")
            else:
                right1 = arr1[cut1]

            # -------- ARR2 CUT --------

            if cut2 == 0:
                left2 = float("-inf")
            else:
                left2 = arr2[cut2 - 1]

            if cut2 == n2:
                right2 = float("inf")
            else:
                right2 = arr2[cut2]

            # Correct cut
            if left1 <= right2 and left2 <= right1:

                # Odd number of total elements
                if (n1 + n2) % 2 == 1:
                    return max(left1, left2)

                # Even number of total elements
                else:
                    left_max = max(left1, left2)
                    right_min = min(right1, right2)

                    return (left_max + right_min) / 2

            # Took too many elements from arr1
            elif left1 > right2:
                high = cut1 - 1

            # Took too few elements from arr1
            else:
                low = cut1 + 1

"""
```text
MEDIAN OF TWO SORTED ARRAYS — BINARY SEARCH PARTITION

PROBLEM:
We are given two sorted arrays.

Example:

arr1 = [1, 3, 8]
arr2 = [7, 9, 10, 11]

We need to find the median without actually merging both arrays.


MAIN IDEA:

We create an imaginary vertical CUT in both arrays.

The goal is:

COMBINED LEFT AREA | COMBINED RIGHT AREA

such that:

1. The LEFT AREA contains half of the total elements.
2. Every value on the LEFT AREA is <= every value on the RIGHT AREA.


STEP 1: ALWAYS BINARY SEARCH THE SMALLER ARRAY

arr1 = [1, 3, 8]
arr2 = [7, 9, 10, 11]

arr1 is smaller, so we binary search how many elements to take from arr1.


STEP 2: FIND HOW MANY ELEMENTS BELONG ON THE LEFT

Total elements:

3 + 4 = 7

Left side size:

(7 + 1) // 2 = 4

So we want:

LEFT AREA       | RIGHT AREA
4 elements      | 3 elements


STEP 3: CHOOSE A CUT IN arr1

Suppose:

cut1 = 1

This means take 1 element from arr1.

Since LEFT AREA needs 4 total elements:

cut2 = 4 - 1 = 3

So:

             LEFT AREA       |      RIGHT AREA

arr1:           [1]          |       [3, 8]
arr2:        [7, 9, 10]      |       [11]


STEP 4: LOOK ONLY AT THE VALUES AROUND THE CUT

arr1:

[1 | 3, 8]
 ↑   ↑
left1 right1

arr2:

[7, 9, 10 | 11]
         ↑    ↑
       left2 right2


We need:

left1 <= right2
AND
left2 <= right1


For this cut:

1 <= 11 ✅
10 <= 3 ❌

So the cut is wrong.

The LEFT AREA contains 10 while the RIGHT AREA contains 3.

That means we took TOO FEW elements from arr1.

Move the arr1 cut RIGHT.


STEP 5: TRY ANOTHER CUT

cut1 = 2
cut2 = 2

             LEFT AREA       |      RIGHT AREA

arr1:         [1, 3]         |        [8]
arr2:         [7, 9]         |     [10, 11]

Boundary values:

left1 = 3
right1 = 8

left2 = 9
right2 = 10

Check:

3 <= 10 ✅
9 <= 8  ❌

Still wrong.

Again, we took too few from arr1.

Move RIGHT.


STEP 6: CORRECT CUT

cut1 = 3
cut2 = 1

             LEFT AREA       |      RIGHT AREA

arr1:       [1, 3, 8]        |        [ ]
arr2:          [7]           |    [9, 10, 11]

Boundary values:

left1 = 8
right1 = +infinity

left2 = 7
right2 = 9

Check:

8 <= 9 ✅
7 <= infinity ✅

Correct partition.


Conceptually:

LEFT AREA        | RIGHT AREA
[1, 3, 7, 8]    | [9, 10, 11]


STEP 7: FIND MEDIAN

If total length is ODD:

median = max(left1, left2)

Here:

max(8, 7) = 8


If total length is EVEN:

median =
(max(left1, left2) + min(right1, right2)) / 2


BINARY SEARCH MOVEMENT:

left1 > right2
→ took TOO MANY from arr1
→ move cut LEFT

left2 > right1
→ took TOO FEW from arr1
→ move cut RIGHT

Both conditions valid
→ correct partition
→ calculate median


MAIN VISUAL:

arr1: [ LEFT PART | RIGHT PART ]
arr2: [ LEFT PART | RIGHT PART ]

               ↓

       COMBINED LEFT | COMBINED RIGHT

Goal:

everything on LEFT <= everything on RIGHT
```

"""