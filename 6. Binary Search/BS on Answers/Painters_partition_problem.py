"""
Painter's Partition Problem
Problem Statement: Given an array/list of length ‘N’, where the array/list represents the boards and each element of the given array/list represents the length of each board. Some ‘K’ numbers of painters are available to paint these boards. Consider that each unit of a board takes 1 unit of time to paint. You are supposed to return the area of the minimum time to get this job done of painting all the ‘N’ boards under the constraint that any painter will only paint the continuous sections of boards.
Examples

Example 1:
Input Format: N = 4, boards[] = {5, 5, 5, 5}, k = 2
Result: 10
Explanation: We can divide the boards into 2 equal-sized partitions, so each painter gets 10 units of the board and the total time taken is 10.

Example 2:
Input Format: N = 4, boards[] = {10, 20, 30, 40}, k = 2
Result: 60
Explanation: We can divide the first 3 boards for one painter and the last board for the second painter


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
#we are supposed to find Find the minimum possible value of the largest painter workload if that makes sense lol
class Solution:
    def min_time(self, arr, k):
        low = max(arr)
        high = sum(arr)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            sum_boards = 0
            painters = 1
            for boards in arr:
                if sum_boards + boards <= mid:
                    sum_boards += boards
                else:
                    sum_boards = boards
                    painters += 1
            if painters <= k :
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans
    
"""
PAINTER'S PARTITION — SHORT EXPLANATION

Goal:
Split the boards among k painters in contiguous order so that the
MAXIMUM time taken by any painter is as SMALL as possible.

SEARCH RANGE:

low = max(arr)
→ One painter must at least be able to paint the largest board.

high = sum(arr)
→ One painter painting everything is the maximum possible time.

mid = maximum time currently allowed for one painter.


HOW WE CHECK MID:

Keep adding boards to the current painter.

If:
sum_boards + board <= mid
→ give the board to the current painter.

Otherwise:
→ use a new painter
→ painters += 1
→ sum_boards = board


BINARY SEARCH:

painters <= k
→ mid works
→ save mid
→ search LEFT for smaller time

painters > k
→ mid is too small
→ search RIGHT for larger time


Example:

arr = [10, 20, 30, 40]
k = 2

60 works:
Painter 1 → [10,20,30] = 60
Painter 2 → [40] = 40

59 fails because we need 3 painters.

Answer = 60


Time: O(N * log(sum(arr) - max(arr)))
Space: O(1)
"""

