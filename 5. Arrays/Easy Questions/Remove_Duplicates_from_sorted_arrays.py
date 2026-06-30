def remove_duplicates(arr):
    n = len(arr)
    i = 0
    for j in range(1,n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
            
    return arr[:i + 1]
sorted_arr = [1,2,2,4,9,9]
print(remove_duplicates(sorted_arr))