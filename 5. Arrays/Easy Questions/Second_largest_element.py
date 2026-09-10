"""
Problem Statement: Given an array, find the second smallest and second largest element in the 
array. Print ‘-1’ in the event that either of them doesn’t exist. 

I’m using a single-pass approach to find the second largest element without sorting the array. I 
keep two variables: large for the largest number I’ve seen so far and second_large for the second 
largest. I initialize both to negative infinity so any real number can replace them. As I go 
through the array, if the current number is greater than large, then my old largest becomes the 
second largest, and the current number becomes the new largest. Otherwise, if the current number 
is smaller than large but greater than second_large, I update only second_large. I also check 
arr[i] != large so duplicates of the largest number don’t count as the second largest. At the 
end, I return second_large, or -1 if a second largest value doesn’t exist. The time complexity is 
O(n) because I go through the array once, and the space complexity is O(1) because I only use 
two extra variables.
"""

def second_largest_element(arr):
    n = len(arr)
    large = float("-inf")
    second_large = float("-inf")
    if n < 2:
        return -1
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    if second_large == "-inf":
        return -1
    return second_large

arr = [8,5,2,9,1]
print(second_largest_element(arr))