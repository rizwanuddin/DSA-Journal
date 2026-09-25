"""
Sum of Highest and Lowest Frequency
"""
class Solution:
    def sumHighestLowestFreq(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        return max(freq.values()) + min(freq.values())