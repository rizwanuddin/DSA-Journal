"""
Implement Upper Bound
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find 
the upper bound of x.

UPPER BOUND — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array and a value x. I need to find the first index whose value
is strictly greater than x.

If no such element exists, I return the length of the array."


2. BRUTE FORCE

"The straightforward approach would be to go through the array from
left to right and return the first index where arr[i] is greater than x.

This would work, but in the worst case I would check every element,
giving O(n) time complexity."


3. OPTIMIZE

"Since the array is already sorted, I can optimize this using binary
search.

Instead of checking every element, I can eliminate half of the remaining
search space after every comparison."


4. KEY OBSERVATION

"The key observation is that I am looking for the first element that is
strictly greater than x.

If arr[mid] is greater than x, mid could be my answer, so I save it.
However, there might be an earlier element that is also greater than x,
so I continue searching to the left.

If arr[mid] is less than or equal to x, it cannot be the upper bound,
so I search to the right."


5. APPROACH

"I'll initialize low to 0 and high to the last index.

I'll initialize ans to the length of the array, which is the default
answer if no element greater than x exists.

While low is less than or equal to high, I'll calculate mid.

If arr[mid] is greater than x, I'll save mid as a possible answer and
move high to mid - 1 to continue searching left.

Otherwise, I'll move low to mid + 1 and search the right side.

When the search space becomes empty, I'll return ans."


6. WHILE CODING

"I'm initializing low and high as the boundaries of my search space.

I'm setting ans to the length of the array in case no element greater
than x exists.

I'm using low <= high because as long as the boundaries haven't crossed,
there are still elements left to search.

If arr[mid] > x, I'm saving mid as a possible answer and searching left
because I want the first valid index.

Otherwise, arr[mid] <= x, so I'm searching to the right."


7. EDGE CASES

"Some edge cases I would consider are an empty array, x being smaller
than every element, x being larger than every element, x existing in
the array, and duplicate values."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space by
half after every comparison.

The space complexity is O(1) because I only use a constant number of
variables such as low, high, mid, and ans."


MAIN RULE TO REMEMBER:

Upper Bound = first index where arr[i] > x

arr[mid] > x
→ save mid
→ search LEFT

arr[mid] <= x
→ search RIGHT


LOWER BOUND VS UPPER BOUND:

Lower Bound → first value >= x

Upper Bound → first value > x
"""
class UpperBoundFinder:
    # Binary search to find upper bound
    def upper_bound(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = len(arr)  # Default to length if no element > x

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > x:
                ans = mid      # Store current mid as answer
                high = mid - 1 # Search left
            else:
                low = mid + 1  # Search right
        return ans

# Driver code
arr = [3, 5, 8, 9, 15, 19]
x = 9

finder = UpperBoundFinder()
ind = finder.upper_bound(arr, x)

print("The upper bound is the index:", ind) 
