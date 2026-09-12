"""
Find out how many times the array has been rotated
Problem Statement: Given an integer array arr of size N, sorted in ascending order (with 
distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many 
times the array has been rotated.

COUNT ROTATIONS IN A SORTED ROTATED ARRAY — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array that has been rotated.

I need to find how many times the array was rotated."


2. BRUTE FORCE

"The straightforward approach would be to scan the array and find the
minimum element.

The index of the minimum element tells me the number of rotations.

This would work, but it would take O(n) time."


3. OPTIMIZE

"Since the array was originally sorted, I can use binary search to find
the minimum element more efficiently.

Once I find the minimum element, its index is also the number of
rotations."


4. KEY OBSERVATION

"The key observation is:

NUMBER OF ROTATIONS = INDEX OF THE MINIMUM ELEMENT.

For example:

[4, 5, 6, 7, 0, 1, 2]

The minimum element is 0 at index 4.

There are four elements before 0, which means the original sorted array
was rotated 4 times.

So instead of directly counting rotations, I can find the index of the
minimum element."


5. APPROACH

"I'll initialize low at the beginning and high at the end.

While low is less than high, I'll calculate mid.

I'll compare arr[mid] with arr[high].

If arr[mid] is greater than arr[high], the minimum must be to the right
of mid, so I'll set low to mid + 1.

Otherwise, the minimum could be at mid or somewhere to its left, so I'll
set high to mid.

Eventually, low and high will meet at the minimum element.

Instead of returning arr[low], I'll return low because the index of the
minimum element is the number of rotations."


6. WHILE CODING

"I'm using the same binary search that I would use to find the minimum
element in a rotated sorted array.

If arr[mid] > arr[high], I know the minimum is to the right, so I move
low to mid + 1.

Otherwise, the minimum could be at mid or to its left, so I set high
equal to mid.

Once low equals high, low is the index of the minimum element.

Since the index of the minimum equals the number of rotations, I return
low."


7. EDGE CASES

"Some edge cases I would consider are an array with one element, an
array that has not been rotated at all, and an array rotated almost
completely.

This version assumes there are no duplicate elements."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space after
every comparison.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:

ROTATIONS = INDEX OF MINIMUM


Example:

Original:
[0, 1, 2, 4, 5, 6, 7]

After 4 rotations:
[4, 5, 6, 7, 0, 1, 2]
             ↑
          minimum
          index = 4

Therefore:

rotations = 4


BINARY SEARCH RULE:

Compare MID with HIGH


arr[mid] > arr[high]
→ minimum is RIGHT
→ low = mid + 1


arr[mid] <= arr[high]
→ minimum is at MID or LEFT
→ high = mid


When:

low == high

→ low = index of minimum
→ low = number of rotations


EASIEST WAY TO REMEMBER:

Find minimum element
        ↓
Get its index
        ↓
That index = number of rotations


FIND MINIMUM vs FIND ROTATIONS:

Find minimum:
→ return arr[low]

Find rotations:
→ return low
"""
class Solution:
    def find_rotations(self, arr):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        return low
# Input array
arr = [4, 5, 6, 7, 0, 1, 2]
# Create object of Solution
sol = Solution()
rotations = sol.find_rotations(arr)
print(rotations)