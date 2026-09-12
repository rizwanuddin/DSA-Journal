"""
Minimum in Rotated Sorted Array
Problem Statement:
Given an integer array arr of size N, sorted in ascending order (with distinct values), the array
is rotated at any index which is unknown. Find the minimum element in the array.

FIND MINIMUM IN ROTATED SORTED ARRAY — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array that has been rotated.

I need to find and return the minimum element in the array."


2. BRUTE FORCE

"The straightforward approach would be to go through the entire array
and keep track of the smallest element.

This would work, but it would take O(n) time."


3. OPTIMIZE

"Since the array was originally sorted and then rotated, I can optimize
this using binary search.

I can use the middle element and the rightmost element to determine
which side contains the minimum."


4. KEY OBSERVATION

"The key observation is to compare arr[mid] with arr[high].

If arr[mid] is greater than arr[high], that means the rotation and the
minimum must be to the RIGHT of mid.

So I can set low to mid + 1.

Otherwise, the minimum could be at mid or somewhere to its LEFT.

So I set high to mid.

I keep doing this until low and high meet, and that position contains
the minimum element."


5. APPROACH

"I'll initialize low at the beginning and high at the end.

While low is less than high, I'll calculate mid.

If arr[mid] is greater than arr[high], I'll move low to mid + 1 because
the minimum must be on the right side.

Otherwise, I'll set high to mid because mid itself could still be the
minimum.

When low and high become equal, only one possible position remains, so
I'll return arr[low]."


6. WHILE CODING

"I'm using low < high because I'm trying to narrow the search down to
one remaining position.

I'm comparing arr[mid] with arr[high].

If arr[mid] > arr[high], the minimum must be after mid, so I'm setting
low to mid + 1.

Otherwise, the minimum could actually be arr[mid], so I cannot remove
mid. That's why I'm setting high to mid instead of mid - 1.

Once low equals high, I've found the minimum."


7. EDGE CASES

"Some edge cases I would consider are an array with one element, an
array that has not been rotated, and the minimum being at the beginning
or end.

This version assumes there are no duplicate elements."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space after
every comparison.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:

Compare MID with HIGH


arr[mid] > arr[high]
→ minimum is to the RIGHT
→ low = mid + 1


arr[mid] <= arr[high]
→ minimum is at MID or to the LEFT
→ high = mid


Stop when:

low == high

→ return arr[low]


IMPORTANT:

Why high = mid and NOT mid - 1?

→ Because arr[mid] could itself be the minimum.
→ So we cannot eliminate mid.


Example:

[4, 5, 6, 7, 0, 1, 2]

Eventually:

        low
         ↓
[4, 5, 6, 7, 0, 1, 2]
            ↑
           high

low == high

→ minimum = 0
"""
class Solution:
    def find_min(self, arr):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (high + low) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        return arr[low]
# Input array
arr = [4, 5, 6, 7, 0, 1, 2]
# Create object of Solution
sol = Solution()
result = sol.find_min(arr)
print("Minimum element is", result)

"""
Important-- so since theres obvously going to be a minimum value we do while low < high cause we
dont need to open the loop again
and out loop return num[low] because by the time the loop finishes its already low == high so 
thats obv the last min element
"""
