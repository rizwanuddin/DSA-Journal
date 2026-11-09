"""
Task Scheduler

You are given a list of tasks represented by uppercase English letters ('A' to 'Z'), and an integer n representing 
a cooldown interval between two same tasks.
Each task takes exactly 1 CPU interval to complete.
Tasks can be executed in any order, but identical tasks must be separated by at least n intervals, during which 
the CPU may remain idle or execute other tasks.
Return the minimum number of CPU intervals required to complete all the tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
One valid execution order is:
A -> B -> idle -> A -> B -> idle -> A -> B
Total intervals = 8

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation:
A possible execution:
A -> B -> C -> D -> A -> B
No idle interval is needed as cooldown = 1.
"""
import heapq
from collections import Counter, deque

class Solution:
    def minCPU(self, tasks, n):
        count = Counter(tasks)          # TIME O(T): one pass | SPACE O(1): <= 26 keys
        heap = []                       # SPACE O(1): one count per letter, <= 26
        for c in count.values():        # <= 26 loops -> O(1)
            heap.append(-c)
        heapq.heapify(heap)             # TIME O(26) -> O(1)
        time = 0

        queue = deque()                 # SPACE O(1): <= 26 letters cooling
        while heap or queue:            # runs once per time unit -> O(answer) which is O(T x n)in worst case-- [A,A,A], n = 100  ->  A + 100 idles + A + 100 idles + A  = 203 loops
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1       # O(log 26) -> O(1)
                if cnt != 0:
                    queue.append((cnt, time + n))   # O(1)
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])   # O(1)
        return time
"""
T = number of tasks (the length of tasks)
k = number of distinct tasks → at most 26 (letters A to Z)
n = cooldown
"""
         

