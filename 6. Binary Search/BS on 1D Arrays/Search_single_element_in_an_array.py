"""
Search Single Element in a sorted array
Problem Statement: Given an array of N integers. Every number in the array except one appears 
twice. Find the single number in the array.

SINGLE ELEMENT IN A SORTED ARRAY — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array where every element appears exactly twice except for one
element that appears once.

I need to find and return that single element."


2. BRUTE FORCE

"The straightforward approach would be to go through the array and
compare the elements in pairs until I find an element that does not
have a matching pair.

This would work, but in the worst case it would take O(n) time."


3. OPTIMIZE

"Since the array is sorted and all the duplicate elements appear next
to each other, I can optimize this using binary search.

I can use the positions of the pairs to determine whether the single
element is on the left or right side."


4. KEY OBSERVATION

"The key observation is that before the single element, every pair
starts at an even index.

For example:

[1, 1, 2, 2, 3, 4, 4, 5, 5]

 0  1  2  3  4  5  6  7  8

Before the single element:

1,1 → indices 0,1
2,2 → indices 2,3

So the pairs start at even indices.

After the single element appears, this pattern becomes shifted.

So I make mid even and compare arr[mid] with arr[mid + 1].

If they are equal, the pair is correct and the single element must be
to the right.

If they are different, the pattern is broken, so the single element is
at mid or somewhere to the left."


5. APPROACH

"I'll initialize low at the beginning and high at the end.

While low is less than high, I'll calculate mid.

If mid is odd, I'll subtract one to make it even. This makes mid point
to where a pair should begin.

Then I'll compare arr[mid] with arr[mid + 1].

If they are equal, this is a normal pair, so the single element must be
after this pair. I'll move low to mid + 2.

If they are different, the pair pattern has been broken, so the single
element must be at mid or somewhere to the left. I'll set high to mid.

Eventually low and high will meet at the single element, so I'll return
arr[low]."


6. WHILE CODING

"I'm calculating mid and making sure it is even so that it points to
the expected beginning of a pair.

If arr[mid] equals arr[mid + 1], I know this pair is correct, so I can
remove both elements from my search space and move low to mid + 2.

If they are different, the pair pattern is broken, which tells me the
single element is at mid or to the left.

I use high = mid instead of mid - 1 because mid itself could be the
single element.

Once low equals high, I've found the single element."


7. EDGE CASES

"Some edge cases I would consider are the single element being at the
beginning, the single element being at the end, and an array containing
only one element."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space using
binary search.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:

Make MID EVEN first:

mid is odd
→ mid--


Then check the pair:

arr[mid] == arr[mid + 1]

→ pair is CORRECT
→ single is on the RIGHT
→ low = mid + 2


arr[mid] != arr[mid + 1]

→ pair is BROKEN
→ single is at MID or LEFT
→ high = mid


WHY MAKE MID EVEN?

Because a normal pair should look like:

even index, odd index

0,1
2,3
4,5
6,7


EASIEST WAY TO REMEMBER:

Make mid even
      ↓
Check mid with mid + 1
      ↓
PAIR MATCHES?
YES → skip pair → RIGHT
NO  → single is MID or LEFT


Example:

[1, 1, 2, 2, 3, 4, 4, 5, 5]
             ↑
             3

Before 3:
pairs follow even → odd

After 3:
pair pattern shifts

Answer = 3
"""
class Solution:
    def single_element(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            # Make mid even so it points
            # to the beginning of a pair
            if mid % 2 == 1:
                mid -= 1

            # Pair is correct, single is on the right
            if arr[mid] == arr[mid + 1]:
                low = mid + 2

            # Pair is broken, single is at mid or left
            else:
                high = mid

        return arr[low]


arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]

obj = Solution()
result = obj.single_element(arr)

print("Single element:", result)

"""
The pair pattern has already broken. Therefore, the single element must be at mid or 
somewhere before it.
"""