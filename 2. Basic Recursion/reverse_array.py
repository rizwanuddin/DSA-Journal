def reverse_array(array, start, end):
    while start < end :
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array
# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr, 0, len(arr)-1))  # Output: [5, 4, 3, 2, 1]    
print(" ".join(map(str, arr)))