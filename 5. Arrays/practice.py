"Largest element in the array"
def largest_element(self, arr):
    largest = float("-inf")
    for element in arr:
        if element > largest:
            largest = element
    return largest




"Second largest and second smallest element in the array"
def second_largest(self, arr, n):
    n = len(arr)
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] != largest and arr[i] > second_largest:
            second_largest = arr[i]
    if second_largest == float("-inf"):
        return -1
    return second_largest

def second_smallest(self, arr, n):
    n = len(arr)
    smallest = float("inf")
    sec_smallest = float("inf")
    for i in range(n):
        if arr[i] < smallest:
            sec_smallest = smallest
            smallest = arr[i]
        elif arr[i] < sec_smallest and arr[i] != smallest:
            sec_smallest = arr[i]
    if sec_smallest == float("inf"):
        return -1
    return sec_smallest




"Check if the array is sorted"
def sorted_check(self, arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True




"Remove duplicates from sorted array"
def remove_duplicate(self, arr):
    n = len(arr)
    left = 0
    for i in range(1, n):
        if arr[i] != arr[left]:
            left += 1
            arr[left] = arr[i]
    return arr[:left + 1]


