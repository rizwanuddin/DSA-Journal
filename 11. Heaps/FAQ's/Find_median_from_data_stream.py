"""
Find Median from Data Stream

Implement a class that finds the median from a data stream. The median is the middle value 
in an ordered integer list. If the size of the list is even, there is no middle value, and 
the median is the mean of the two middle values.
Implement the MedianFInder class as follows:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the 
actual answer will be accepted.

Example 1:
Input: [MedianFinder(), addNum(1), addNum(2), addNum(3), findMedian()]
Output: [null, null, null, null, 2]
Explanation:
MedianFinder(): initializes the object.
addNum(1): adds 1 to the data structure
addNum(2): adds 2 to the data structure
addNum(3): adds 3 to the data structure
findMedian(): returns 2 as the median of [1, 2, 3]

Example 2:
Input: [MedianFinder(), addNum(1), addNum(6), findMedian(), addNum(3), findMedian()]
Output: [null, null, null, 3.5, null, 3]
Explanation:
MedianFinder(): initializes the object.
addNum(1): adds 1 to the data structure
addNum(6): adds 6 to the data structure
findMedian(): returns 3.5 as the median of [1, 6] -> (1 + 6) / 2 = 3.5
addNum(3): adds 3 to the data structure
findMedian(): returns 3 as the median of [1, 3, 6].




# Find Median from Data Stream: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I need to design a class with two functions.
addNum adds a number from a stream.
findMedian returns the median of all the numbers added so far."

"What is the median?
If I sort all the numbers, it's the middle one.
If the count is odd, it's the exact middle.
If the count is even, it's the average of the two middle numbers."

"Quick things I'd confirm:
will findMedian only be called after at least one number is added?
I'll assume yes.
Can numbers be negative or repeated? I'll assume yes, it doesn't matter.
Is findMedian called a lot? I'll assume both are called many times,
so I want both of them fast."

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"I'll just keep every number in a list.
In addNum, I append the number. Super simple."

"In findMedian, I sort the list,
and pick the middle one, or average the two middle ones."

### Time complexity

"Now what will be the time complexity?"

"addNum is just an append, so big O of 1."

"findMedian sorts the whole list.
If I've added n numbers so far, sorting takes n logarithmic of n.
Picking the middle is big O of 1.
So findMedian is big O of n log n, every single call."

"And here's the problem, agreed?
If findMedian is called after every add,
I'm sorting again and again, even though only one number changed."

### Space complexity

"Am I using any extra space?
The list holds every number, so that's big O of n."

"Obviously the interviewer will not be happy with n log n for every median,
and he'll ask me to optimize."

## Optimal

"Here's the key thing I notice.
To find the median, do I need everything sorted? No.
I only need the middle, agreed?"

"So what I'll do is, I'll split the numbers into two halves.
A smaller half, and a larger half."

"From the smaller half, I need its biggest number.
From the larger half, I need its smallest number.
Those two are exactly the middle of everything."

"So I'll use two heaps.
In case you don't know about them, nothing to worry about.
Just remember, a min-heap always gives me the smallest,
and a max-heap always gives me the biggest."

"The smaller half goes in a max-heap, so its biggest is on top.
The larger half goes in a min-heap, so its smallest is on top."

"Python only has a min-heap,
so for the max-heap I store the numbers as negative.
Then the biggest number becomes the smallest negative, right at the top."

"I need to keep two rules true all the time."

"Rule 1: everything in small is less than or equal to everything in large.
That's what makes them a smaller half and a larger half."

"Rule 2: the sizes differ by at most 1.
That's what keeps the middle right at the tops."

"What is the next step? Adding a number."

"If small is empty, or the number is less than or equal to small's top,
it belongs in the smaller half, so I push it into small.
Otherwise, it belongs in the larger half, so I push it into large.
That keeps rule 1 true."

"Then I check rule 2.
If small has more than one extra number,
I pop small's top and push it into large.
If large has more than one extra number,
I pop large's top and push it into small."

"Why does moving the top keep rule 1 safe?
Because the top of small is its biggest,
so it's still less than or equal to everything in large.
And the top of large is its smallest,
so it's still bigger than or equal to everything in small."

"Now finding the median is super simple."

"If both heaps are the same size, the count is even,
so the median is the average of the two tops."

"If small has one more, the middle is small's top.
If large has one more, the middle is large's top."

"I just peek, I don't pop anything. Done and dusted."

### Time complexity

"Now let's discuss the time complexity.
I'll say n is the number of numbers added so far."

"First, addNum.
First portion, the comparison with small's top, that's big O of 1.
Next portion, one push, that's logarithmic of n."

"Next portion, the rebalance.
In the worst case, I do one pop and one push.
Each is logarithmic of n."

"So addNum does at most one push, one pop, and one more push.
That's near about three into log n,
which is nothing but big O of log n."

"Now findMedian.
I just compare the sizes and peek at the tops.
Peeking a heap is just looking at index 0, so big O of 1.
So findMedian is big O of 1."

"If I compare with the brute force,
findMedian went from n log n down to 1,
and addNum went from 1 up to log n.
That's a great trade, because log n is tiny."

### Space complexity

"What about the space complexity?
Every number I add lives in exactly one of the two heaps.
Each heap holds about n by 2 numbers,
so together it's nothing but big O of n."

## Code

"In the constructor, I make two empty lists.
small is the max-heap for the smaller half, stored as negatives.
large is the min-heap for the larger half."

"In addNum, I check if small is empty,
or if num is less than or equal to negative small[0].
I put the negative sign there because small stores negatives,
so negative small[0] is the real biggest number in the smaller half."

"If that's true, I push negative num into small.
Otherwise, I push num into large."

"Then I check if small has more than large plus 1.
If yes, I pop from small, flip the sign back,
and push that value into large."

"Else, if large has more than small plus 1,
I pop from large, and push its negative into small."

"In findMedian, if both lengths are equal,
I return negative small[0] plus large[0], divided by 2.
I use slash, not double slash, because the median can be a decimal."

"Else if small is bigger, I return negative small[0]."

"Else, large is bigger, so I return large[0]."

## Quick check

```
addNum(1)
addNum(2)
findMedian()   → 1.5
addNum(3)
findMedian()   → 2
```

- "addNum(1): small is empty, so 1 goes into small. small is [-1]."
- "addNum(2): is 2 less than or equal to 1? No, so it goes into large.
  large is [2]. The sizes are 1 and 1, so they're balanced."
- "findMedian: the sizes are equal, so it's 1 plus 2, divided by 2, which is 1.5. Correct."
- "addNum(3): is 3 less than or equal to 1? No, so it goes into large.
  large is [2, 3]. large has 2, and small has 1.
  Is 2 more than 1 plus 1? No, so nothing moves."
- "findMedian: large has one more, so the median is large[0], which is 2. Perfect."

"A quick rebalance case: add 5, then 3, then 1.
5 goes into small. 3 is less than or equal to 5, so it goes into small too.
Now small has 2 and large has 0, so I move 5 into large.
1 goes into small. small holds 3 and 1, and large holds 5.
small has one more, so the median is 3. Correct."
"""
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []   # max-heap (negated values) -> SPACE O(n/2) for the smaller half
        self.large = []   # min-heap (normal values)   -> SPACE O(n/2) for the larger half

    def addNum(self, num):
        if not self.small or num <= -self.small[0]:        # O(1) check
            heapq.heappush(self.small, -num)                # O(log n)
        else:
            heapq.heappush(self.large, num)                 # O(log n)

        if len(self.small) > len(self.large) + 1:           # O(1) check
            val = -heapq.heappop(self.small)                # O(log n)
            heapq.heappush(self.large, val)                 # O(log n)
        elif len(self.large) > len(self.small) + 1:         # O(1) check
            val = heapq.heappop(self.large)                 # O(log n)
            heapq.heappush(self.small, -val)                # O(log n)

        # TOTAL for addNum: at most 2 pushes + 1 pop + 1 push -> O(log n) overall

    def findMedian(self):
        if len(self.small) == len(self.large):              # O(1)
            return (-self.small[0] + self.large[0]) / 2      # O(1): just peek both tops
        elif len(self.small) > len(self.large):              # O(1)
            return -self.small[0]                            # O(1): peek small's top
        else:
            return self.large[0]                             # O(1): peek large's top

        # TOTAL for findMedian: O(1)

# OVERALL (n = total numbers added so far):
# addNum:      O(log n) time  -> one or two heap pushes/pops, each log n
# findMedian:  O(1) time      -> just peeking the tops, no popping
# SPACE:       O(n) total     -> every number added lives in one of the two heaps