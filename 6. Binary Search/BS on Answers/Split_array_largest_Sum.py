"""
Split Array - Largest Sum
Problem Statement: Given an integer array ‘A’ of size ‘N’ and an integer ‘K'. Split the array ‘A’ into ‘K’ non-empty subarrays such that the largest sum of any subarray is minimized. Your task is to return the minimized largest sum of the split. A subarray is a contiguous part of the array.
Examples

Example 1:
Input Format: N = 5, a[] = {1,2,3,4,5}, k = 3
Result: 6
Explanation: There are many ways to split the array a[] into k consecutive subarrays. The best way to do this is to split the array a[] into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.
Example 2:
Input Format: N = 3, a[] = {3,5,1}, k = 3
Result: 5
Explanation: There is only one way to split the array a[] into 3 subarrays, i.e., [3], [5], and [1]. The largest sum among these subarrays is 5.

SPLIT ARRAY — MINIMIZE LARGEST SUBARRAY SUM — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array and a number k.

I need to split the array into at most k contiguous subarrays.

Among those subarrays, I look at the sum of each one, and I want to
minimize the largest subarray sum.

So the goal is to find the smallest possible maximum subarray sum."


2. BRUTE FORCE

"The straightforward approach would be to try all possible ways to split
the array into k contiguous parts and calculate the largest subarray sum
for each split.

Then I would take the minimum among all of those answers.

This would work, but there are too many possible partitions, so it would
be very inefficient."


3. OPTIMIZE

"We can optimize this using binary search on the answer.

Instead of directly deciding where to split the array, I can guess a
maximum allowed subarray sum and check how many subarrays are needed to
stay within that limit.

Then I can adjust the limit using binary search."


4. KEY OBSERVATION

"The minimum possible answer is max(arr), because no subarray can have
a maximum sum smaller than the largest single element.

The maximum possible answer is sum(arr), because I could put the whole
array into one subarray.

For a candidate value mid, I greedily build subarrays from left to
right.

If adding the next number keeps the current subarray sum less than or
equal to mid, I keep it in the same subarray.

If adding it would exceed mid, I start a new subarray.

If I can split the array into k or fewer subarrays, then mid works and
I can try a smaller maximum sum.

If I need more than k subarrays, then mid is too small and I need to
increase it."


5. APPROACH

"I'll set low to max(arr) and high to sum(arr).

I'll also initialize ans to high, which is the worst valid answer.

For each mid, I'll treat mid as the maximum allowed sum for any subarray.

I'll go through the array and keep a running sum called num_sum.

If num_sum + num is less than or equal to mid, I'll add the number to
the current subarray.

Otherwise, I'll start a new subarray, increment the subarray count, and
set num_sum to the current number.

After processing the whole array, if the number of subarrays is less
than or equal to k, mid is valid, so I'll save it and search left for
a smaller answer.

Otherwise, mid is too small, so I'll search right."


6. WHILE CODING

"I'm setting low to max(arr) because the largest element must fit inside
some subarray by itself.

I'm setting high to sum(arr) because putting everything into one
subarray is always a valid upper bound.

For each mid, I'm checking how many subarrays I need if no subarray is
allowed to have a sum greater than mid.

I'm starting subarr at 1 because I begin with the first subarray.

If the current number fits in the current subarray, I add it to num_sum.

If it doesn't fit, I start a new subarray, increment subarr, and make
the current number the first element of that new subarray.

If subarr <= k, this maximum sum works, so I save mid and try a smaller
one.

If subarr > k, this maximum sum is too small, so I increase low."


7. EDGE CASES

"If the array could be empty, I should handle that before calling max()
or sum()."

if not arr:
    return 0

"If k is 1, the whole array must stay together, so the answer is the
sum of the array."

if k == 1:
    return sum(arr)

"If k is greater than or equal to the number of elements, every element
can be its own subarray, so the answer is the largest element."

if k >= len(arr):
    return max(arr)


8. COMPLEXITY

"Let S be the sum of the array and M be the maximum element.

The binary search takes O(log(S - M + 1)) iterations.

For every candidate mid, I traverse the entire array once to count how
many subarrays are needed.

So the total time complexity is O(n log(S - M + 1)), commonly written
as O(n log S).

The space complexity is O(1) because I only use a constant number of
extra variables."
"""
class Solution:
    def min_sum(self, arr, k):
        low = max(arr)
        high = sum(arr)
        ans = high #always keep the worst answer
        while low <= high:
            mid = (low + high) // 2 #target is to get the
                                    #smallest possible sum for k
            num_sum = 0
            subarr = 1
            for num in arr:
                if num_sum + num <= mid:
                    num_sum += num
                else:
                    subarr += 1
                    num_sum = num
            if subarr <= k:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans
"""
SPLIT ARRAY - LARGEST SUM

PROBLEM:
Split the array into k contiguous subarrays.

We want the LARGEST subarray sum to be as SMALL as possible.

Example:
arr = [1, 2, 3, 4, 5]
k = 3


SEARCH RANGE:

low = max(arr) = 5
→ A subarray must contain the largest element.

high = sum(arr) = 15
→ The whole array together is the largest possible sum.

mid = candidate maximum sum allowed for each subarray.


HOW WE CHECK MID:

Keep adding numbers while:

num_sum + num <= mid

If adding the next number exceeds mid:
→ create a new subarray
→ subarr += 1
→ num_sum = num


DRY RUN:

low = 5
high = 15

mid = 10

[1,2,3,4] = 10
[5] = 5

2 subarrays <= 3 ✅
→ 10 works
→ search LEFT


mid = 7

[1,2,3] = 6
[4] = 4
[5] = 5

3 subarrays <= 3 ✅
→ 7 works
→ search LEFT


mid = 5

[1,2] = 3
[3] = 3
[4] = 4
[5] = 5

4 subarrays > 3 ❌
→ 5 is too small
→ search RIGHT


mid = 6

[1,2,3] = 6
[4] = 4
[5] = 5

3 subarrays ✅

Answer = 6


MAIN RULE:

subarr <= k
→ mid works
→ save mid
→ LEFT for smaller maximum

subarr > k
→ mid is too small
→ RIGHT

Time: O(N * log(sum(arr) - max(arr)))
Space: O(1)
"""