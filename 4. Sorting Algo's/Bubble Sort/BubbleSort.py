def bubbleSort(arr):
    l = len(arr)
    for i in range(l - 1):
        swapped = False
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break        

arr = [7, 3, 2, 5, 1]
bubbleSort(arr)
print(arr)