"""
Nth Root of a Number using Binary Search
Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of 
a number M is defined as a number X when raised to the power N equals M. If the 'nth 
root is not an integer, return -1. 
hint- To find the nth root of a number m, we want to find a number x such that x^n = m

Input: N = 3, M = 27
Output: 3
Explanation: The cube root of 27 is equal to 3.
Input : N = 4, M = 69
Output: -1
Explanation : The 4th root of 69 does not exist. So, the answer is -1.

NTH ROOT OF A NUMBER — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given two
integers M and N.

I need to find an integer x such that x raised to the power N is exactly
equal to M.

If no integer Nth root exists, I need to return -1."


2. BRUTE FORCE

"The straightforward approach would be to try every number from 1 to M
and calculate its Nth power.

If a number raised to N equals M, I can return that number.

This would work, but in the worst case I could check up to M numbers."


3. OPTIMIZE

"We can optimize this using binary search.

Instead of checking every possible number from 1 to M, I can binary
search through the possible answers and eliminate half of the search
space after every comparison."


4. KEY OBSERVATION

"The key observation is that as the possible root gets larger, its Nth
power also gets larger.

So I can calculate mid raised to N and compare it with M.

If mid^N equals M, I've found the answer.

If mid^N is smaller than M, I need a larger number, so I search right.

If mid^N is greater than M, I need a smaller number, so I search left."


5. APPROACH

"I'll initialize low to 1 and high to M.

While low is less than or equal to high, I'll calculate mid and then
calculate mid raised to the power N.

If that value equals M, I'll return mid.

If the value is smaller than M, I'll move low to mid + 1.

Otherwise, I'll move high to mid - 1.

If binary search finishes without finding an exact Nth root, I'll
return -1."


6. WHILE CODING

"I'm setting low to 1 and high to M because those are the possible
integer roots I'm searching through.

I'm calculating mid and then mid raised to N.

If the result equals M, I've found the exact root.

If it's smaller than M, mid is too small, so I'm searching right.

If it's greater than M, mid is too large, so I'm searching left.

If I finish the binary search without finding an exact match, I'll
return -1."


7. EDGE CASES

"Some edge cases I would consider are M being 0 or 1, N being 1, and
M not having an exact integer Nth root.

I can handle 0 and 1 directly because their Nth root is themselves."

if M == 0 or M == 1:
    return M

"If N is 1, the answer is M itself."

if N == 1:
    return M

"If there is no exact integer Nth root, the binary search finishes
without finding value == M, so I return -1."

return -1


8. COMPLEXITY

"The binary search performs O(log M) iterations.

If calculating mid^N takes O(N) time by multiplying mid N times, the
overall time complexity is O(N log M).

The space complexity is O(1) because I only use a constant number of
variables."
"""
class Solution:
    def nth_root(self, M, N):
        low = 1
        high = M
        while low <= high:
            mid = (low + high) // 2
            value = mid ** N
            if value == M:
                return mid
            elif value < M:
                low = mid + 1
            else:
                high = mid - 1
        return -1