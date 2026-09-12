"""
Search Element in Rotated Sorted Array II
Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain 
duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to 
you. Return True if k is present and otherwise, return False. 

SEARCH IN ROTATED SORTED ARRAY II — WITH DUPLICATES


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array that has been rotated, and this time the array can contain
duplicate values.

I need to determine whether the target x exists in the array.

If it exists, I'll return True. Otherwise, I'll return False."


2. BRUTE FORCE

"The straightforward approach would be to go through the entire array
and check every element for the target.

This would work, but it would take O(n) time."


3. OPTIMIZE

"Since the array was originally sorted, I can still use a modified
binary search.

Just like the rotated array problem without duplicates, I'll try to
identify which half is sorted and determine whether the target is
inside that half.

However, duplicates create one extra situation that I need to handle."


4. KEY OBSERVATION

"The main difference from the version without duplicates is that
sometimes arr[low], arr[mid], and arr[high] can all be equal.

For example:

[3, 1, 2, 3, 3, 3, 3]

If low, mid, and high all contain 3, I cannot clearly determine which
half is sorted because the duplicate values hide the rotation.

So when:

arr[low] == arr[mid] == arr[high]

I'll shrink the search space from both sides by doing:

low += 1
high -= 1

Then I'll continue the binary search normally."


5. APPROACH

"I'll initialize low and high as the boundaries of my search space.

While low is less than or equal to high, I'll calculate mid.

First, if arr[mid] equals x, I'll return True.

Then I'll handle the duplicate case. If arr[low], arr[mid], and
arr[high] are all equal, I'll increment low and decrement high and
continue to the next iteration.

Otherwise, I'll determine which half is sorted.

If the left half is sorted, I'll check whether the target falls inside
that range. If it does, I'll search left; otherwise, I'll search right.

If the right half is sorted, I'll check whether the target falls inside
that range. If it does, I'll search right; otherwise, I'll search left.

If the search space becomes empty, I'll return False."


6. WHILE CODING

"I'm first checking whether mid is the target.

Then I'm handling the special duplicate case.

If low, mid, and high all have the same value, I can't reliably tell
which side contains the rotation, so I'm shrinking both boundaries.

After handling that, the remaining logic is the same as normal rotated
binary search.

I find the sorted half, check whether the target is inside its range,
and either search that half or eliminate it."


7. EDGE CASES

"Some edge cases I would consider are an array with one element, all
elements being the same, the target not existing, the target appearing
multiple times, and duplicates hiding the rotation point."


8. COMPLEXITY

"The average time complexity is O(log n) because binary search normally
eliminates half of the search space.

However, because of duplicates, the worst-case time complexity can
become O(n). For example, if many elements are equal, I may only be
able to shrink low and high one position at a time.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:


NORMAL ROTATED BINARY SEARCH:

Find sorted half
→ Is target inside?
→ YES: search there
→ NO: search other half


ONE EXTRA RULE FOR DUPLICATES:

arr[low] == arr[mid] == arr[high]

→ Can't tell which half is useful
→ low++
→ high--
→ continue


THEN NORMAL LOGIC:

LEFT SORTED:
arr[low] <= arr[mid]

    target inside left?
    → go LEFT

    otherwise
    → go RIGHT


RIGHT SORTED:

    target inside right?
    → go RIGHT

    otherwise
    → go LEFT


BIGGEST DIFFERENCE:

Rotated Array I
→ No duplicates
→ O(log n)

Rotated Array II
→ Duplicates allowed
→ Same logic + one duplicate check
→ O(log n) average
→ O(n) worst case
"""
class Solution:
    def search_ii(self, arr, x):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return True
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
            if arr[low] <= arr[mid]:
                if arr[low] <= x < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] < x <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    x = 3
    sol = Solution()
    result = sol.search_ii(arr, x)
    if result:
        print("Target is present in the array.")
    else:
        print("Target is not present.")
"""
Duplicates themselves aren't the problem. The problem is when arr[low] == arr[mid] == arr[high], 
because then the duplicates can hide which half contains the rotation. We shrink both ends until 
that ambiguity disappears.
"""


