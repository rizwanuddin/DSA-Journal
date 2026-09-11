"""
Last occurrence in a sorted array
Problem Statement: Given a sorted array of N integers, write a program to find the index of the 
last occurrence of the target key. If the target is not found then return -1. Note: Consider 0 
based indexing 

LAST OCCURRENCE — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array and a target value x.

I need to find the index of the last occurrence of x.

If x does not exist in the array, I'll return -1."


2. BRUTE FORCE

"The straightforward approach would be to go through the entire array
and whenever I find x, save its index.

After checking the entire array, the saved index would be the last
occurrence.

This would work, but it would take O(n) time."


3. OPTIMIZE

"Since the array is sorted, I can optimize this using binary search.

Instead of stopping when I find x, I can save its index and continue
searching to the right for a later occurrence."


4. KEY OBSERVATION

"The key observation is that finding x does not mean I'm done.

If arr[mid] equals x, mid is a possible answer, so I'll save it and
continue searching to the RIGHT because there might be another x at a
larger index.

If arr[mid] is smaller than x, I'll also search right.

If arr[mid] is greater than x, I'll search left."


5. APPROACH

"I'll initialize low to 0 and high to the last index.

I'll initialize ans to -1 in case the target does not exist.

While low is less than or equal to high, I'll calculate mid.

If arr[mid] equals x, I'll save mid in ans and move low to mid + 1
because I'm looking for the last occurrence.

If arr[mid] is smaller than x, I'll search to the right.

Otherwise, I'll search to the left.

When the search space becomes empty, I'll return ans."


6. WHILE CODING

"I'm initializing ans to -1 in case the target isn't found.

I'm using normal binary search to find the target.

The important difference is that when I find x, I don't immediately
return.

I save mid as a possible answer and continue searching to the right
because I want the LAST occurrence.

If I find x again, ans will simply be updated to the later index."


7. EDGE CASES

"Some edge cases I would consider are an empty array, the target not
being present, the target appearing only once, the target appearing
multiple times, and every element being equal to the target."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space by
half after every comparison.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:

LAST OCCURRENCE:

arr[mid] == x
→ save mid
→ search RIGHT


FIRST OCCURRENCE:

arr[mid] == x
→ save mid
→ search LEFT


So the easiest way to remember it:

FIRST occurrence → find it, then go LEFT
LAST occurrence  → find it, then go RIGHT
"""
class Solution:
    def last_occurence(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                ans = mid
                low = mid + 1
            elif arr[mid] < x :
                low = mid + 1
            else :
                high = mid - 1
        return ans
arr = [1, 2, 3, 3, 3, 4, 5]
x = 3
obj = Solution()
index = obj.last_occurrence(arr, x)
print("Last occurrence is at index:", index)



