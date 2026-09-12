"""
Search Element in a Rotated Sorted Array

Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values)
 and a target value k. The array is rotated at some pivot point that is unknown. Find the index 
 at which k is present and if k is not present return -1.

SEARCH IN ROTATED SORTED ARRAY — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array that was originally sorted but has been rotated, and a target x.

I need to find the index of x.

If x does not exist in the array, I'll return -1."


2. BRUTE FORCE

"The straightforward approach would be to go through the entire array
and check each element until I find x.

This would work, but it would take O(n) time in the worst case."


3. OPTIMIZE

"Since the array was originally sorted, I can still use a modified
binary search.

Even though the entire array is no longer sorted, after choosing mid,
at least one of the two halves will always be sorted.

I can identify that sorted half and use it to decide which side could
contain the target."


4. KEY OBSERVATION

"The key observation is that at every step, either the left half or the
right half is sorted.

I first check which half is sorted.

If the left half is sorted, I check whether the target falls within
the values of that sorted half.

If it does, I search left. Otherwise, I search right.

If the right half is sorted, I do the same thing. If the target falls
inside that range, I search right. Otherwise, I search left.

I repeat this every iteration because after I remove half of the array,
the new search space can still contain the rotation point, so I need
to determine which half is sorted again."


5. APPROACH

"I'll initialize low and high as the boundaries of my search space.

While low is less than or equal to high, I'll calculate mid.

First, if arr[mid] equals x, I'll return mid.

Otherwise, I'll determine which half is sorted.

If arr[low] <= arr[mid], the left half is sorted.

I'll check whether x is between arr[low] and arr[mid].

If it is, I'll search left. Otherwise, I'll search right.

If the left half isn't sorted, then the right half must be sorted.

I'll check whether x is between arr[mid] and arr[high].

If it is, I'll search right. Otherwise, I'll search left.

If the search space becomes empty, I'll return -1."


6. WHILE CODING

"I'm first checking whether mid is the target.

Then I'm checking arr[low] <= arr[mid] to determine whether the left
half is sorted.

If the left half is sorted and the target is inside its range, I move
high to mid - 1.

Otherwise, I move low to mid + 1.

If the left half isn't sorted, then the right half is sorted.

If the target is inside the sorted right half, I move low to mid + 1.

Otherwise, I move high to mid - 1.

I repeat this check every iteration because the remaining search space
may still contain the rotation point."


7. EDGE CASES

"Some edge cases I would consider are an array with one element, the
target being at the rotation point, the target being at either end of
the array, the array not being rotated, and the target not existing.

This version assumes there are no duplicate elements. If duplicates are
allowed, additional handling may be needed."


8. COMPLEXITY

"The time complexity is O(log n) because I eliminate half of the search
space after every iteration.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:


1. CHECK MID

arr[mid] == x
→ return mid


2. FIND WHICH HALF IS SORTED

arr[low] <= arr[mid]
→ LEFT is sorted

otherwise
→ RIGHT is sorted


3. IF LEFT IS SORTED

arr[low] <= x < arr[mid]
→ target is inside LEFT
→ go LEFT

otherwise
→ go RIGHT


4. IF RIGHT IS SORTED

arr[mid] < x <= arr[high]
→ target is inside RIGHT
→ go RIGHT

otherwise
→ go LEFT


SUPER SHORT MEMORY TRICK:

Find sorted half
        ↓
Is target inside it?
        ↓
YES → search that half
NO  → search the other half 
"""
class Solution:
    def search(self, arr, x):
        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = (low + high) // 2

            # Found target
            if arr[mid] == x:
                return mid

            # LEFT HALF IS SORTED
            if arr[low] <= arr[mid]:

                # Target is inside sorted left half
                if arr[low] <= x < arr[mid]:
                    high = mid - 1

                # Target is not there
                else:
                    low = mid + 1

            # RIGHT HALF IS SORTED
            else:

                # Target is inside sorted right half
                if arr[mid] < x <= arr[high]:
                    low = mid + 1

                # Target is not there
                else:
                    high = mid - 1

        return -1

"""
SEARCH IN ROTATED SORTED ARRAY — FULL THINK ALOUD WHILE CODING


"I'm first going to create a class called Solution."

class Solution:


"Inside the class, I'll define a method called search.

It takes arr, which is my rotated sorted array, and x, which is
the target I'm looking for."

    def search(self, arr, x):


"Since this is still based on a sorted array, I'm going to use
binary search.

I'll initialize low at the first index and high at the last index.
These represent my current search space."

        low = 0
        high = len(arr) - 1


"Now I'll continue searching while low is less than or equal to high."

        while low <= high:


"I'll calculate the middle index."

            mid = (low + high) // 2


"First, I'll check whether the middle element itself is my target.

If it is, I can immediately return its index."

            if arr[mid] == x:
                return mid


"Now because the array is rotated, I can't simply compare the target
with arr[mid] like normal binary search.

However, in a rotated sorted array, at least one side of mid will
always be sorted.

So first I'll check whether the LEFT half is sorted.

If arr[low] is less than or equal to arr[mid], then the values from
low through mid are in sorted order."

            if arr[low] <= arr[mid]:


"Now that I know the left half is sorted, I'll check whether my
target lies inside its value range.

The target must be greater than or equal to arr[low] and smaller
than arr[mid]."

                if arr[low] <= x < arr[mid]:


"If that's true, the target must be somewhere in the left half.

So I'll remove the right half by moving high to mid minus one."

                    high = mid - 1


"Otherwise, the target is not inside the sorted left half.

So I can safely discard that half and search the right side."

                else:
                    low = mid + 1


"Now, if the left half was NOT sorted, then because this is a rotated
sorted array, the RIGHT half must be sorted."

            else:


"I'll check whether the target lies inside that sorted right half.

The target must be greater than arr[mid] and less than or equal
to arr[high]."

                if arr[mid] < x <= arr[high]:


"If that's true, I'll search the right half by moving low to
mid plus one."

                    low = mid + 1


"Otherwise, the target is not inside the sorted right half,
so it must be on the other side.

I'll move high to mid minus one."

                else:
                    high = mid - 1


"If low eventually becomes greater than high, my search space is
empty and I never found the target.

So I'll return -1."

        return -1


"Now outside the class, I'll create my rotated sorted array."

arr = [6, 7, 8, 1, 2, 3, 4, 5]


"I'll set my target x to 7."

x = 7


"Now I'll create an object of my Solution class."

obj = Solution()


"I'll call the search method using my array and target and store
the returned index."

index = obj.search(arr, x)


"Finally, I'll print the result."

print("Target found at index:", index)
"""