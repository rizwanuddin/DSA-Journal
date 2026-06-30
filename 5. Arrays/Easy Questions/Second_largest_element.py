def second_largest_element(arr):
    n = len(arr)
    large = float("-inf")
    second_large = float("-inf")
    if n < 2:
        return -1
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    if second_large == "-inf":
        return -1
    return second_large

arr = [8,5,2,9,1]
print(second_largest_element(arr))