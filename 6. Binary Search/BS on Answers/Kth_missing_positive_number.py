"""
Kth Missing Positive Number
Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.
Examples

Example 1:
Input Format: vec[]={4,7,9,10}, k = 1
Result: 1
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.

Example 2:
Input Format: vec[]={4,7,9,10}, k = 4
Result: 5
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 4, the fourth missing element is 5.


KTH MISSING POSITIVE NUMBER — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array of positive integers and a value k.

Some positive numbers are missing from the array.

I need to find and return the kth missing positive number."


2. BRUTE FORCE

"The straightforward approach would be to go through the positive
numbers one by one and check whether each number exists in the array.

I could count the missing numbers until I reach the kth one.

This would work, but it would be slower because I may have to check
many numbers."


3. OPTIMIZE

"Since the array is sorted, I can optimize this using binary search.

Instead of finding every missing number, I can calculate how many
numbers are missing before each index and use that information to find
where the kth missing number belongs."


4. KEY OBSERVATION

"The key observation is that if there were no missing numbers, the
value at index mid should be mid + 1.

So the number of missing values before arr[mid] is:

arr[mid] - (mid + 1)

If this missing count is smaller than k, the kth missing number must
be further to the right.

Otherwise, I've already reached or passed the kth missing number, so
I search to the left."


5. APPROACH

"I'll initialize low to 0 and high to the last index.

For every mid, I'll calculate how many positive numbers are missing
before that position using:

missing = arr[mid] - (mid + 1)

If missing is less than k, I haven't reached the kth missing number
yet, so I'll search right.

Otherwise, the kth missing number must be before this position, so
I'll search left.

When binary search finishes, low represents how many array elements
come before the kth missing number.

So the answer is low + k."


6. WHILE CODING

"I'm calculating mid and then finding how many numbers are missing
before arr[mid].

I do that using arr[mid] - (mid + 1), because mid + 1 is the value
that should have been at this position if no numbers were missing.

If missing < k, I still need more missing numbers, so I'm searching
right.

Otherwise, I've reached or passed the kth missing number, so I'm
searching left.

Once the binary search finishes, I'm returning low + k."


7. EDGE CASES

"If the array could be empty, the kth missing positive number is simply
k."

if not arr:
    return k

"If the kth missing number comes before the first array element, binary
search will leave low at 0, and this formula still returns k."

return low + k

"If the kth missing number comes after the last array element, low will
become len(arr), and the same formula still works."

return low + k


8. COMPLEXITY

"The time complexity is O(log n) because I use binary search and reduce
the search space by half after every comparison.

The space complexity is O(1) because I only use a constant number of
variables."
"""
class Solution:
    def kth_missing(self, arr, k):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (high + low) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k
# Driver code
arr = [4, 7, 9, 10]
k = 4

obj = Solution()
result = obj.kth_missing(arr, k)

print("Kth missing positive number:", result)    



"""
KTH MISSING POSITIVE NUMBER — EXPLANATION

We binary search the INDICES of the array.

For every mid, we calculate:

missing = arr[mid] - (mid + 1)

This tells us how many positive numbers are missing before arr[mid].

If:
missing < k

→ We haven't reached the kth missing number yet.
→ Search RIGHT.
→ low = mid + 1


If:
missing >= k

→ We have reached/passed the kth missing number.
→ Search LEFT.
→ high = mid - 1


EXAMPLE:

arr = [4, 7, 9, 10]
k = 4

mid = 1
arr[mid] = 7

missing = 7 - 2 = 5

5 >= 4
→ Search LEFT


mid = 0
arr[mid] = 4

missing = 4 - 1 = 3

3 < 4
→ Search RIGHT


Search ends with:

low = 1

Answer:

low + k
= 1 + 4
= 5


MAIN RULE:

missing < k  → RIGHT
missing >= k → LEFT

Answer = low + k

Time: O(log n)
Space: O(1)
"""