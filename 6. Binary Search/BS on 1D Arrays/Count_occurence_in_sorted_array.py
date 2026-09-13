"""
Count Occurrences in Sorted Array
Problem Statement: You are given a sorted array containing N integers and a number X, you have 
to find the occurrences of X in the given array.

Example 1:
Input:
 N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output: 4
Explanation:
 3 is occurring 4 times in 
the given array so it is our answer.

COUNT OCCURRENCES IN SORTED ARRAY — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array and a target value x.

I need to find how many times x appears in the array.

If x does not exist, I'll return 0."


2. BRUTE FORCE

"The straightforward approach would be to go through the entire array
and increment a counter every time I find x.

This would work, but it would take O(n) time."


3. OPTIMIZE

"Since the array is sorted, I can optimize this using binary search.

Instead of counting every occurrence individually, I can find the first
occurrence and the last occurrence of x.

Then I can calculate the total number of occurrences using:

last - first + 1"


4. KEY OBSERVATION

"The key observation is that all occurrences of x will be next to each
other because the array is sorted.

So I only need to know where the group of x values starts and where it
ends.

For the first occurrence, when I find x, I save the index and continue
searching LEFT.

For the last occurrence, when I find x, I save the index and continue
searching RIGHT."


5. APPROACH

"First, I'll use binary search to find the first occurrence of x.

When I find x, I'll save its index and continue searching to the left.

If the first occurrence is -1, then x does not exist, so I'll return 0.

Otherwise, I'll use another binary search to find the last occurrence.

When I find x this time, I'll save its index and continue searching to
the right.

Finally, I'll calculate the number of occurrences using:

last - first + 1"


6. WHILE CODING

"In first_occurrence, when I find x, I'm not returning immediately.

I'm saving mid and searching left because there might be an earlier
occurrence.

In last_occurrence, when I find x, I'm saving mid and searching right
because there might be a later occurrence.

Then in count_occurrences, I first check whether x exists.

If it does, I calculate the count using last - first + 1."


7. EDGE CASES

"Some edge cases I would consider are an empty array, the target not
existing, the target appearing once, the target appearing multiple
times, and every element being equal to the target."


8. COMPLEXITY

"Finding the first occurrence takes O(log n), and finding the last
occurrence also takes O(log n).

So the total time complexity is still O(log n).

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:

COUNT = LAST INDEX - FIRST INDEX + 1


FIRST OCCURRENCE:
find x
→ save mid
→ search LEFT


LAST OCCURRENCE:
find x
→ save mid
→ search RIGHT


Then:

count = last - first + 1


Example:

arr = [1, 2, 3, 3, 3, 4, 5]
x = 3

first = 2
last  = 4

count = 4 - 2 + 1
      = 3
"""
class Solution:
    def first_occurrence(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                ans = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def last_occurrence(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                ans = mid
                low = mid + 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def count_occurrences(self, arr, x):
        first = self.first_occurrence(arr, x)
        if first == -1:
            return 0
        last = self.last_occurrence(arr, x)
        return last - first + 1

arr = [1, 2, 3, 3, 3, 4, 5]
x = 3
obj = Solution()
count = obj.count_occurrences(arr, x)
print("Number of occurrences:", count)