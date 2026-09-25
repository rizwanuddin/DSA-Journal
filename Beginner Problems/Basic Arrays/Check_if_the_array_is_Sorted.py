"""
Check if the Array is Sorted I
"""
class Solution:
    def arraySortedOrNot(self, arr):
        n = len(arr)
        for i in range(n - 1):
            if arr[i] > arr[i + 1] :
                return False
        return True
