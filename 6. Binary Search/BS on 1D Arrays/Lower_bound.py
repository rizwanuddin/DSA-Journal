"""
Implement Lower Bound
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find 
the lower bound of x.

LOWER BOUND — INTERVIEW EXPLANATION


1. CLARIFY

"Let me make sure I understand the problem correctly. We are given a
sorted array and a value x. I need to find the first index whose value
is greater than or equal to x.

If no such element exists, I return the length of the array."


2. BRUTE FORCE

"The straightforward approach would be to go through the array from
left to right and return the first index where arr[i] is greater than
or equal to x.

This would work, but in the worst case I would check every element,
giving O(n) time complexity."


3. OPTIMIZE

"Since the array is already sorted, I can do better using binary search.

Instead of checking every element, I can eliminate half of the remaining
search space after every comparison."


4. KEY OBSERVATION

"The key observation is that I am looking for the first element that is
greater than or equal to x.

If arr[mid] is greater than or equal to x, mid could be my answer, so
I save it. However, there might be an earlier valid index, so I continue
searching to the left.

If arr[mid] is smaller than x, then mid and everything before it cannot
be the answer, so I search to the right."


5. APPROACH

"I'll initialize low to 0 and high to the last index of the array.

I'll initialize ans to n, which will be my default answer if no lower
bound exists in the array.

While low is less than or equal to high, I'll calculate the middle index.

If arr[mid] is greater than or equal to x, I'll save mid as a possible
answer and move high to mid - 1 to search for an earlier valid index.

Otherwise, I'll move low to mid + 1 and search the right side.

When the search space becomes empty, I'll return ans."


6. WHILE CODING

"I'm initializing low and high as the boundaries of my search space.

I'm setting ans equal to n in case every element in the array is smaller
than x.

I'm using low <= high because as long as the boundaries haven't crossed,
there are still elements left to search.

If arr[mid] >= x, I'm saving mid as a possible answer and searching
left because I want the first valid index.

Otherwise, arr[mid] is too small, so I'm searching to the right."


7. EDGE CASES

"Some edge cases I would consider are an empty array, x being smaller
than every element, x being larger than every element, x already existing
in the array, and the array containing duplicate values."


8. COMPLEXITY

"The time complexity is O(log n) because I reduce the search space by
half after every comparison.

The space complexity is O(1) because I only use a constant number of
variables such as low, high, mid, and ans."


MAIN RULE TO REMEMBER:

Lower Bound = first index where arr[i] >= x

arr[mid] >= x
→ save mid
→ search LEFT

arr[mid] < x
→ search RIGHT
"""
class LowerBoundFinder:
    def lower_bound(self, arr: [int], x: int) -> int: # define the function
        n = len(arr) # initialize
        low = 0
        high = n - 1
        ans = len(arr)
        while low <= high: #loop end condition means i dont have elemets left in my search space
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
if __name__=="__main__":
    arr = [3, 5, 8, 15, 19]                # Sorted input array
    x = 9                                  # Target value

    finder = LowerBoundFinder()           # Create object   #I'll create an object of my LowerBoundFinder class.
    ind = finder.lower_bound(arr, x)      # Call method
    #I'll call the lower_bound method using my array and x, and store
    #the returned index in ind.

    print("The lower bound is the index:", ind)  # Output result
    


    
                


            
