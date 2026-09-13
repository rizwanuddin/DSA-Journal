"""
Koko Eating Bananas
Problem Statement: A monkey Koko is given ‘n’ piles of bananas, whereas the 'ith' pile has ‘a[i]’ bananas. 
An integer ‘h’ is also given, which denotes the time (in hours) for all the bananas to be eaten.
Each hour, the monkey chooses a non-empty pile of bananas and eats ‘k’ bananas. If the pile contains less 
than ‘k’ bananas, then the monkey consumes all the bananas and won’t eat any more bananas in that hour.
Find the minimum number of bananas ‘k’ to eat per hour so that the monkey can eat all the bananas within 
‘h’ hours.

Examples
Input: N = 4, a[] = {7, 15, 6, 3}, h = 8
Output: 5
Explanation:  If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. 
So, he will take 8 hours to complete all the piles.  

Input: N = 5, a[] = {25, 12, 8, 14, 19}, h = 5
Output: 25
Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. 
            

KOKO EATING BANANAS / MINIMUM EATING SPEED — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array where each element represents a pile of bananas, and we are given
h hours.

Koko can eat k bananas per hour from one pile at a time.

I need to find the minimum eating speed k that allows her to finish all
the piles within h hours."


2. BRUTE FORCE

"The straightforward approach would be to try every possible eating
speed starting from 1.

For each speed, I would calculate how many total hours it takes to eat
all the piles.

The maximum speed I ever need to try is max(a), because at that speed
Koko can finish any pile in at most one hour.

This works, but checking every possible speed can be slow."


3. OPTIMIZE

"We can optimize this using binary search on the possible eating speeds.

The possible speeds range from 1 to max(a).

For each speed mid, I calculate how many hours it would take to finish
all the piles.

Then I can determine whether that speed is fast enough or too slow and
eliminate half of the possible speeds."


4. KEY OBSERVATION

"The key observation is that if a certain eating speed allows Koko to
finish within h hours, then any faster speed will also work.

So when total_hours <= h, mid is a possible answer, but I search left
because I want the minimum possible speed.

If total_hours > h, mid is too slow, so I need a faster speed and
search right."


5. APPROACH

"I'll set low to 1 because the minimum possible eating speed is one
banana per hour.

I'll set high to max(a) because we never need a speed greater than the
largest pile.

For each mid, I'll treat mid as the eating speed I'm testing.

I'll go through every pile and calculate the hours needed using
ceil(pile / mid), then add those hours together.

If the total hours are less than or equal to h, the speed works, so
I'll save mid as a possible answer and search left for a smaller speed.

Otherwise, the speed is too slow, so I'll search right.

When binary search finishes, I'll return the smallest valid speed."


6. WHILE CODING

"I'm setting my binary search range from 1 to the largest pile.

For each mid, I'm treating mid as a possible eating speed.

I'm going through every pile and calculating how many hours that pile
would take using ceil(pile / mid).

If the total number of hours is within h, this speed works, so I'm
saving it and searching left for a smaller valid speed.

If the total hours exceed h, the speed is too slow, so I'm searching
right."


7. EDGE CASES

"First, I should handle an empty array if the input does not guarantee
at least one pile, because max(a) would otherwise fail."

if not a:
    return 0

"If h is smaller than the number of non-empty piles, then it is
impossible to finish because Koko can only eat from one pile per hour.

If the problem guarantees that a solution always exists, I don't need
this check."

if h < len(a):
    return -1

"If there is only one pile, the same binary search logic still works
normally."


8. COMPLEXITY

"The binary search checks O(log(max(a))) possible speeds.

For each speed, I go through all N piles to calculate the total hours.

So the total time complexity is O(N log(max(a))).

The space complexity is O(1) because I only use a constant number of
extra variables."
""" 
from math import ceil

class Solution:
    def min_eating_speed(self, a, N, h):

        low = 1
        high = max(a)
        ans = high

        while low <= high:

            mid = (low + high) // 2

            total_hours = 0

            for pile in a:
                total_hours += ceil(pile / mid)

            if total_hours <= h:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans


# Driver code
if __name__ == "__main__":

    a = [7, 15, 6, 3]
    N = len(a)
    h = 8

    obj = Solution()

    result = obj.min_eating_speed(a, N, h)

    print("Minimum eating speed:", result)

"""
KOKO EATING BANANAS — BINARY SEARCH ON ANSWER

PROBLEM:
Koko has N piles of bananas.

Example:
a = [7, 15, 6, 3]
N = 4
h = 8

a = number of bananas in each pile
N = number of piles
h = maximum number of hours Koko has
k = bananas Koko eats per hour

We need to find the SMALLEST eating speed k that allows Koko
to finish all the piles within h hours.


IMPORTANT:
We are NOT binary searching the array a.
The piles do not need to be sorted.

We are binary searching the possible ANSWERS (eating speeds).

Possible speeds:
1, 2, 3, 4, 5, ... max(a)

So:
low = 1
high = max(a)

There is no reason to try a speed greater than max(a), because
even at max(a), every pile can already be finished in at most
one hour. Eating even faster cannot make a pile take less than
one hour.


HOW TO TEST A SPEED:

mid represents the eating speed we are currently testing.

For every pile, calculate:

hours = ceil(pile / mid)

Example:
pile = 7
mid = 5

ceil(7 / 5) = 2 hours

We calculate this for every pile and add the hours together.

IMPORTANT:
total_hours must be reset to 0 for every new mid because every
mid represents a completely new eating speed being tested.


BINARY SEARCH LOGIC:

If:
total_hours <= h

Then the current speed works.

But we want the SMALLEST speed that works, so:
    ans = mid
    high = mid - 1

We save mid and search LEFT for a smaller working speed.


If:
total_hours > h

Then Koko is eating too slowly.

So we need a BIGGER speed:
    low = mid + 1


EXAMPLE:

a = [7, 15, 6, 3]
h = 8

If k = 4:

7  -> 2 hours
15 -> 4 hours
6  -> 2 hours
3  -> 1 hour

Total = 9 hours

9 > 8
So k = 4 is too slow.


If k = 5:

7  -> 2 hours
15 -> 3 hours
6  -> 2 hours
3  -> 1 hour

Total = 8 hours

8 <= 8
So k = 5 works.

Since 4 does not work but 5 does:

Answer = 5


MAIN PATTERN:

Binary search on SPEED k

Pick mid
    ↓
Treat mid as bananas/hour
    ↓
Calculate total hours for all piles
    ↓
total_hours <= h?
    ↓
YES → speed works
      save mid
      search LEFT for smaller speed

NO  → speed is too slow
      search RIGHT for bigger speed


WHY BINARY SEARCH WORKS:

Smaller speed → more hours
Larger speed  → fewer hours

So the possible speeds have a pattern like:

1  2  3  4  5  6  7  8 ...
❌ ❌ ❌ ❌ ✅ ✅ ✅ ✅ ...

We want the FIRST/SMALLEST speed that works.


COMPLEXITY:

Binary search checks O(log(max(a))) possible speeds.

For every speed, we traverse all N piles.

Time:  O(N * log(max(a)))
Space: O(1)
"""
