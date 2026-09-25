"""
Count of odd numbers in Array
"""
class Solution:
    def countOdd(self, arr):
        count_odd = 0
        for num in arr:
            if num % 2 != 0:
                count_odd += 1
        return count_odd