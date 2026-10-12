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



## Median of Two Sorted Arrays

**Clarify:**
- so I'm given two sorted arrays, and I need to find the median if I were to merge them
- if the total count is odd, median is just the middle value, if it's even, it's the average of the two middle values
- and I shouldn't actually merge them, that would be too slow, they probably want something faster

**Brute force:**
- the easy way is just merge both arrays into one sorted array, then grab the middle value or average the two middle values
- that's O(m+n) time, works but there's a faster way using binary search

**Optimize:**
- since both arrays are already sorted, I can binary search on how many elements to take from the smaller array, and figure out the rest from the bigger one
- that gets me down to O(log(min(m,n))) time, which is way better

**Key observation:**
- the whole idea is I'm trying to make an imaginary cut in both arrays, so that everything on the left side of both cuts combined is less than or equal to everything on the right side
- if I decide how many elements come from array one, that automatically tells me how many need to come from array two, since I know exactly how big the left half should be
- so I just need to check, is the last element on the left side of array one less than or equal to the first element on the right side of array two, and the same the other way around for array two and array one
- if both of those checks pass, I've found the correct cut, and I don't even need to merge anything to get the answer

**Approach:**
- always binary search the smaller array, so the search space stays small
- figure out how many total elements should be on the left side, that's just half of the combined length, rounded up
- binary search cut1, which is how many elements I take from array one, and cut2 is just whatever's left needed from array two
- look at the values right around each cut, using negative infinity or positive infinity for edges that go out of bounds
- if the cut is valid, calculate the median based on whether the total count is odd or even
- if not valid, shift the binary search left or right depending on which side was too big

**While coding:**
- first I define the class Solution
- then the function find_median, taking arr1 and arr2
- first thing I do is check if arr1 is bigger than arr2, if it is, I just call the same function again but swapped, so I always binary search the smaller one
- I get n1 and n2 as the lengths of both arrays
- I set low to 0 and high to n1
- I calculate left_size, which is how many elements the combined left side should have, that's n1 plus n2 plus 1, divided by 2
- I start a while loop that runs while low is less than or equal to high
- inside, I calculate cut1 as low plus high divided by 2
- then cut2 is just left_size minus cut1
- now I figure out left1 and right1 from array one — if cut1 is 0, left1 is negative infinity since there's nothing to the left, otherwise it's arr1 at cut1 minus 1, and if cut1 equals n1, right1 is positive infinity since there's nothing to the right, otherwise it's arr1 at cut1
- I do the exact same thing for left2 and right2, but using array two and cut2
- then I check if left1 is less than or equal to right2, and left2 is less than or equal to right1
- if both are true, this is the correct cut, so now I check if the total length is odd, if yes I return the max of left1 and left2
- if the total length is even, I take the max of left1 and left2 as left_max, and the min of right1 and right2 as right_min, and return the average of those two
- if left1 is bigger than right2, that means I took too many from array one, so I bring high down to cut1 minus 1
- otherwise, I took too few from array one, so I push low up to cut1 plus 1

**Edge cases:**
- if one array is empty, the cut logic should still work since infinity handles the missing side
- if both arrays are the same size, nothing special happens, the swap check just doesn't trigger
- if there's only one element total across both arrays, the loop should resolve that immediately

**Complexity:**
- time is O(log(min(m,n))), since I'm only binary searching the smaller array
- space is O(1), not counting the recursion call for swapping, which happens at most once
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