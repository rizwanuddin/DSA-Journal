#shifting method
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]     # save element to be inserted
        j = i - 1

        # shift elements greater than key one position right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # place key in correct spot

#swapping method
arr = [22, 5, 2, 8, 1]

def swapping_insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i

        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
"""
For loop : (1, 5), i = 1, 2, 3, 4
j = i
while j = 1, 2, 3, 4 and arr[0, 1, 2, 3] > arr[1, 2, 3, 4]
"""
swapping_insertion_sort(arr)