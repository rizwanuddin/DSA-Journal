"""
Aggressive Cows : Detailed Solution
Problem Statement: You are given an array 'arr' of size 'n' which denotes the position of stalls. You are also given an integer 'k' which denotes the number of aggressive cows.
You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible. Find the maximum possible minimum distance.

Example 1:

Input Format:
 N = 6, k = 4, arr[] = {0,3,4,7,10,9}
Result:
 3
Explanation:
 The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

Example 2:

Input Format:
 N = 5, k = 2, arr[] = {4,2,1,3,6}
Result:
 5
Explanation:
 The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions {1, 6}. 

 
 AGGRESSIVE COWS — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given the
positions of stalls and k cows.

I need to place all k cows in the stalls such that the minimum distance
between any two cows is as large as possible.

I need to return that maximum possible minimum distance."


2. BRUTE FORCE

"The straightforward approach would be to try every possible minimum
distance and check whether I can place all k cows with at least that
distance between them.

This would work, but trying every distance one by one can be slow."


3. OPTIMIZE

"We can optimize this using binary search on the answer.

The answer is not an index in the array. It is the minimum distance
between cows.

The smallest possible distance I need to consider is 1.

The largest possible distance is the distance between the first and
last stall after sorting, which is arr[-1] - arr[0]."


4. KEY OBSERVATION

"The key observation is that if I can place all k cows with a minimum
distance of mid, then I can also place them with any smaller distance.

So if mid works, I should try a larger distance because I want to
maximize the minimum distance.

If mid does not work, then the distance is too large, so I need to
search for a smaller one.

To check whether a distance works, I greedily place the first cow in
the first stall, then place each next cow in the earliest stall that
is at least mid distance away from the last cow."


5. APPROACH

"First, I'll sort the stall positions.

I'll set low to 1 and high to arr[-1] - arr[0].

For each mid, I'll treat mid as the minimum distance I'm testing.

I'll place the first cow in the first stall and keep track of its
position using last_cow.

Then I'll go through the remaining stalls.

Whenever the distance between the current stall and last_cow is at
least mid, I'll place another cow there and update last_cow.

After checking all stalls, if I was able to place at least k cows, then
mid is a valid answer, so I'll save it and search right for a larger
distance.

Otherwise, mid is too large, so I'll search left.

When binary search finishes, I'll return ans."


6. WHILE CODING

"I'm sorting the array first because I want to place cows from left to
right in stall order.

I'm setting low to 1 because that is the smallest positive distance I
need to test.

I'm setting high to arr[-1] - arr[0], which is the largest possible
distance between the outermost stalls.

For each mid, I'm placing the first cow at arr[0].

Then for every next stall, I'm checking whether:

stall - last_cow >= mid

If that condition is true, I can place another cow there.

If cow_count >= k, this distance works, so I'm saving mid and searching
right for a larger minimum distance.

Otherwise, the distance is too large, so I'm searching left."


7. EDGE CASES

"If there are fewer stalls than cows, then placing all cows is
impossible."

if len(arr) < k:
    return -1

"If there is only one cow, there is no meaningful distance between
pairs of cows. If the problem guarantees k >= 2, I don't need to handle
this separately."

if k <= 1:
    return 0

"If the input array could be empty, I should handle that before using
arr[0] or arr[-1]."

if not arr:
    return -1


8. COMPLEXITY

"Sorting the stalls takes O(n log n).

The binary search checks O(log D) possible distances, where D is
arr[-1] - arr[0].

For each distance, I scan all n stalls to check how many cows can be
placed.

So the total time complexity is O(n log n + n log D).

The space complexity is O(1) extra if the sorting is done in-place,
ignoring the internal space used by the sorting algorithm."
"""
class Solution:
    def max_dist(self, arr, k):
        arr.sort()
        low = 1
        high = arr[-1] - arr[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            # Place first cow in first stall
            last_cow = arr[0]
            cow_count = 1
            # Try placing remaining cows
            for stall in arr[1:]:
                if stall - last_cow >= mid:
                    last_cow = stall
                    cow_count += 1
            # If we can place all k cows
            if cow_count >= k:
                ans = mid
                # Try a larger minimum distance
                low = mid + 1
            else:
                # Distance is too large
                high = mid - 1
        return ans
# Driver code
arr = [0, 3, 4, 7, 10, 9]
k = 4
obj = Solution()
result = obj.max_dist(arr, k)
print("Maximum minimum distance:", result)


"""
AGGRESSIVE COWS — SHORT EXPLANATION + DRY RUN

PROBLEM:

We have stalls at different positions and k cows.

We need to place all k cows so that the MINIMUM distance between
any two cows is as LARGE as possible.

Example:

arr = [0, 3, 4, 7, 10, 9]
k = 4

First sort:

arr = [0, 3, 4, 7, 9, 10]

We binary search the possible DISTANCE between cows.

low = 1
high = 10 - 0 = 10

For every mid, we ask:

"Can I place at least k cows while keeping a distance of at least
mid between consecutive cows?"

We always place the first cow at the first stall.


DRY RUN:

mid = 5

Cow at 0

3 - 0 < 5  → skip
4 - 0 < 5  → skip
7 - 0 >= 5 → place cow at 7
9 - 7 < 5  → skip
10 - 7 < 5 → skip

Only 2 cows ❌

Distance 5 is too large.
→ search smaller distances


mid = 2

Cow at 0

3 - 0 >= 2 → cow at 3
4 - 3 < 2  → skip
7 - 3 >= 2 → cow at 7
9 - 7 >= 2 → cow at 9

4 cows placed ✅

Distance 2 works.
→ try a larger distance


mid = 3

Cow at 0

3 - 0 >= 3  → cow at 3
4 - 3 < 3   → skip
7 - 3 >= 3  → cow at 7
9 - 7 < 3   → skip
10 - 7 >= 3 → cow at 10

4 cows placed ✅

Distance 3 works.
→ try larger


mid = 4

Cow at 0

3 - 0 < 4  → skip
4 - 0 >= 4 → cow at 4
7 - 4 < 4  → skip
9 - 4 >= 4 → cow at 9
10 - 9 < 4 → skip

Only 3 cows ❌

Distance 4 is too large.


FINAL:

3 works ✅
4 fails ❌

Maximum possible minimum distance = 3


MAIN PATTERN:

cow_count >= k
→ distance works
→ save mid
→ search RIGHT for bigger distance

cow_count < k
→ distance too large
→ search LEFT

Time: O(N log(range)) + sorting
Space: O(1) excluding sorting
"""
               