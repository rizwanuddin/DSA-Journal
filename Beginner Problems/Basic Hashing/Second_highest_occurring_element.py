class Solution:
    def mostFrequentElement(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        counts = sorted(set(freq.values()), reverse=True)

        if len(counts) < 2:
            return -1

        second_count = counts[1]
        candidates = [num for num, count in freq.items() if count == second_count]

        return min(candidates)