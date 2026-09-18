"""
Find the Largest element in an array
Problem Statement: Given an array, we have to find the largest element in the array.
Examples

Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}  
Output:
 5  
Explanation:
5 is the largest element in the array.
Example 2:
Input:
 arr[] = {8, 10, 5, 7, 9}  
Output:
 10  
Explanation:
10 is the largest element in the array.




LARGEST ELEMENT IN AN ARRAY — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given an
array of numbers.

I need to find and return the largest element in the array."


2. BRUTE FORCE

"One approach would be to sort the array and return the last element.

This would work, but sorting would take O(n log n) time, and we don't
actually need the entire array to be sorted."


3. OPTIMIZE

"We can do better by going through the array once and keeping track of
the largest element seen so far.

This allows us to find the answer in O(n) time."


4. KEY OBSERVATION

"The key observation is that I only need to remember the largest value
I've seen so far.

Whenever I find an element greater than my current largest value, I
update largest."


5. APPROACH

"I'll initialize largest to negative infinity so that any number in the
array can replace it.

Then I'll go through every element in the array.

If the current element is greater than largest, I'll update largest.

After checking all the elements, I'll return largest."


6. WHILE CODING

"I'm initializing largest to negative infinity so this also works when
all the numbers in the array are negative."

largest = float("-inf")

"I'm going through every element and comparing it with the largest value
I've seen so far."

for element in arr:
    if element > largest:
        largest = element

"After processing the entire array, largest contains the maximum value."

return largest


7. EDGE CASES

"If the array could be empty, I should handle that before starting the
loop."

if not arr:
    return -1

"If the array contains all negative numbers, initializing largest to
negative infinity makes sure the correct largest negative number is
still found."

largest = float("-inf")

"If the array contains only one element, the loop will automatically
set largest to that element."


8. COMPLEXITY

"The time complexity is O(n) because I go through every element exactly
once.

The space complexity is O(1) because I only use one extra variable,
largest."
"""

# Function to find the largest element in the array
def findLargestElement(arr, n):
    largest = float("-inf")
    for element in arr:
        if element > largest:
            largest = element
    return largest

# Driver code
if __name__ == "__main__":
    # Array 1
    arr1 = [2, 5, 1, 3, 0]
    n = len(arr1)  # Size of the array
    max = findLargestElement(arr1, n)  # Call the function to find the largest element
    print("The largest element in the array is:", max)  # Output the result