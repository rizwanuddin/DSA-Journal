"""
Peak element in Array

Problem Statement: Given an array of length N, peak element is defined as the element greater 
than both of its neighbors. Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and 
arr[i + 1] < arr[i]. Find the index(0-based) of a peak element in the array. If there are 
multiple peak numbers, return the index of any peak number. 

FIND PEAK ELEMENT — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array and I need to find a peak element.

A peak is an element that is greater than its neighboring elements.

I need to return the index of any valid peak."


2. BRUTE FORCE

"The straightforward approach would be to go through the array and
compare every element with its neighbors.

If an element is greater than both neighbors, I can return its index.

This would work, but in the worst case it would take O(n) time."


3. OPTIMIZE

"We can optimize this using binary search.

Instead of checking every element, I can look at the direction of the
array around mid and determine which side must contain a peak."


4. KEY OBSERVATION

"The key observation is that I can compare arr[mid] with arr[mid + 1].

If arr[mid] < arr[mid + 1], I'm going uphill, so there must be a peak
somewhere to the right.

If arr[mid] > arr[mid + 1], I'm going downhill, so a peak can be at mid
or somewhere to the left.

This lets me eliminate part of the array after every comparison."


5. APPROACH

"I'll initialize low at the beginning and high at the last index.

While low is less than high, I'll calculate mid.

If arr[mid] is smaller than arr[mid + 1], I'm going uphill, so I'll
move low to mid + 1.

Otherwise, I'm going downhill, so the peak could be at mid or to the
left. I'll set high to mid.

Eventually low and high will meet at a peak, and I'll return that
index."


6. WHILE CODING

"I'm using low < high because I'm narrowing the search space until only
one possible peak position remains.

I'm comparing arr[mid] with arr[mid + 1].

If arr[mid] < arr[mid + 1], I'm going uphill, so I'm searching right.

Otherwise, I'm going downhill, so I'm keeping mid in the search space
and searching toward the left.

That's why I use high = mid instead of mid - 1, because mid itself
could be the peak.

When low equals high, I've found a peak index."


7. EDGE CASES

"Some edge cases I would consider are an array with only one element,
a completely increasing array, a completely decreasing array, and a
peak occurring somewhere in the middle.

For this version, I'm assuming adjacent elements are not equal."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space after
every comparison.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:

Compare:

arr[mid] with arr[mid + 1]


arr[mid] < arr[mid + 1]

→ going UPHILL
→ peak is on the RIGHT
→ low = mid + 1


arr[mid] > arr[mid + 1]

→ going DOWNHILL
→ peak is at MID or LEFT
→ high = mid


EASIEST WAY TO REMEMBER:

UPHILL   ↗ → go RIGHT

DOWNHILL ↘ → keep MID and go LEFT


Stop when:

low == high

→ return low
→ this is a peak index
"""
class Solution:
    def search_peak(self, arr):
        low = 0
        high = len(arr) - 1
        while low < high :
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                # Going uphill → peak exists on the right
                low = mid + 1
            else:
                # Going downhill → peak is at mid or on the left
                high = mid
        return low

"""
A peak is an element that is bigger than its immediate neighbors.Peak = local maximum, NOT 
necessarily the largest number in the whole array.
"""