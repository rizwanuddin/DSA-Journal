def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1 # target is in the right half
        else:
            high = mid - 1 # target is in the left half
    return -1
arr = [2, 4, 7, 9, 12, 15, 20]
target = 15
print(binary_search(arr, target))

