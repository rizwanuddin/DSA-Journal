def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]     # save element to be inserted
        j = i - 1

        # shift elements greater than key one position right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # place key in correct spot