"""
K-th Element of two sorted arrays
Problem Statement: Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.

Examples
Example 1:
Input:
 a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5  
Output:
 6  
Explanation:
 The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
Example 2:
Input:
 a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7  
Output:
 256  
Explanation:
 The final sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element of this array is 256.

 

MEDIAN OF TWO SORTED ARRAYS — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given two
sorted arrays.

I need to find the median of the two arrays as if they were combined
into one sorted array, but I want to do it without actually merging
them."


2. BRUTE FORCE

"The straightforward approach would be to merge both sorted arrays into
one sorted array and then find the middle element.

This would take O(n1 + n2) time and O(n1 + n2) extra space.

Since both arrays are already sorted, we can do better."


3. OPTIMIZE

"We can optimize this using binary search.

Instead of merging the arrays, I'll divide both arrays into a LEFT side
and a RIGHT side.

I want the left side to contain half of the total elements, and every
element on the left should be less than or equal to every element on
the right.

I'll binary search how many elements I should take from the first array."


4. KEY OBSERVATION

"The key observation is that I don't need to know every element in the
left and right sides.

I only need to know the four elements around the cuts:

left1  = largest element taken from arr1
right1 = first element not taken from arr1

left2  = largest element taken from arr2
right2 = first element not taken from arr2

I have the correct partition when:

left1 <= right2

and

left2 <= right1

That means everything on the left belongs before everything on the
right."


5. APPROACH

"First, I'll always binary search the smaller array because that gives
me the better time complexity.

I'll calculate how many total elements should be on the left side using:

left_size = (n1 + n2 + 1) // 2

Then I'll binary search a cut position in arr1.

cut1 tells me how many elements I'm taking from arr1.

Since the total number of elements on the left must stay fixed, I can
calculate:

cut2 = left_size - cut1

Then I'll get the four boundary values around those cuts.

If the partition is correct, I can calculate the median.

If the total number of elements is odd, the median is the largest value
on the left side.

If the total is even, the median is the average of the largest value on
the left and the smallest value on the right.

If left1 > right2, I've taken too many elements from arr1, so I move
the cut left.

Otherwise, I've taken too few elements from arr1, so I move the cut
right."


6. WHILE CODING

"I'm first making sure arr1 is the smaller array because that's the one
I want to binary search."

if len(arr1) > len(arr2):
    return self.find_median(arr2, arr1)

"I'm binary searching the number of elements taken from arr1, so my
search range is from 0 to n1."

low = 0
high = n1

"I'm calculating how many total elements should belong on the left."

left_size = (n1 + n2 + 1) // 2

"cut1 is how many elements I'm taking from arr1, and cut2 is how many
I need from arr2."

cut1 = (low + high) // 2
cut2 = left_size - cut1

"I'm using negative and positive infinity when a cut is at the edge so
I don't go outside the array."

if cut1 == 0:
    left1 = float("-inf")

if cut1 == n1:
    right1 = float("inf")

"I'm checking whether the partition is valid."

if left1 <= right2 and left2 <= right1:

"If the total length is odd, I return the largest value from the left
side."

return max(left1, left2)

"If the total length is even, I take the largest value from the left
and the smallest value from the right and average them."

return (max(left1, left2) + min(right1, right2)) / 2

"If left1 > right2, I took too much from arr1, so I move left."

high = cut1 - 1

"Otherwise, I took too little from arr1, so I move right."

low = cut1 + 1


7. EDGE CASES

"If arr1 is larger than arr2, I'll swap them so binary search always
runs on the smaller array."

if len(arr1) > len(arr2):
    return self.find_median(arr2, arr1)

"If one array is empty, the infinity values around the cuts allow the
same logic to still work."

if cut1 == 0:
    left1 = float("-inf")

if cut1 == n1:
    right1 = float("inf")

if cut2 == 0:
    left2 = float("-inf")

if cut2 == n2:
    right2 = float("inf")

"If both arrays are empty, there is no valid median, so if the problem
does not guarantee at least one element, I should handle that."

if not arr1 and not arr2:
    return None

"I also assume both input arrays are already sorted, because the
partition logic depends on that."


8. COMPLEXITY

"Let n1 be the size of the smaller array and n2 be the size of the
larger array.

The time complexity is O(log(min(n1, n2))) because I only binary search
the smaller array.

The space complexity is O(1) because I only use a constant number of
variables."
"""
class Solution:
    def kth_element(self, a, b, k):

        # Always binary search the smaller array
        if len(a) > len(b):
            return self.kth_element(b, a, k)

        n1 = len(a)
        n2 = len(b)

        # cut1 cannot be less than k - n2,
        # otherwise we would need more than n2 elements from b
        low = max(0, k - n2)

        # cut1 cannot be more than k or more than n1
        high = min(k, n1)

        while low <= high:

            # cut1 = how many elements we take from a into LEFT AREA
            cut1 = (low + high) // 2

            # cut2 = remaining elements needed from b
            # so that LEFT AREA has exactly k elements
            cut2 = k - cut1

            # We binary search cut1 inside array a
            # and cut2 adjusts automatically in array b

            # Values around the cut in a
            if cut1 == 0:
                left1 = float("-inf")
            else:
                left1 = a[cut1 - 1]

            if cut1 == n1:
                right1 = float("inf")
            else:
                right1 = a[cut1]

            # Values around the cut in b
            if cut2 == 0:
                left2 = float("-inf")
            else:
                left2 = b[cut2 - 1]

            if cut2 == n2:
                right2 = float("inf")
            else:
                right2 = b[cut2]

            # Correct partition:
            # everything in LEFT AREA is <= everything in RIGHT AREA
            if left1 <= right2 and left2 <= right1:

                # LEFT AREA contains exactly k elements,
                # so the largest value in LEFT AREA is the kth element
                return max(left1, left2)

            # Took too many elements from a
            elif left1 > right2:
                high = cut1 - 1

            # Took too few elements from a
            else:
                low = cut1 + 1  


"""
KTH ELEMENT OF TWO SORTED ARRAYS

Goal:
Find the kth element without actually merging the arrays.

MAIN IDEA:

We create a cut in both arrays so that the LEFT AREA contains
exactly k elements.

                 LEFT AREA   |   RIGHT AREA

a:          [ ... cut1 ...   | ........ ]
b:          [ ... cut2 ...   | ........ ]

cut1 + cut2 = k


We binary search cut1 in the smaller array.

cut2 is automatically:

cut2 = k - cut1


VALUES AROUND THE CUT:

a:
... left1 | right1 ...

b:
... left2 | right2 ...


CORRECT PARTITION:

left1 <= right2
AND
left2 <= right1

If both are true, then everything in LEFT AREA is smaller than
everything in RIGHT AREA.


Since LEFT AREA contains exactly k elements:

kth element = max(left1, left2)


BINARY SEARCH MOVEMENT:

left1 > right2
→ took too many elements from a
→ move cut1 LEFT

left2 > right1
→ took too few elements from a
→ move cut1 RIGHT


WHY LOW AND HIGH:

low = max(0, k - n2)
→ minimum number of elements we MUST take from a

high = min(k, n1)
→ maximum number of elements we CAN take from a


MAIN VISUAL:

a: [ LEFT PART | RIGHT PART ]
b: [ LEFT PART | RIGHT PART ]

          ↓

   COMBINED LEFT | COMBINED RIGHT

LEFT contains exactly k elements
→ answer = largest element on LEFT
"""



