"""
Remove Duplicates in-place from Sorted Array
Problem Statement: Given an integer array sorted in non-decreasing order, remove the 
uplicates in place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
If there are k elements after removing the duplicates, then the first k elements of the 
array should hold the final result. It doesn't matter what you leave beyond the first k elements.

Examples
Input: arr[]=[1,1,2,2,2,3,3]
Output: [1,2,3,_,_,_,_]
Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Input: arr[]=[1,1,1,2,2,3,3,3,3,4,4]
Output: [1,2,3,4,_,_,_,_,_,_,_]
Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.
            

I’m using a **two-pointer approach** because the array is already sorted, which means any duplicate values will be next to each other. 
I use `i` to represent the position of the **last unique element** that I’ve kept, while `j` moves through the array looking for new 
unique values. I start `i` at index `0` because the first element is automatically unique, and I start `j` from index `1`. For every 
element, I compare `nums[j]` with `nums[i]`. If they are the same, I simply continue because it’s a duplicate. If they are different, 
I’ve found a new unique value, so I move `i` forward by one and place `nums[j]` at `nums[i]`. This means that as I go through the array, 
all the unique elements are being collected at the beginning of the array. At the end, `i` represents the index of the last unique element, 
so I return `i + 1` to get the total number of unique elements. The **time complexity is O(n)** because I go through the array once, and 
the **space complexity is O(1)** because I modify the original array in-place and only use the two pointer variables.

"""

def remove_duplicates(arr):
    n = len(arr)
    i = 0
    for j in range(1,n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
            
    return arr[:i + 1]
sorted_arr = [1,2,2,4,9,9]
print(remove_duplicates(sorted_arr))

"""
WHY NOT BINARY SEARCH?

Binary search works when we can safely ignore half the array.

For removing duplicates, we need to check the ENTIRE array because
duplicates can exist anywhere.

Example:
[1, 1, 2, 2, 2, 3, 4, 4]

Even if binary search quickly finds the 2s, we still need to process
the 1s, 3s, 4s, etc.

So we cannot discard half → use a linear/two-pointer approach O(n).
"""