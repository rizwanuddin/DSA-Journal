"""
Find Minimum In Rotated Sorted Array - Explanation

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 
and n times. For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array
6 times produces the original array. Assuming all elements in the rotated sorted array nums are unique, return the 
minimum element of this array. A solution that runs in O(n) time is trivial, can you write an algorithm that runs 
in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2]
Output: 1

Example 2:
Input: nums = [4,5,0,1,2,3]
Output: 0

Example 3:
Input: nums = [4,5,6,7]
Output: 4



## Find Minimum In Rotated Sorted Array

**Clarify:**
- so the array was sorted originally, then rotated some number of times
- I need to find the minimum, and all elements are unique
- O(n) is easy, they want O(log n), so binary search is probably the move

**Brute force:**
- just scan the whole array and track the smallest value I see
- that's O(n), works but not what they're asking for

**Optimize:**
- since it's a rotated sorted array, there's still some sorted structure left in there, so I can binary search on it
- that gets me O(log n)

**Key observation:**
- if I look at the middle element and compare it to the last element, that tells me which half is actually sorted
- if nums[mid] is bigger than nums[high], that means the minimum has to be somewhere to the right of mid, because the left side including mid is still in the "bigger" rotated chunk
- if nums[mid] is smaller or equal to nums[high], that means mid itself could be the minimum, or the minimum is somewhere to its left, so I don't throw away mid, I just bring high down to mid

**Approach:**
- set low to 0, high to the last index
- loop while low is less than high
- find mid
- if nums[mid] is greater than nums[high], the minimum is to the right, so move low to mid plus 1
- otherwise, the minimum is at mid or to its left, so bring high down to mid
- once the loop ends, low and high meet at the minimum, so return nums[low]

**While coding:**
- first I make a class called Solution
- then a function called search_minimum that takes nums
- I set low to 0 and high to len(nums) minus 1
- I start a while loop that runs while low is less than high
- inside, I get mid as low plus high divided by 2
- I compare nums[mid] to nums[high]
- if nums[mid] is bigger, I know the minimum is on the right side, so I move low to mid plus 1
- otherwise, I bring high down to mid, since mid could still be the answer
- once the loop ends, I just return nums[low], since low and high have converged on the minimum

**Edge cases:**
- if the array isn't rotated at all, like [4,5,6,7], this should still correctly return the first element
- if there's only one element, low and high start equal, loop doesn't even run, just returns that one value
- if the minimum is right at the start or right at the end, the comparison logic still handles it fine since it's always comparing against nums[high]

**Complexity:**
- time is O(log n) since the search space cuts in half every step
- space is O(1), just a couple of variables
"""
class Solution:
    def search_minimum(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low  + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]