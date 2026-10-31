"""
Kth Largest Element In An Array - Medium

Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
Follow-up: Can you solve it without sorting?

Example 1:
Input: nums = [2,3,1,5,4], k = 2
Output: 4

Example 2:
Input: nums = [2,3,1,1,5,5,4], k = 3
Output: 4




# Kth Largest Element in an Array: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given an unsorted array of integers and a number k.
I need to return the kth largest number.
That means the number that would be at position k
if I sorted the array from biggest to smallest."

"I have a few quick questions before I start."

"Do duplicates count separately?
For example, in [5, 5, 4], is the 2nd largest 5?"
→ Yes, the problem says it's not the kth distinct element,
so each copy counts.

"Is k always between 1 and the length of the array?"
→ I'll assume yes.

"Can the numbers be negative?"
→ I'll assume yes.

"Is it okay to change the array, or should I leave it alone?"
→ I'll assume I should leave it alone, so I'll build a separate heap.

"The follow-up asks to do it without sorting.
Is that a hard requirement, or just a bonus?"
→ I'll treat it as something to aim for.

"Okay, so I need the number with exactly k - 1 numbers
ahead of it when everything is ordered from biggest to smallest."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
nums = [2, 3, 1, 5, 4], k = 2
```
"From biggest to smallest, it's 5, 4, 3, 2, 1.
The 2nd largest is 4. Answer: 4."

```
nums = [2, 3, 1, 1, 5, 5, 4], k = 3
```
"From biggest to smallest, it's 5, 5, 4, 3, 2, 1, 1.
The 3rd largest is 4, since both 5s count. Answer: 4."

"A few edge cases:"
- "k = 1: return the biggest number."
- "k = n: return the smallest number."
- "One element: return that element."
- "All the same, like [7, 7, 7] with k = 2: Answer: 7."
- "Negative numbers, like [-1, -5, -3] with k = 1: Answer: -1."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I sort the array from biggest to smallest,
and return the number at index k - 1."

"This works because after sorting,
the kth largest is sitting right at position k - 1."

"The time is O(n log n), because of the sort."

"The space is O(n) if I make a sorted copy,
or O(1) extra if I sort in place."

"The problem is that I'm putting every number in perfect order,
when I only need the top k.
Also, the follow-up asks me to solve it without sorting."

## 4. Optimal solution

"The bottleneck is sorting everything, when I only need the k biggest."

"Instead of sorting the whole array,
I can put every number into a max-heap,
and pop the biggest one k times.
The kth pop is my answer."

"The data structure I'll use is a max-heap,
because it gives me the biggest remaining number every time I pop,
without sorting the rest."

"Python's heapq only gives me a min-heap.
So I'll store every number as a negative.
The smallest negative is the biggest number,
so it sits at the top."

"As I go through the array, I add each number as a negative to a list."

"Then I heapify the whole list at once.
That builds the heap from the bottom up in O(n),
which is faster than pushing one number at a time."

"When I pop k times, the last number I pop is the kth largest."

"At the end, I flip the sign back and return it."

"The time is O(n + k log n).
Building the list is O(n), heapify is O(n),
and each of the k pops is O(log n)."

"The space is O(n), because the heap holds every number."

"So I go from O(n log n) down to O(n + k log n),
and I don't sort, which answers the follow-up."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll import heapq.
In Python, it gives me a min-heap on a regular list."

"Then I'll make a class called Solution,
and a function called KthLargest that takes self, nums, and k."

"I'll start with an empty list called heap."

"Then I loop over each num in nums,
and append -num to the list.
I'm making each number negative,
because heapq is a min-heap and I want the biggest number on top.
This also builds a new list, so I don't change the input."

"After the loop, I call heapq.heapify on the list.
That turns it into a valid heap in O(n),
with the biggest number, stored as the smallest negative, at the top."

"Then I loop k times."

"Each time, I pop from the heap and store it in ans.
Each pop removes the biggest number that's left,
and the heap fixes itself in O(log n)."

"After k pops, ans holds the kth biggest number, but it's still negative."

"So I return -ans, which flips it back to the real value."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[2, 3, 1, 5, 4], k = 2: the heap holds -5, -4, -3, -2, -1.
  The first pop gives -5. The second pop gives -4.
  I return 4. That matches."
- "[2, 3, 1, 1, 5, 5, 4], k = 3: the pops give -5, -5, then -4.
  I return 4, since both 5s count. That matches."
- "k = 1: one pop gives the biggest number."
- "k = n: I pop everything, and the last one is the smallest."
- "One element: one pop, and I return it."
- "[7, 7, 7], k = 2: the second pop is still -7, so I return 7."
- "[-1, -5, -3], k = 1: the heap holds 1, 5, 3.
  The smallest is 1, so the first pop gives 1, and I return -1. That matches."

"The output matches what I expected for all of them."

"To recap, time is O(n + k log n) and space is O(n)."

"If memory matters, I'd keep a min-heap of size k instead.
I push every number, and pop the smallest whenever the heap goes over k.
At the end, the top is the kth largest.
That's O(n log k) time and only O(k) space."

"And if they want the best average time, I'd use Quickselect.
It partitions the array around a pivot, like quicksort,
but only goes into the side that has the answer.
That's O(n) on average, but O(n²) in the worst case."
"""
import heapq
class Solution:
    def KthLargest(self, nums, k):
        heap = []
        for num in nums:
            heap.append(-num)
        heapq.heapify(heap)
        for i in range(k):
            ans = heapq.heappop(heap)
        return -ans

            
        
