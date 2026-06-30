def rotate_by_one(arr):
    n = len(arr)
    if n == 0:
        return []
    temp = arr[0] #[1,2,3,4,5] --> [2,3,4,5,1]
    for i in range (1,n):
        arr[i-1] = arr[i]
    arr[-1] = temp
    return arr

arr = [1,2,3,4,5] 
print(rotate_by_one(arr))