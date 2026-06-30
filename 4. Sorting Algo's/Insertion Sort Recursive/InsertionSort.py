def insertion_sort(arr,i, n):
    if i == n:
        return
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
    insertion_sort(arr, i + 1, n)

arr = [7,5,1,9]
n = len(arr)
print(insertion_sort(arr, 1, n))
