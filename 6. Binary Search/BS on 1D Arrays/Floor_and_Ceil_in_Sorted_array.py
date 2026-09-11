"""
Floor and Ceil in Sorted Array
Problem Statement: ou're given an sorted array arr of n integers and an integer x. Find the floor 
and ceiling of x in arr[0..n-1]. The floor of x is the largest element in the array which is 
smaller than or equal to x. The ceiling of x is the smallest element in the array greater than 
or equal to x
remember - floor = largest value <= x
           ceil  = smallest value >= x
so you might be thinking by moving right or left we are giving away a hald completely but no we are
not because the array is sorted !!

FLOOR AND CEIL — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array and a target value x.

I need to find the floor and ceil of x.

The floor is the largest value that is less than or equal to x.

The ceil is the smallest value that is greater than or equal to x.

If either one does not exist, I'll return -1 for it."


2. BRUTE FORCE

"The straightforward approach would be to go through the entire array
and check every element.

I could keep track of the largest value less than or equal to x for the
floor, and the smallest value greater than or equal to x for the ceil.

This would work, but it would take O(n) time."


3. OPTIMIZE

"Since the array is sorted, I can optimize this using binary search.

I can actually find both the floor and ceil during the same binary
search by keeping track of possible answers."


4. KEY OBSERVATION

"The key observation is that if arr[mid] equals x, then x itself is both
the floor and the ceil, so I can stop immediately.

If arr[mid] is smaller than x, it could be my floor. I save it and
search to the right because I want to find a larger value that is still
less than or equal to x.

If arr[mid] is greater than x, it could be my ceil. I save it and
search to the left because I want to find a smaller value that is still
greater than or equal to x."


5. APPROACH

"I'll initialize low and high as the boundaries of the search space.

I'll initialize floor and ceil to -1 in case either one does not exist.

While low is less than or equal to high, I'll calculate mid.

If arr[mid] equals x, I'll set both floor and ceil to x and stop.

If arr[mid] is smaller than x, I'll save arr[mid] as a possible floor
and move low to mid + 1 to search for a better floor.

If arr[mid] is greater than x, I'll save arr[mid] as a possible ceil
and move high to mid - 1 to search for a better ceil.

At the end, I'll return both values."


6. WHILE CODING

"I'm initializing floor and ceil to -1 in case they don't exist.

If arr[mid] == x, x is both the floor and ceil.

If arr[mid] < x, I'm saving it as a possible floor and searching right
for a larger possible floor.

If arr[mid] > x, I'm saving it as a possible ceil and searching left
for a smaller possible ceil."


7. EDGE CASES

"Some edge cases I would consider are an empty array, x being smaller
than every element, x being larger than every element, x already
existing in the array, and duplicate values."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space by
half after every comparison.

The space complexity is O(1) because I only use a constant number of
variables."


MAIN RULE TO REMEMBER:

FLOOR = largest value <= x
CEIL  = smallest value >= x


arr[mid] == x
→ floor = x
→ ceil = x
→ DONE


arr[mid] < x
→ possible FLOOR
→ save arr[mid]
→ search RIGHT for a bigger floor


arr[mid] > x
→ possible CEIL
→ save arr[mid]
→ search LEFT for a smaller ceil


Example:

arr = [3, 4, 4, 7, 8, 10]
x = 5

Floor = 4
because 4 is the largest value <= 5

Ceil = 7
because 7 is the smallest value >= 5
""" 
class Solution:
    def floor_ceil(self, arr, x):
        low = 0
        high = len(arr) - 1
        floor = -1
        ceil = -1
        while low <= high:
            mid = (low  + high) // 2
            if arr[mid] == x:
                floor = arr[mid]
                ceil = arr[mid]
                break
            elif arr[mid] < x:
                floor = arr[mid]
                low = mid + 1
            else:
                ceil = arr[mid]
                high = mid - 1
        return floor, ceil
# Driver code
arr = [3, 4, 4, 7, 8, 10]
x = 5

obj = Solution()

floor, ceil = obj.floor_ceil(arr, x)

print("Floor:", floor)
print("Ceil:", ceil)
            
                

"""
FLOOR AND CEIL — FULL THINK ALOUD WHILE CODING


"I'm first going to create a class called Solution."

class Solution:


"Inside the class, I'll define a method called floor_ceil.

This method takes arr, which is my sorted array, and x, which is
the target whose floor and ceil I'm trying to find."

    def floor_ceil(self, arr, x):


"Since the array is sorted, I'm going to use binary search.

I'll initialize low to 0 and high to the last index of the array.
These represent the boundaries of my current search space."

        low = 0
        high = len(arr) - 1


"Now I need to keep track of both the floor and the ceil.

I'll initialize both of them to -1.

If a floor or ceil doesn't exist, its value will remain -1."

        floor = -1
        ceil = -1


"Now I'll start my binary search.

As long as low is less than or equal to high, there are still
elements left in my search space."

        while low <= high:


"I'll calculate the middle index of my current search space."

            mid = (low + high) // 2


"Now there are three possible cases.

First, if the middle element is exactly equal to x, then x itself
is both the largest value less than or equal to x and the smallest
value greater than or equal to x.

So x is both the floor and the ceil."

            if arr[mid] == x:
                floor = arr[mid]
                ceil = arr[mid]


"Since I already found the exact target, there cannot be a better
floor or ceil, so I can stop the binary search."

                break


"Now for the second case, if arr[mid] is smaller than x,
then arr[mid] is a possible floor."

            elif arr[mid] < x:


"So I'll save arr[mid] as my current floor."

                floor = arr[mid]


"But I want the LARGEST value that is still less than or equal to x.

Since the array is sorted, there might be a larger valid floor
somewhere to the right.

Also, everything to the left is smaller than my current floor,
so it cannot give me a better answer.

Therefore, I'll move low to mid + 1 and search the right side."

                low = mid + 1


"The final case is when arr[mid] is greater than x.

In that case, arr[mid] is a possible ceil."

            else:


"So I'll save arr[mid] as my current ceil."

                ceil = arr[mid]


"But I want the SMALLEST value that is still greater than or equal
to x.

Since the array is sorted, there might be a smaller valid ceil
somewhere to the left.

Everything to the right would be even larger, so it cannot give
me a better ceil.

Therefore, I'll move high to mid - 1 and search the left side."

                high = mid - 1


"Once low becomes greater than high, the search space is empty.

At this point, floor contains the largest value less than or equal
to x, and ceil contains the smallest value greater than or equal
to x.

So I'll return both values."

        return floor, ceil


"Now I'm outside the class, so I'll write my driver code.

I'll create my sorted input array."

arr = [3, 4, 4, 7, 8, 10]


"I'll set x to 5, so I want to find the floor and ceil of 5."

x = 5


"Now I'll create an object of the Solution class so I can call
the floor_ceil method."

obj = Solution()


"I'll call floor_ceil using my array and x.

Since the method returns two values, I'll store them in the
variables floor and ceil."

floor, ceil = obj.floor_ceil(arr, x)


"Finally, I'll print both results."

print("Floor:", floor)
print("Ceil:", ceil)
"""