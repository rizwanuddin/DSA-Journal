"""
Find Second Smallest and Second Largest Element in an array
Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
Examples

Example 1:
Input:
 [1, 2, 4, 7, 7, 5]  
Output:
Second Smallest : 2  
Second Largest : 5  
Explanation:
  The elements are sorted as 1, 2, 4, 5, 7, 7.  
Hence, the second smallest element is 2, and the second largest element is 5.
Example 2:
Input:
 [1]  
Output:
Second Smallest : -1  
Second Largest : -1  
Explanation:
  Since there is only one element in the array, it is both the largest and smallest element.  
Therefore, there is no second smallest or second largest element present.



SECOND LARGEST & SECOND SMALLEST — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array of numbers.

I need to find the second largest and second smallest DISTINCT elements.

If either one doesn't exist, I'll return -1."


2. BRUTE FORCE

"The straightforward approach would be to sort the array.

Then I could find the first distinct value after the smallest and the
first distinct value before the largest.

This would work, but sorting takes O(n log n) time."


3. OPTIMIZE

"We can do better by finding both values in a single traversal.

For second largest, I'll maintain the largest and second largest values
I've seen so far.

For second smallest, I'll maintain the smallest and second smallest
values I've seen so far."


4. KEY OBSERVATION

"For second largest, whenever I find a new largest value, the old
largest automatically becomes the second largest.

Otherwise, if the current value is smaller than the largest but greater
than the second largest, it becomes the new second largest.

The second smallest follows the opposite logic.

Whenever I find a new smallest value, the old smallest becomes the
second smallest.

Otherwise, if the current value is greater than the smallest but
smaller than the second smallest, it becomes the new second smallest."


5. APPROACH

"For second largest, I'll initialize large and second_large to negative
infinity.

As I go through the array, if the current value is greater than large,
I'll move the old large into second_large and make the current value
the new large.

Otherwise, if it's greater than second_large and different from large,
I'll update second_large.

For second smallest, I'll do the opposite using positive infinity.

If the current value is smaller than smallest, I'll move the old
smallest into sec_smallest and update smallest.

Otherwise, if it's smaller than sec_smallest and different from
smallest, I'll update sec_smallest."


6. WHILE CODING

"For second largest, I'm starting both values at negative infinity."

large = float("-inf")
second_large = float("-inf")

"If I find a new largest value, the previous largest becomes my second
largest."

if arr[i] > large:
    second_large = large
    large = arr[i]

"Otherwise, I'm checking whether the current value can become my second
largest while making sure it isn't equal to the largest."

elif arr[i] > second_large and arr[i] != large:
    second_large = arr[i]

"For second smallest, I'm doing the exact opposite."

smallest = float("inf")
sec_smallest = float("inf")

"If I find a new smallest value, the previous smallest becomes my second
smallest."

if arr[i] < smallest:
    sec_smallest = smallest
    smallest = arr[i]

"Otherwise, I'm checking whether the current value can become my second
smallest."

elif arr[i] < sec_smallest and arr[i] != smallest:
    sec_smallest = arr[i]


7. EDGE CASES

"If there are fewer than two elements, a second largest or second
smallest cannot exist."

if len(arr) < 2:
    return -1

"If all elements are equal, there is no second distinct largest value."

if second_large == float("-inf"):
    return -1

"Similarly, if there is no second distinct smallest value, I'll return
-1."

if sec_smallest == float("inf"):
    return -1


8. COMPLEXITY

"The time complexity is O(n) because I only need to traverse the array
once for each function.

The space complexity is O(1) because I only use a constant number of
extra variables."
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
    if second_large == float("-inf"):
        return -1
    return second_large

def second_smallest(self, arr, n):
    n = len(arr)
    smallest = float("inf")
    sec_smallest = float("inf")
    for i in range(n):
        if arr[i] < smallest:
            sec_smallest = smallest
            smallest = arr[i]
        elif arr[i] < sec_smallest and arr[i] != smallest:
            sec_smallest = arr[i]
    if sec_smallest == float("inf"):
        return -1
    return sec_smallest

arr = [8,5,2,9,1]
print(second_largest_element(arr))