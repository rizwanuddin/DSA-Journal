"""
Finding Sqrt of a number using Binary Search
Problem Statement: You are given a positive integer n. Your task is to find and return its square root. If
‘n’ is not a perfect square, then return the floor value of sqrt(n). 

Input: N = 36
Output: 6
Explanation: Square root of 36 is 6. 

Input: N = 28
Output: 5
Explanation: Square root of 28 is approximately 5.292. So, the floor value will be 5.

FLOOR SQUARE ROOT — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
non-negative integer n.

I need to find the floor of its square root.

This means I need to return the largest integer whose square is less
than or equal to n.

For example, if n is 28, the square root is around 5.29, so I would
return 5."


2. BRUTE FORCE

"The straightforward approach would be to start from 1 and keep checking
numbers until their square becomes greater than n.

Then I could return the previous number.

This would work, but in the worst case it could take O(n) time."


3. OPTIMIZE

"We can optimize this using binary search.

Instead of checking every possible number, I can search through the
possible square root values and eliminate half of them after every
comparison."


4. KEY OBSERVATION

"The key observation is that I'm looking for the largest number whose
square is less than or equal to n.

If mid squared equals n, then I've found the exact square root and can
return mid.

If mid squared is smaller than n, mid could be my floor answer, but
there might be a larger valid answer, so I'll save mid and search right.

If mid squared is greater than n, mid is too large, so I'll search
left."


5. APPROACH

"First, if n is 0 or 1, I'll directly return n.

Otherwise, I'll initialize low to 1 and high to n.

I'll also initialize ans to 0 to keep track of the best floor value
I've found.

While low is less than or equal to high, I'll calculate mid.

If mid squared equals n, I'll return mid immediately.

If mid squared is less than n, I'll save mid as a possible answer and
search to the right for a larger valid value.

Otherwise, mid is too large, so I'll search to the left.

When the search space becomes empty, I'll return ans."


6. WHILE CODING

"I'm first handling 0 and 1 because their square roots are themselves.

I'm using low and high as the boundaries of the possible square root.

For every mid, I'm comparing mid squared with n.

If they're equal, I've found the exact answer.

If mid squared is smaller than n, I'm saving mid as a possible floor
and searching right for a larger answer.

If mid squared is greater than n, I'm searching left because mid is
too large."


7. EDGE CASES

"Some edge cases I would consider are n being 0 or 1, n being a perfect
square, and n not being a perfect square."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space by
half after every comparison.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:

Find the LARGEST mid where:

mid * mid <= n


mid * mid == n
→ exact square root
→ return mid


mid * mid < n
→ possible FLOOR answer
→ ans = mid
→ search RIGHT


mid * mid > n
→ mid is too large
→ search LEFT


EASIEST WAY TO REMEMBER:

Square too SMALL
→ save it
→ go RIGHT

Square too BIG
→ go LEFT

Square EXACT
→ return it


Example:

n = 28

5 * 5 = 25  <= 28  → valid

6 * 6 = 36  > 28   → too large

Therefore:

floor(sqrt(28)) = 5
"""
class Solution:
    def floor_sqrt(self, n):

        # Edge case: sqrt(0) = 0 and sqrt(1) = 1
        if n < 2:
            return n

        low = 1
        high = n
        ans = 0

        while low <= high:

            mid = (low + high) // 2

            # Perfect square
            if mid * mid == n:
                return mid

            # Possible floor answer
            elif mid * mid < n:
                ans = mid
                low = mid + 1

            # mid is too large
            else:
                high = mid - 1

        return ans


# Driver code
n = 28

obj = Solution()
result = obj.floor_sqrt(n)

print("Floor square root:", result)


"""
EDGE CASES
1. n = 0
   → sqrt(0) = 0
   → return 0

2. n = 1
   → sqrt(1) = 1
   → return 1

3. Perfect square
   Example: n = 36
   → if mid * mid == n
   → return mid immediately

4. Not a perfect square
   Example: n = 28
   → keep the best mid where mid² < n
   → return floor value, which is 5

5. Very small numbers
   Example: n = 2
   → floor sqrt = 1

6. Large n
   → binary search still works in O(log n)
"""