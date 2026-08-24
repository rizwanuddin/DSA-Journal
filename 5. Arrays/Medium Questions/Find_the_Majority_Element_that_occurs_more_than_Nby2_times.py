"""
I’m using the Boyer-Moore Voting Algorithm to find the majority element, which is the element that appears more than n/2 times in the array. I maintain two 
variables: candidate, which stores the element that could be the majority, and count, which keeps track of its current vote count. As I go through the array, if 
count becomes 0, I choose the current number as my new candidate. Then, if the current number is equal to the candidate, I increment count, and if it’s different, 
I decrement count. The main idea is that different elements basically cancel each other out, so because the majority element appears more than all the other 
competing elements combined, it will eventually survive as the final candidate. Once I finish going through the array, I return that candidate. This algorithm 
assumes that a majority element is guaranteed to exist; if it isn’t guaranteed, I would need a second pass to verify that the candidate actually appears more than 
n/2 times. The time complexity is O(n) because I traverse the array once, and the space complexity is O(1) because I only use candidate and count.
"""
class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate