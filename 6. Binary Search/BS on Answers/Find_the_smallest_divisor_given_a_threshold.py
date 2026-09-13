"""
Find the Smallest Divisor Given a Threshold
Problem Statement: You are given an array of integers 'arr' and an integer i.e. a 
threshold value 'limit'. Your task is to find the smallest positive integer divisor, 
such that upon dividing all the elements of the given array by it, the sum of the 
division's result is less than or equal to the given threshold value.
Examples

Example 1:
Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result: 3
Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array 
by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is 
the minimum possible answer.

Example 2:
Input Format: N = 4, arr[] = {8,4,2,3}, limit = 10
Result: 2
Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. 
So, 2 is the answer.


SMALLEST DIVISOR GIVEN A THRESHOLD — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array of positive integers and a limit.

I need to choose a positive divisor, divide every element by that
divisor, round each result up, and add them together.

I need to find the smallest divisor for which this total is less than
or equal to the given limit."


2. BRUTE FORCE

"The straightforward approach would be to try every possible divisor
starting from 1 up to the maximum element in the array.

For each divisor, I would calculate the total and return the first
divisor whose total is less than or equal to the limit.

This would work, but trying every divisor can be slow."


3. OPTIMIZE

"We can optimize this using binary search on the possible divisors.

The smallest possible divisor is 1, and the largest divisor we need to
consider is max(arr).

For every mid, I'll treat mid as a possible divisor and check whether
it satisfies the limit."


4. KEY OBSERVATION

"The key observation is that the divisor and the total move in opposite
directions.

A smaller divisor gives me a larger total.

A larger divisor gives me a smaller total.

So if the total is less than or equal to the limit, mid works, but I
search left because I want the smallest possible divisor.

If the total is greater than the limit, the divisor is too small, so
I need a larger divisor and search right."


5. APPROACH

"I'll initialize low to 1 and high to the maximum element in the array.

For every mid, I'll treat mid as the divisor I'm testing.

I'll go through the array and calculate ceil(num / mid) for every
element, then add these values to total_value.

If total_value is less than or equal to the limit, mid is a valid
divisor, so I'll save it and search left for a smaller valid divisor.

Otherwise, the divisor is too small, so I'll search right.

When binary search finishes, I'll return the smallest valid divisor."


6. WHILE CODING

"I'm setting my binary search range from 1 to max(arr).

For each mid, I'm treating mid as my possible divisor.

I'm going through every number, dividing it by mid, rounding up, and
adding the result to total_value.

If total_value <= limit, this divisor works, so I'm saving mid and
searching left for a smaller divisor.

If total_value > limit, my divisor is too small, so I'm searching right
for a larger divisor."


7. EDGE CASES

"If the array could be empty, I should handle that before calling
max(arr)."

if not arr:
    return -1

"Since every positive number contributes at least 1 to the total, if
the limit is smaller than the number of elements, no divisor can work."

if limit < len(arr):
    return -1

"The divisor can never be zero, so I start my binary search from 1."

low = 1


8. COMPLEXITY

"Let M be the maximum value in the array.

Binary search takes O(log M) iterations.

For every divisor I test, I traverse all n elements to calculate the
total.

So the total time complexity is O(n log M).

The space complexity is O(1) because I only use a constant number of
extra variables."
"""
from math import ceil
class Solution:
    def smalles_divisor(self, arr, limit):
        low = 1
        high = max(arr)
        ans = -1
        value = 0
        while low <= high:
            total_value = 0 
            mid = (low + high) // 2
            for num in arr: #smaller the divisor bigger the total_value so you can adjust mid based of that
                value = ceil(num/mid)
                total_value += value
            if total_value <= limit:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


"""
FIND THE SMALLEST DIVISOR GIVEN A THRESHOLD — BINARY SEARCH ON ANSWER

PROBLEM:
We are given:

arr = array of positive integers
limit = maximum allowed sum

We need to find the SMALLEST positive integer divisor such that:

ceil(arr[0] / divisor)
+ ceil(arr[1] / divisor)
+ ...
<= limit

Example:

arr = [1, 2, 3, 4, 5]
limit = 8


STEP 1: BINARY SEARCH ON THE DIVISOR

We are NOT binary searching arr.
arr does not need to be sorted.

We are binary searching the possible DIVISORS.

The smallest possible positive divisor is:

low = 1

The largest useful divisor is:

high = max(arr)

We don't use min(arr) because the divisor does NOT have to be an
element from arr. It can be any positive integer.


STEP 2: TEST A CANDIDATE DIVISOR

mid represents the divisor we are currently testing.

For every number in arr:

value = ceil(num / mid)

We use ceil because the problem requires the division result to
be rounded UP.

Add all the results:

total_value += ceil(num / mid)

IMPORTANT:
total_value must be reset to 0 for every new mid because each mid
is a completely new divisor being tested.


STEP 3: BINARY SEARCH DECISION

If:

total_value <= limit

then mid is a valid divisor.

But we want the SMALLEST valid divisor.

So:

ans = mid
high = mid - 1

We save mid and search LEFT for a smaller divisor.


If:

total_value > limit

then our divisor is too small.

A smaller divisor produces larger division results, so we need
a BIGGER divisor.

Therefore:

low = mid + 1


EXAMPLE:

arr = [1, 2, 3, 4, 5]
limit = 8

Try divisor = 2:

ceil(1 / 2) = 1
ceil(2 / 2) = 1
ceil(3 / 2) = 2
ceil(4 / 2) = 2
ceil(5 / 2) = 3

total = 9

9 > 8

So divisor 2 is too small.
We need a bigger divisor.


Try divisor = 3:

ceil(1 / 3) = 1
ceil(2 / 3) = 1
ceil(3 / 3) = 1
ceil(4 / 3) = 2
ceil(5 / 3) = 2

total = 7

7 <= 8

So divisor 3 works.

Since we want the smallest divisor, we would search LEFT for an
even smaller valid divisor.

But 2 already failed, so:

Answer = 3


MAIN PATTERN:

Binary search on DIVISOR

Pick mid
    ↓
Treat mid as candidate divisor
    ↓
Calculate:
sum of ceil(num / mid)
    ↓
total_value <= limit?
    ↓
YES → divisor works
      save mid
      search LEFT

NO  → divisor is too small
      search RIGHT


WHY BINARY SEARCH WORKS:

Smaller divisor → larger total
Larger divisor  → smaller total

So possible divisors follow a pattern:

1  2  3  4  5 ...
❌ ❌ ✅ ✅ ✅ ...
      ↑
smallest divisor that works

We want the FIRST valid divisor.


COMPLEXITY:

For every candidate divisor, we traverse all N elements:
O(N)

Binary search checks:
O(log(max(arr)))

Time:
O(N * log(max(arr)))

Space:
O(1)
"""

