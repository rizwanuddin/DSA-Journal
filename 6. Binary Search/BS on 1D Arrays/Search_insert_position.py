"""
Search Insert Position
Problem Statement: You are given a sorted array arr of distinct values and a target value x. You 
need to search for the index of the target value in the array.

SEARCH INSERT POSITION — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array and a target value x.

If x already exists, I need to return its index. If it does not exist,
I need to return the index where it should be inserted so that the array
remains sorted."


2. BRUTE FORCE

"The straightforward approach would be to go through the array from
left to right and find the first element that is greater than or equal
to x.

That index would be the correct insertion position.

This works, but in the worst case I would check every element, giving
O(n) time complexity."


3. OPTIMIZE

"Since the array is sorted, I can optimize this using binary search.

To find the correct index where the target should be inserted, I
basically need to find the LOWER BOUND of x.

The lower bound gives me the first index where arr[i] is greater than
or equal to x, which is exactly where x belongs in sorted order."


4. KEY OBSERVATION

"The key observation is that SEARCH INSERT POSITION is basically a
LOWER BOUND problem.

Lower Bound = first index where arr[i] >= x.

If arr[mid] is greater than or equal to x, mid could be the insertion
position, so I save it and continue searching left for an earlier
position.

If arr[mid] is smaller than x, then x has to come after mid, so I
search to the right."


5. APPROACH

"I'll initialize low to 0 and high to the last index.

I'll initialize ans to n. This handles the case where x is greater than
every element and therefore needs to be inserted at the end.

While low is less than or equal to high, I'll calculate mid.

If arr[mid] is greater than or equal to x, I'll save mid as a possible
insertion position and search to the left.

Otherwise, I'll search to the right.

When the search space becomes empty, I'll return ans."


6. WHILE CODING

"I'm initializing low and high as the boundaries of my search space.

I'm setting ans to n because if the target is larger than every element,
its insertion position will be at the end of the array.

I'm checking arr[mid] >= x because I'm looking for the lower bound.

If this condition is true, mid could be my answer, but I'm searching
left to see if there is an earlier valid position.

Otherwise, arr[mid] is smaller than x, so I move low to mid + 1 and
search to the right."


7. EDGE CASES

"Some edge cases I would consider are an empty array, the target already
existing in the array, the target being smaller than every element, and
the target being larger than every element."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space by
half after every comparison.

The space complexity is O(1) because I only use a constant number of
variables such as low, high, mid, and ans."


MAIN RULE TO REMEMBER:

Search Insert Position = Find the LOWER BOUND of target

Lower Bound = first index where arr[i] >= x


arr[mid] >= x
→ possible insertion position
→ save mid
→ search LEFT

arr[mid] < x
→ target belongs further right
→ search RIGHT


Example:

arr = [1, 2, 4, 7]
x = 6

First value >= 6 is 7
7 is at index 3

So 6 should be inserted at index 3:

[1, 2, 4, 6, 7]
         ↑
       index 3
"""
class BinarySearchInsert:
    def search_insert(self, arr, x):
        low = 0
        high = len(arr) - 1
        n = len(arr)
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                left = mid + 1
        return ans
# Main execution
if __name__ == "__main__":
    arr = [1, 2, 4, 7]
    x = 6
    obj = BinarySearchInsert()
    index = obj.search_insert(arr, x)
    print(f"The index is: {index}")
"""
Lower bound finds the **first index where the value is greater than or equal to `x` (`>= x`)**, while **upper bound** finds the **first index where the value is strictly greater than `x` (`> x`)**. We use lower bound for **Search Insert Position** because it gives the position where `x` already exists, or where `x` should be inserted if it doesn't exist. Upper bound would place `x` **after any existing equal values**, which is not what Search Insert Position asks for.

"""