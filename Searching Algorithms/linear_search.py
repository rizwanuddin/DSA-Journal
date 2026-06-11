"""
All of these use linear search logic.
First occurrence: O(n)
Last occurrence: O(n)
All occurrences: O(n)
2D search: O(rows * columns)
Min/max: O(n)
"""
# 1. Find first occurrence
def first_occurences(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i #finding the index of the first occurence
    return -1  

# 2. Find last occurrence
def last_occurence(arr, target):
    last_index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            last_index = i
    return last_index

# 3. Find all occurrences
def all_occurences(arr, target):
    result = []
    for i in range(len(arr)):
        if arr[i] == target:
            result.append(i) #this stores the index of the occurences
    return result

# 4. Search in a 2D array
def search_2d(matrix, target):
    for i in range(len(matrix)): # matrix[row][column] len of matrix is number of rows
        for j in range(len(matrix[i])): # and len of matrix[i] is number of columns
            if matrix[i][j] == target:
                return True
    return False        

# 5. Find minimum element 
def find_min(arr):
    if len(arr) == 0: # If the array is empty, this line causes an error: IndexError: list index out of range
        return None
    min_index = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_index:
            min_index = arr[i]
    return min_index
#If the array is empty, accessing arr[0] will cause an error. 
# So before initializing min or max with the first element,
#  I check whether the array length is zero. If it is empty,
#  I return None or handle it based on the requirement.

# 5. Find maximum element
def find_min(arr):
    if len(arr) == 0:
        return None
    max_index = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_index:
            max_index = arr[i]
    return max_index