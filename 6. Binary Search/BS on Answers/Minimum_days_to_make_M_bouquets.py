"""
Minimum days to make M bouquets
Problem Statement: You are given 'N’ roses and you are also given an array 'arr' where 
'arr[i]' denotes that the 'ith' rose will bloom on the 'arr[i]th' day. You can only 
pick already bloomed roses that are adjacent to make a bouquet. You are also told that 
you require exactly 'k' adjacent bloomed roses to make a single bouquet. Find the 
minimum number of days required to make at least ‘m' bouquets each containing 'k' 
roses. Return -1 if it is not possible. 

Example 1:
Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already 
bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the 
last 3 flowers.

Example 2:
Input Format: N = 5, arr[] = {1, 10, 3, 10, 2}, m = 3, k = 2
Result: -1
Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 
flowers. But we are given only 5 flowers, so, we cannot make the bouquets.


MINIMUM DAYS TO MAKE M BOUQUETS — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array where arr[i] represents the day the ith flower blooms.

I need to make m bouquets, and each bouquet requires k adjacent flowers.

I need to find the minimum number of days I have to wait until it is
possible to make at least m bouquets.

If there aren't enough flowers to make m bouquets at all, I'll return
-1."


2. BRUTE FORCE

"The straightforward approach would be to try every possible day from
the minimum bloom day to the maximum bloom day.

For each day, I would go through the array and check how many bouquets
I can make using flowers that have bloomed by that day.

This would work, but checking every possible day can be slow."


3. OPTIMIZE

"We can optimize this using binary search on the possible number of
days.

My search space goes from the earliest bloom day to the latest bloom
day.

For each mid, I'll check whether it is possible to make at least m
bouquets by that day."


4. KEY OBSERVATION

"The key observation is that if I can make m bouquets by a certain day,
then I can also make them on any later day because more flowers may
have bloomed.

So if mid works, it is a possible answer, but I'll search left for an
earlier day.

If mid does not work, I need to wait longer, so I'll search right.

To handle the adjacency requirement, I count consecutive bloomed
flowers.

If arr[i] <= mid, that flower has bloomed, so I increase flowers.

When flowers reaches k, I've found k adjacent flowers, so I make one
bouquet and reset flowers to 0.

If I find a flower where arr[i] > mid, that flower has not bloomed yet,
so the consecutive sequence is broken and I reset flowers to 0."


5. APPROACH

"First, I'll check whether m * k is greater than the number of flowers.
If it is, making the required bouquets is impossible, so I'll return
-1.

Then I'll binary search between min(arr) and max(arr).

For every mid, I'll treat mid as the day I'm testing.

I'll go through the array and count consecutive flowers whose bloom
day is less than or equal to mid.

Whenever the consecutive count reaches k, I'll make one bouquet and
reset the flower count.

If I can make at least m bouquets, mid works, so I'll save it and
search left for a smaller day.

Otherwise, I'll search right because I need to wait longer.

Finally, I'll return the minimum valid day."


6. WHILE CODING

"I'm first checking whether I even have enough flowers to make m
bouquets.

I'm using the minimum and maximum bloom days as my binary search range.

For every mid, I'm checking how many bouquets can be made by that day.

If day <= mid, the flower has bloomed, so I'm increasing my consecutive
flower count.

When flowers reaches k, I've found k adjacent flowers, so I'm increasing
the bouquet count and resetting flowers to 0.

If day > mid, the flower hasn't bloomed, so adjacency is broken and I'm
resetting flowers to 0.

If bouquet >= m, this day works, so I'm saving it and searching left
for an earlier day.

Otherwise, I need more time, so I'm searching right."


7. EDGE CASES

"If there aren't enough total flowers to create m bouquets, I'll return
-1 immediately."

if m * k > len(arr):
    return -1

"If the input array could be empty, I should handle that before calling
min(arr) or max(arr)."

if not arr:
    return -1

"The adjacency requirement is handled by resetting flowers whenever I
find a flower that has not bloomed yet."

if day > mid:
    flowers = 0

"This prevents flowers from different separated sections of the array
from being incorrectly used in the same bouquet."


8. COMPLEXITY

"Let D be the difference between the maximum and minimum bloom days.

Binary search takes O(log D) iterations.

For every possible day I test, I traverse all n flowers to count the
bouquets.

So the total time complexity is O(n log D).

The space complexity is O(1) because I only use a constant number of
extra variables."
"""


class Solution:
    def min_days(self, arr, m, k): # m - no of bouquet; k - no of adj.flowers in each bouqeut
        if m * k > len(arr):
            return -1
        low = min(arr)
        high = max(arr)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            bouquet = 0
            flowers = 0
            for day in arr:
                if day <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquet += 1
                        flowers = 0
                else:
                    flowers = 0
            if bouquet >= m :
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


"""
MINIMUM DAYS TO MAKE M BOUQUETS — BINARY SEARCH ON ANSWER

PROBLEM:
We are given an array where:

arr[i] = the day the ith flower blooms
m = number of bouquets we need
k = number of ADJACENT flowers needed for each bouquet

We need to find the MINIMUM day when we can make at least m bouquets.

Example:
arr = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3

We need:
2 bouquets
3 adjacent flowers per bouquet


STEP 1: CHECK IF IT IS EVEN POSSIBLE

We need a total of:

m * k

flowers.

If:

m * k > len(arr)

then we don't even have enough flowers, so:

return -1


STEP 2: BINARY SEARCH ON THE DAY

We are NOT binary searching arr.
arr does not need to be sorted.

We are binary searching the possible DAYS.

The earliest useful day is:

low = min(arr)

The latest useful day is:

high = max(arr)

By max(arr), every flower has bloomed.


STEP 3: TEST A CANDIDATE DAY

mid represents the DAY we are currently testing.

For every bloom day in arr:

If:

day <= mid

the flower has already bloomed, so:

flowers += 1

If:

flowers == k

we have k adjacent bloomed flowers, so we can make one bouquet:

bouquet += 1
flowers = 0

We reset flowers because those k flowers have now been used.


STEP 4: HANDLE ADJACENCY

If:

day > mid

that flower has NOT bloomed yet.

This breaks the chain of adjacent bloomed flowers, so:

flowers = 0

Example:

B B X B B B

The X breaks adjacency.

The flowers before X cannot be combined with the flowers after X.


STEP 5: BINARY SEARCH DECISION

After checking all flowers:

If:

bouquet >= m

then day mid works.

But we want the MINIMUM possible day.

So:

ans = mid
high = mid - 1

We save mid and search LEFT for an earlier working day.


If:

bouquet < m

then day mid is too early.

We need to wait longer:

low = mid + 1


EXAMPLE:

arr = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3

Suppose:

mid = 12

By day 12:

7  -> bloomed
7  -> bloomed
7  -> bloomed

3 adjacent flowers:
bouquet = 1
flowers = 0

7  -> bloomed
13 -> NOT bloomed
      adjacency breaks
      flowers = 0

11 -> bloomed
12 -> bloomed
7  -> bloomed

3 adjacent flowers:
bouquet = 2

So:

bouquet >= m

Day 12 works.

We save 12 and search LEFT to see if an earlier day also works.


MAIN PATTERN:

Binary search on DAY

Pick mid
    ↓
Treat mid as a candidate day
    ↓
Scan all flowers
    ↓
day <= mid
→ bloomed
→ flowers += 1

day > mid
→ not bloomed
→ adjacency breaks
→ flowers = 0

flowers == k
→ make bouquet
→ bouquet += 1
→ flowers = 0
    ↓
bouquet >= m?
    ↓
YES → day works
      save mid
      search LEFT

NO  → too early
      search RIGHT


WHY BINARY SEARCH WORKS:

As the number of days increases, more flowers can bloom.

So the possible days follow a pattern like:

early                         late

❌ ❌ ❌ ❌ ❌ ✅ ✅ ✅ ✅
               ↑
        first day that works

Once a day works, every later day will also work.

We want the FIRST/MINIMUM working day.


COMPLEXITY:

Let:
N = number of flowers

For every candidate day, we scan all N flowers:
O(N)

Binary search checks:
O(log(max(arr) - min(arr) + 1))

Time:
O(N * log(max(arr) - min(arr) + 1))

Space:
O(1)
"""