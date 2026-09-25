"""
Highest Occurring Element in an Array
"""
class Solution:
    def mostFrequentElement(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_count = 0
        result = None
        for num, count in freq.items():
            if count > max_count:
                max_count = count
                result = num

        return result
# or

class Solution:
    def mostFrequentElement(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        max_count = 0
        result = None
        for num, count in freq.items():
            if count > max_count:
                max_count = count
                result = num
        return result