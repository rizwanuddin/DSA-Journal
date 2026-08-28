"""
I’m using the Next Permutation algorithm to rearrange the array into the next lexicographically greater permutation. The idea is to make the smallest possible change that gives us a 
permutation larger than the current one. First, I scan the array from right to left to find the first position where arr[i] < arr[i + 1]; I call this the pivot. This is the position where 
I can make the permutation slightly larger. If I can’t find a pivot, the entire array is in descending order, meaning it is already the largest possible permutation, so I simply reverse it 
to get the smallest permutation. If a pivot exists, I scan from the end of the array and find the first element greater than arr[pivot], then swap it with the pivot. Searching from the 
right ensures I get the smallest value that is still greater than the pivot, so I don’t make the permutation unnecessarily large. Finally, I reverse everything after the pivot because that 
portion was originally in descending order, and reversing it puts it into the smallest possible order, giving me the immediate next permutation rather than just any larger permutation. The 
time complexity is O(n) because each step scans at most the length of the array, and the space complexity is O(1) because everything is modified in-place.
"""
class Solution:
    def next_permutation(self, arr):
        n = len(arr)

        # Step 1: Find the pivot pivot = -1
        
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        # If no pivot exists, array is in descending order
        if pivot == -1:
            arr.reverse()
            return arr

        # Step 2: Find the first element from the right
        # that is greater than arr[pivot]
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                # Step 3: Swap
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Step 4: Reverse everything after pivot
        left = pivot + 1
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr
