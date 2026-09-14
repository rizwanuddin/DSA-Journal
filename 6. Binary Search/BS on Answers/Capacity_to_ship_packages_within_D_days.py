"""
Capacity to Ship Packages within D Days
8
Problem Statement: You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. The packages must be shipped within 'd' days. The weights of the packages are given in an array 'of weights'. The packages are loaded on the conveyor belts every day in the same order as they appear in the array. The loaded weights must not exceed the maximum weight capacity of the ship. Find out the least-weight capacity so that you can ship all the packages within 'd' days .
Examples

Input: N = 5, weights = [5, 4, 5, 2, 3, 4, 5, 6], d = 5
Output: 9
Explanation: The minimum ship capacity needed to ship all packages within 5 days is 9.

Input: N = 3, weights = [1, 2, 3, 4, 5], d = 2
Output: 9
Explanation: With a capacity of 9, the packages can be shipped in 2 days as [1,2,3,4] and [5].


CAPACITY TO SHIP PACKAGES WITHIN D DAYS — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array of package weights and d days.

The packages must be shipped in the same order they appear in the array.

I need to find the minimum ship capacity that allows me to ship all
packages within d days."


2. BRUTE FORCE

"The straightforward approach would be to try every possible ship
capacity.

For each capacity, I would simulate loading the packages in order and
calculate how many days are required.

Then I would return the first capacity that can finish within d days.

This works, but trying every possible capacity can be slow."


3. OPTIMIZE

"We can optimize this using binary search on the possible ship
capacities.

The minimum possible capacity is max(weights), because the ship must at
least be able to carry the heaviest package.

The maximum capacity is sum(weights), because with that capacity I could
ship everything in one day."


4. KEY OBSERVATION

"The key observation is that if a certain capacity can ship everything
within d days, then any larger capacity will also work.

So if mid requires d days or fewer, mid is a possible answer, but I'll
search left for a smaller capacity.

If mid requires more than d days, the capacity is too small, so I'll
search right for a larger capacity."


5. APPROACH

"I'll set low to the heaviest package and high to the total weight of
all packages.

For each mid, I'll treat mid as the ship capacity I'm testing.

I'll start with day 1 and a load of 0.

I'll go through the packages in order and add each weight to the current
load.

If the load becomes greater than mid, the current package doesn't fit
on that day, so I'll start a new day and make that package the first
package of the new day's load.

After processing all packages, I'll check the number of days required.

If days is less than or equal to d, the capacity works, so I'll save it
and search left for a smaller capacity.

Otherwise, I'll search right for a larger capacity."


6. WHILE CODING

"I'm setting low to max(weights) because the ship must be able to carry
the heaviest package.

I'm setting high to sum(weights) because that would let me ship
everything in one day.

For each mid, I'm treating mid as a possible ship capacity.

I'm starting days at 1 because I begin shipping on the first day, and
load at 0 because the ship is initially empty.

For every package, I'm adding its weight to the current load.

If load becomes greater than mid, that package cannot fit on the current
day, so I'm increasing days and starting the new day's load with that
package.

If days <= d, this capacity works, so I'm searching left for a smaller
one.

Otherwise, the capacity is too small, so I'm searching right."


7. EDGE CASES

"If the weights array could be empty, I should handle it before calling
max() or sum()."

if not weights:
    return 0

"If d is 1, all packages must be shipped in one day, so the required
capacity is the total weight."

if d == 1:
    return sum(weights)

"The ship must always be able to carry the heaviest individual package,
which is why my binary search starts here."

low = max(weights)


8. COMPLEXITY

"Let S be the sum of all package weights and M be the maximum package
weight.

The binary search takes O(log(S - M + 1)) iterations.

For each capacity I test, I traverse all n packages to calculate the
number of days required.

So the total time complexity is O(n log(S - M + 1)), commonly written
as O(n log S).

The space complexity is O(1) because I only use a constant number of
extra variables."
"""


class Solution:
    def min_weight(self, weights, d):

        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:

            # Candidate ship capacity
            mid = (low + high) // 2

            days = 1
            load = 0

            # Calculate how many days this capacity needs
            for weight in weights:

                load += weight

                # Current package does not fit
                if load > mid:

                    # Start a new day
                    days += 1

                    # Current package becomes first package of new day
                    load = weight

            # Capacity works
            if days <= d:
                ans = mid

                # Try a smaller capacity
                high = mid - 1

            # Capacity is too small
            else:

                # Try a bigger capacity
                low = mid + 1

        return ans


# Driver code
weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5

obj = Solution()
result = obj.min_weight(weights, d)

print("Minimum ship capacity:", result)

"""
CAPACITY TO SHIP PACKAGES WITHIN D DAYS — BINARY SEARCH ON ANSWER

PROBLEM:
We are given package weights in a fixed order and d days.

We need to find the SMALLEST ship capacity that can ship all packages
within d days.

Example:
weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5


SEARCH RANGE:

low = max(weights)

The ship must at least carry the heaviest package.

high = sum(weights)

With this capacity, all packages could be shipped in one day.

We binary search between low and high, where mid represents a
candidate ship capacity.


HOW WE TEST A CAPACITY:

Start with:

days = 1
load = 0

Go through packages in order and add each weight to load.

If:

load > mid

the package doesn't fit on the current day.

So:
days += 1
load = weight

The current package becomes the first package of the new day.


BINARY SEARCH:

If:
days <= d

The capacity works.

But we want the SMALLEST capacity, so:

ans = mid
high = mid - 1


If:
days > d

The capacity is too small, so:

low = mid + 1


QUICK DRY RUN:

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5

low = 6
high = 34

mid = 20 → needs 2 days ✅
→ works, search smaller

mid = 12 → needs 4 days ✅
→ works, search smaller

mid = 8 → needs 6 days ❌
→ too small, search bigger

mid = 10 → needs 4 days ✅
→ works, search smaller

mid = 9 → needs 5 days ✅
→ works

For capacity 9:

Day 1 → [5,4] = 9
Day 2 → [5,2] = 7
Day 3 → [3,4] = 7
Day 4 → [5]   = 5
Day 5 → [6]   = 6

So the minimum capacity is 9.


MAIN PATTERN:

Binary search on CAPACITY

days <= d → works → save mid → LEFT
days > d  → too small → RIGHT


COMPLEXITY:

Time: O(N * log(sum(weights)))
Space: O(1)
"""
         

