"""
Search In Rotated Sorted Array - Explanation

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 
and n times. For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not 
present.
You may assume all elements in the sorted rotated array nums are unique,
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2], target = 1
Output: 4

Example 2:
Input: nums = [3,5,6,0,1,2], target = 4
Output: -1



## Search in Rotated Sorted Array

**Clarify:**
- array was sorted originally, then rotated at some unknown point
- all elements are unique, need to find target's index, or return -1 if it's not there
- needs to run in O(log n), so has to be some form of binary search

**Brute force:**
- just scan the whole array looking for target
- that's O(n), works but doesn't meet the requirement

**Optimize:**
- even though the whole array isn't sorted anymore, at least ONE half of it around mid is always sorted
- so I can figure out which half is sorted, check if target falls inside that sorted half, and binary search from there
- that gets me O(log n)

**Key observation:**
- if arr[low] is less than or equal to arr[mid], that means the left half is the sorted one
- if the left half is sorted, I just check if target falls between arr[low] and arr[mid], if yes I search left, if no I search right
- if the left half isn't sorted, that means the right half must be the sorted one instead
- same idea there, check if target falls between arr[mid] and arr[high], if yes search right, if no search left

**Approach:**
- set low to 0, high to the last index
- loop while low is less than or equal to high
- find mid, check if arr[mid] is target, return mid if so
- figure out which side is sorted by comparing arr[low] to arr[mid]
- if left side is sorted, check if target is inside that range, narrow low or high accordingly
- if right side is sorted instead, check if target is inside that range, narrow low or high accordingly
- if loop ends with nothing found, return -1

**While coding:**
- first I define the function search_element, taking arr and target
- I set low to 0 and high to len(arr) minus 1
- I start a while loop that runs while low is less than or equal to high
- inside, I get mid as low plus high divided by 2
- I check if arr[mid] equals target, if so I return mid right away
- then I check if arr[low] is less than or equal to arr[mid], that tells me the left side is sorted
- if the left side is sorted, I check if target is between arr[low] and arr[mid], if yes I bring high down to mid minus 1, otherwise I push low up to mid plus 1
- if the left side isn't sorted, that means the right side is sorted instead
- I check if target is between arr[mid] and arr[high], if yes I push low up to mid plus 1, otherwise I bring high down to mid minus 1
- if the loop finishes without returning anything, I return -1

**Edge cases:**
- if the array isn't rotated at all, this should still work like normal binary search
- if target isn't in the array at all, the loop just shrinks down to low greater than high, returns -1
- if there's only one element, it either matches target right away or returns -1 immediately

**Complexity:**
- time is O(log n), still cutting the search space in half every step
- space is O(1), just a few variables
"""
def search_element(self, arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # LEFT side is sorted
        if arr[low] <= arr[mid]:

            # Target lies inside sorted LEFT side
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # RIGHT side is sorted
        else:

            # Target lies inside sorted RIGHT side
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1