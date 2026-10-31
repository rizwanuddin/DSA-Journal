"""
Task Scheduler - Medium

You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. 
You are also given an integer n.
Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
Return the minimum number of CPU cycles required to complete all tasks.

Example 1:
Input: tasks = ["X","X","Y","Y"], n = 2
Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:
Input: tasks = ["A","A","A","B","C"], n = 3
Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.





# Task Scheduler: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given a list of tasks, where each task is a letter,
and a number n.
Each time unit, the CPU can either run one task or sit idle.
Two copies of the same task have to be at least n time units apart.
I need to return the minimum total time to finish all the tasks."

"I have a few quick questions before I start."

"Are the tasks only uppercase letters A to Z?"
→ I'll assume yes, so there are at most 26 task types.

"Can I run the tasks in any order?"
→ I'll assume yes.

"Can n be 0?"
→ I'll assume yes. Then there's no cooldown,
and the answer is just the number of tasks.

"Do idle time units count toward the total?"
→ I'll assume yes.

"Do I need to return the actual schedule, or just the time?"
→ I'll assume just the time.

"Okay, so the goal is to keep the CPU busy as much as possible,
and only go idle when every available task is still cooling down."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
tasks = ["A","A","A","B","C"], n = 3
```
"A has to wait 3 units between runs.
One schedule is A → B → C → idle → A → idle → idle → idle → A.
Answer: 9."

```
tasks = ["A","A","A","B","B","B"], n = 2
```
"A → B → idle → A → B → idle → A → B.
Answer: 8."

"A few edge cases:"
- "n = 0: no cooldown, so the answer is the number of tasks."
- "One task: Answer: 1."
- "Every task is different: no waiting needed. Answer: the number of tasks."
- "Lots of task types, so they fill all the gaps: no idles at all."
- "Large n with one repeated task, like ["A","A"] with n = 5:
  A, then 5 idles, then A. Answer: 7."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I simulate the CPU one time unit at a time."

"At each time unit, I look through every task type,
skip the ones still cooling down,
and run the one with the most copies left.
If nothing is available, the CPU goes idle."

"I pick the one with the most copies left,
because that task creates the most waiting.
Getting it started early gives the other tasks a chance
to fill in its cooldown gaps."

"This works because it always makes the best move at each step,
and it keeps going until every task is done."

"The time is O(T * k),
where T is the total time, idles included,
and k is the number of task types.
Every time unit, I scan all k types."

"The space is O(k), for the counts and the cooldown times."

"The problem is that I re-scan every task type at every single time unit,
just to find the biggest available one."

## 4. Optimal solution

"The bottleneck is scanning every task type each time unit
to find the one with the most copies left."

"Instead of scanning all the types every time,
I can keep the available tasks in a max-heap,
and park the cooling-down tasks in a queue."

"The data structures I'll use are a max-heap and a queue."

"The max-heap holds the remaining counts of tasks that are ready to run,
because it gives me the task with the most copies left in O(log k)."

"The queue holds tasks that are cooling down,
along with the time they become ready again.
A queue works because tasks go in at increasing times,
so the one at the front is always the next one to come back."

"I only need the counts, not the letters,
because the task names don't change the answer."

"As I go, every time unit I add 1 to the clock."

"When the heap isn't empty, I pop the task with the most copies left,
and run one copy of it.
If it still has copies left, I put it in the queue,
with the time it'll be ready again, which is now plus n."

"When the task at the front of the queue is ready, at the current time,
I move it back into the heap."

"When both the heap and the queue are empty, every task is done.
At the end, I return the clock."

"The time is O(T * log k).
Each time unit does a constant number of heap and queue operations.
Since there are only 26 letters, log k is tiny,
so it's really just O(T).
In the worst case, T can be about m times (n + 1),
where m is the number of tasks."

"The space is O(k), so at most 26 entries, which is O(1)."

"So I go from O(T * k) down to O(T * log k)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll import Counter and deque from collections, and heapq."

"Then I'll make a class called Solution,
and a function called leastInterval that takes self, tasks, and n."

"I'll start by counting each task with Counter,
and store it in count.
That gives me how many copies of each letter there are."

"Then I build heap as a list of the negative counts.
I'm making them negative because heapq is a min-heap,
and I want the task with the most copies on top.
I only keep the counts, because the letters don't matter for the answer."

"Then I call heapq.heapify on it, so it becomes a valid heap in O(k)."

"Next, I set t to 0.
This is my clock."

"Then I create an empty deque called queue.
It holds pairs of the remaining count and the time that task is ready again."

"Now I start a while loop that runs while the heap or the queue isn't empty.
If either one still has something, there are tasks left to do."

"Inside it, I add 1 to t.
Every loop is one time unit, whether I run a task or go idle."

"Then I check if the heap isn't empty."

"If it isn't, I pop the top, and add 1 to it, and store it in cnt.
The count is negative, so adding 1 means one copy has been run.
For example, -3 becomes -2."

"Then I check if cnt is not 0.
If it's not 0, there are still copies left.
So I add the pair (cnt, n + t) to the queue.
n + t is the time when this task can be run again."

"If cnt is 0, that task is completely done,
so I don't add it anywhere."

"If the heap was empty, the CPU is idle for this time unit,
and I just skip down."

"Next, I check if the queue isn't empty,
and the task at the front has a ready time equal to t."

"If so, its cooldown is over, so I pop it from the front,
and push its count back into the heap.
It's now ready to run starting next time unit."

"When the loop ends, every task has been run,
so I return t."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "["A","A","A","B","C"], n = 3: the heap starts with -3, -1, -1.
  At t = 1, I run A. It becomes -2, and goes to the queue, ready at 4.
  At t = 2, I run B. It's done.
  At t = 3, I run C. It's done.
  At t = 4, the heap is empty, so it's idle.
  A's ready time is 4, so it goes back to the heap.
  At t = 5, I run A. It becomes -1, ready at 8.
  t = 6, 7, and 8 are idle. At t = 8, A goes back to the heap.
  At t = 9, I run A, and it's done.
  Both are empty, so I return 9. That matches."
- "["A","A","A","B","B","B"], n = 2: A and B take turns,
  with one idle after each pair, so I return 8. That matches."
- "n = 0: each task goes into the queue with a ready time equal to t,
  so it comes right back in the same step, and there are no idles.
  I return the number of tasks."
- "One task: one time unit, and I return 1."
- "All different tasks: each one finishes in one run, so there's no waiting."
- "["A","A"], n = 5: A runs at t = 1, and is ready at 6.
  t = 2 through 6 are idle. A runs at t = 7. I return 7."

"The output matches what I expected for all of them."

"To recap, time is O(T * log k), which is basically O(T),
and space is O(1), since there are at most 26 task types."

"If they want it faster, there's a math formula.
The most frequent task decides the shape of the schedule.
If it appears maxFreq times, it makes maxFreq - 1 blocks of length n + 1,
plus one last row for every task that ties for the max count.
So the answer is (maxFreq - 1) * (n + 1) + countOfMaxFreq.
But if there are so many tasks that they fill every gap,
there are no idles, and the answer is just len(tasks).
So I return the bigger of those two.
That's O(m) time and O(1) space."
"""
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        t = 0
        queue = deque()
        while heap or queue:
            t += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    queue.append((cnt, n + t))
            if queue and queue[0][1] == t:
                heapq.heappush(heap, queue.popleft()[0])
        return t


            
