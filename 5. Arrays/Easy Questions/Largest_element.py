def largest_element(arr, l):
    largest = arr[0]
    for i in range(l):
        if arr[i] > l:
            l = arr[i]
    return largest

arr = [6,3,2,4,1]
l = len(arr)
print(largest_element(arr, l))