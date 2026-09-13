"""
Two Sum
Optimal Approach - Hashing
"""
class Solution:
    def two_sum_indices(self, arr, target):
        mp = {}
        for i, num in enumerate(arr):
            compliment = target - num
            if compliment in mp:
                return [mp[compliment], i]
            mp[num] = i
        return [-1, -1]




"""
Sort an array of 0's 1's and 2's
Optimal Approach - Dutch National Flag/Three pointers
"""
class Solution:
    def sortZeroOneTwo(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1




"""
Find the Majority Element that occurs more than N/2 times
Optimal Approach - Boore-Moore voting algorithm
"""
class Solution:
    def majority(self, arr):
        candidate = None
        count = 0
        for num in arr:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate




"""
Maximum Subarray Sum in an Array
Optimal Approach - Kadane's Algorithm
"""
class Solution:
    def max_subarray(self, arr):
        maximum = float("-inf")
        current_sum = 0
        for num in arr:
            current_sum += num
            maximum = max(current_sum, maximum)
            if current_sum < 0 :
                current_sum = 0
        return maximum
"""one more feature - return that subarray too"""
class Solution:
    def max_subarray(self, arr):
        maximum = float("-inf")
        current_sum = 0

        n = len(arr)

        start = 0
        ans_start = -1
        ans_end = -1
        for i in range(n):
            current_sum += arr[i]
            if current_sum > maximum:
                maximum = current_sum
                ans_start = start
                ans_end = i

            if current_sum < 0 :
                current_sum = 0
                start = i + 2
                
        print("Maximum-sum subarray:", arr[ans_start:ans_end+1])
        return maximum




"""
Stock Buy And Sell
Optimal Approach - Greedy Algorithm
"""
class Solution:
    def stockbuyorsell(self, arr):
        min_price = float("inf")
        max_profit = 0
        for price in arr:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit




"""
Rearrange Array Elements by Sign
Optimal Approach - Frredy Algorithm
"""
class Solution:
    def rearrange_by_sign(self, A):
        n = len(A)
        arr = [0] * n

        neg_pointer = 1
        pos_pointer = 0

        for i in range(n):
            if A[i] < 0:
                arr[neg_pointer] = A[i]
                neg_pointer += 2
            else:
                arr[pos_pointer] = A[i]
                pos_pointer += 2
        return arr




"""
Next Permutation
Optimal Approach - Next permutation algorithm
"""
class Solution:
    def next_permuatation(self, arr):
        n = len(arr)
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        if pivot == -1:
            arr.reverse()
            return arr
        for i in range(n - 1, pivot, -1):
            if arr[i] > pivot:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
        left = pivot + 1
        right = n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr






    
                    
                

        
