def bubble_sort(arr, n):
    # Base case: only one element left
    if n == 1:
        return

    did_swap = False  # Flag to detect swap

    # Single pass: move the largest to the end
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            did_swap = True

    # If no swaps occurred, list is already sorted
    if not did_swap:
        return

    # Recurse on the smaller array
    bubble_sort(arr, n - 1)

"""
n = 4
loop runs : n - 1 = 3 = 0, 1, 2
4, 5, 2, 1
4, 2, 5, 1
4, 2, 1, 5
now the length (which is n here) decreases bu 1
n = 3
loop runs : n - 1 = 2 = 0, 1
2, 4, 1, 5
2, 1, 4, 5
n = 2
loop runs : n - 1 = 1 = 0
1, 2, 4, 5
n = 1, BEST CASE ( as n == 1 ) CALLED RESURSIVE UNWINDS AND RETURNS
"""


arr = [5,4,2,1]
n = len(arr)
result = bubble_sort(arr, n)