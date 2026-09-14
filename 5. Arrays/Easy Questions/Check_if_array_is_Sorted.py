"""
Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.
"""

def is_sorted(arr):
    n = len(arr)

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False

    return True