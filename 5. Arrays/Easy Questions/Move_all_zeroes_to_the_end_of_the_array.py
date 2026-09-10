"""
I’m using a two-pointer approach to move all the zeroes to the end while keeping the non-zero 
elements in the same order. First, I use a loop to find the first zero in the array and store 
its index in j. If I don’t find any zero, I can return immediately because there’s nothing to 
move. Once I find the first zero, I start another pointer i from the position after j. Whenever 
i finds a non-zero element, I swap it with the zero at j, and then move j forward so it points 
to the next position where a non-zero value should go. I continue until I reach the end of the 
array. This moves all non-zero values toward the front and pushes the zeroes toward the end. The 
time complexity is O(n) because I go through the array at most twice, and the space complexity is 
O(1) because I modify the original array in-place.

1. Find the first 0
→ j points to it

2. Start checking after j

3. Found non-zero?
→ swap arr[i] with arr[j]
→ j++

4. Keep going until the end
"""
def movezeroes(arr):
    n = len(arr)
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    if j == -1:
        return 
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        



arr = [0, 1, 0, 3, 12]