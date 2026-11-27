"""
Minimum Cost to Connect Sticks
You have some sticks with positive integer lengths. You can connect any two sticks together to 
form a longer stick by paying a cost equal to the sum of their lengths. You must connect all 
the sticks into one single stick.
Return the minimum cost of connecting all the sticks.

Example 1:
Input: sticks = [2, 4, 3]
Output: 14
Explanation:
Connect sticks 2 and 3 → cost = 2 + 3 = 5 (sticks = [5, 4]),
Connect sticks 4 and 5 → cost = 4 + 5 = 9 (sticks = [9]),
Total cost = 5 + 9 = 14

Example 2:
Input: sticks = [1, 8, 3, 5]
Output: 30

Explanation:
Connect 1 and 3 → cost = 1 + 3 = 4 (sticks = [4, 8, 5]),
Connect 4 and 5 → cost = 4 + 5 = 9 (sticks = [9, 8]),
Connect 8 and 9 → cost = 8 + 9 = 17 (sticks = [17]),
Total cost = 4 + 9 + 17 = 30



# Minimum Cost to Connect Sticks: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given an array of stick lengths.
I can connect any two sticks into one,
and the cost of doing that is the sum of their lengths.
I need to keep connecting till only one stick is left,
and return the minimum total cost."

"Quick things I'd confirm:
are the lengths always positive? I'll assume yes.
If there's only one stick, or none, is the cost 0? I'll assume yes,
because there's nothing to connect."

"Now here's the thing I notice.
When I connect two sticks, the new stick can get connected again later.
So its length gets added to the cost again, and again.
That means a stick that gets merged early ends up being paid for many times, agreed?"

"So which sticks should I merge early?
The smallest ones, right?
Because paying for a small number many times is cheaper
than paying for a big number many times.
And the biggest sticks should be merged last, so they're paid for the fewest times."

"So every time, I'll pick the two smallest sticks and connect them."

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"I'll keep the sticks in a normal list.
Every round, I scan the whole list to find the smallest stick, and remove it.
Then I scan again to find the next smallest, and remove it.
I add them up, add that to my cost,
and put the new stick back into the list."

"I keep doing this till only one stick is left. Quite simple."

### Time complexity

"Now what will be the
"""
import heapq

class Solution:
    def Min_cost(self, sticks):
        total_cost = 0

        heap = list(sticks)                            # O(n) time copy n elements & O(n) space: copy of sticks
        heapq.heapify(heap)                             # O(n) time: build heap

        while len(heap) > 1:                            # runs n-1 times
            stick1 = heapq.heappop(heap)                # O(log n)
            stick2 = heapq.heappop(heap)                # O(log n)
            sum_ = stick1 + stick2                      # O(1)
            heapq.heappush(heap, sum_)                  # O(log n)
            total_cost += sum_                          # O(1)
                                                          # -> each round: O(log n)
                                                          # -> (n-1) rounds: O(n log n)
        return total_cost
        # TOTAL TIME:  O(n) [heapify] + O(n log n) [loop] -> O(n log n)
        # TOTAL SPACE: O(n) [heap]                         -> O(n)

