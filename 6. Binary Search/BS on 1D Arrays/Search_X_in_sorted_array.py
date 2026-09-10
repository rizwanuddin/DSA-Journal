"""
Binary Search: Explained
Problem statement: You are given a sorted array of integers and a target, your task is to search 
for the target in the given array. Assume the given array does not contain any duplicate numbers.

BINARY SEARCH — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array with no duplicate elements and a target value. We need to
find the target and return its index. If the target is not present,
we return -1."


2. BRUTE FORCE

"The straightforward approach would be to use linear search and traverse
the entire array until we find the target.

This would work, but in the worst case we would have to check every
element, giving us O(n) time complexity."


3. OPTIMIZE

"However, we can do better by taking advantage of the fact that the
array is sorted.

Since it is sorted, we can use binary search and eliminate half of the
remaining search space after every comparison."


4. KEY OBSERVATION

"The key observation is that if we compare the target with the middle
element, we can determine which half of the array could contain the
target.

If the target is greater than the middle element, we only need to search
the right half.

If the target is smaller than the middle element, we only need to search
the left half."


5. APPROACH

"I'll maintain two pointers, left and right, which represent the
boundaries of the current search space.

While left is less than or equal to right, I'll calculate the middle
index.

If the middle element equals the target, I'll return its index.

If the middle element is smaller than the target, I'll move left to
mid + 1 and continue searching the right half.

Otherwise, I'll move right to mid - 1 and continue searching the left
half.

If the search space becomes empty, that means the target does not exist,
so I'll return -1."


6. WHILE CODING

"I'm initializing left at the beginning of the array and right at the
end of the array.

I'm using left <= right because as long as the boundaries haven't
crossed, there are still elements left to search.

I'm calculating mid to divide the current search space into two halves.

Based on the comparison with the middle element, I update one of the
boundaries and eliminate the half that cannot contain the target."


7. EDGE CASES

"Some edge cases I would consider are an empty array, an array with only
one element, the target being at either end of the array, and the target
not being present at all."


8. COMPLEXITY

"The time complexity is O(log n) because we reduce the search space by
half after every comparison.

The space complexity is O(1) because we only use a constant number of
variables such as left, right, and mid."
"""

class Solution:
    def binarySearch(self, nums: [int], target: int) -> int:
        # Edge case: empty array...actaully this edge case is automatically handled by the normal code
        if not nums:
            return -1
        
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]  # sorted list
    target = 6  # target element to search

    obj = Solution()
    ind = obj.binarySearch(a, target)

    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)