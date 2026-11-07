"""
Kth largest element in a stream of running integers - Hard

Implement a class KthLargest to find the kth largest number in a stream. It should have the following methods:

KthLargest(int k, int [] nums) Initializes the object with the integer k and the initial stream of numbers in nums
int add(int val) Appends the integer val to the stream and returns the kth largest element in the stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:

Input: [KthLargest(3, [1, 2, 3, 4]), add(5), add(2), add(7)]

Output: [null, 3, 3, 4]

Explanation: initial stream = [1, 2, 3, 4], k = 3.

add(5): stream = [1, 2, 3, 4, 5] -> returns 3

add(2): stream = [1, 2, 2, 3, 4, 5] -> returns 3

add(7): stream = [1, 2, 2, 3, 4, 5, 7] -> returns 4
Example 2:

Input: [KthLargest(2, [5, 5, 5, 5], add(2), add(6), add(60)]

Output: [null, 5, 5, 6]

Explanation: initial stream = [5, 5, 5, 5], k = 2.

add(2): stream = [5, 5, 5, 5, 2] -> returns 5

add(6): stream = [5, 5, 5, 5, 2, 6] -> returns 5

add(60): stream = [5, 5, 5, 5, 2, 6, 60] -> returns 6
"""
import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) < self.k :
            return -1
        if len(self.heap) > self.k :
            heapq.heappop(self.heap)
        return self.heap[0]
    

