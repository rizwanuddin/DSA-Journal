"""
Counting Occurences in  Sorted Array
"""
def first_occurrence(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                ans = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return ans

def last_occurrence(self, arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            ans = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans

def count_occerence(self, arr, target):
    first = self.first_occurence(arr, target)
    if first == -1:
        return 0
    last = self.first_occurence(arr, target)
    return last - first + 1


"""
Floor And Ceil in sorted array
"""
def floor_and_ceil(self, arr, target):
    low = 0
    high = len(arr) - 1
    floor = float("-inf")
    ceil = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            floor = arr[mid]
            ceil = arr[mid]
            break
        elif arr[mid] > target:
            high = mid - 1
            ceil = mid
        else:
            low = mid + 1
            floor = mid
    return floor, ceil


"""
Last Occurence in a sorted array
"""
def last_occurrence(self, arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            ans = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans


"""
Lower Bound 
"""
def lower_bound(self, arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans



"""
Minimum in rotated sorted array
"""
def minimum(self, arr):
    low = 0 
    high = len(arr) - 1
    while low < high :
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return arr[low]



"""
Number of times rotated sorted array has been rotated
"""
def rotated_times(self, arr):
    low = 0 
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low



"""
Peak element in an array
"""
def peak_element(self, arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low



"""
Search element in a rotated sorted array I
"""
def search_element(self, arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1




"""
Search element in a rotated sorted array II
"""
def search_ii(self, arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        if arr[low] <= arr[mid]:
            if arr[low] <= x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False




"""
Search Insert Position
"""
def search_insert(self, arr, x):
    low = 0
    high = len(arr) - 1
    n = len(arr)
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            left = mid + 1
    return ans 



"""
search single element in an array
"""
def search_insert(self, arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid % 2 == 1:
            mid -= 1
        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return arr[low]



"""
search target in sorted array
"""
def search_target(self, nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1



"""
Upper Bound
"""
def upper_bound(self, arr, x):
    low, high = 0, len(arr) - 1
    ans = len(arr)  # Default to length if no element > x

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = mid      # Store current mid as answer
            high = mid - 1 # Search left
        else:
            low = mid + 1  # Search right
    return ans

        




