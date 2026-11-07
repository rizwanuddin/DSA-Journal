"""
Sort a K-Sorted Array 

You are given an integer array arr and an integer k.
The array is k-sorted, meaning every element is at most k positions away from its correct position in the completely sorted array.
Sort the array in non-decreasing order and return the sorted array.
Your solution should take advantage of the k-sorted property rather than simply sorting the entire array.

Example 1:
Input: arr = [3, 1, 2, 5, 4, 7, 6], k = 2
Output: [1, 2, 3, 4, 5, 6, 7]
Explanation: Every element is at most 2 positions away from its position in the sorted array. After sorting, the array becomes [1, 2, 3, 4, 5, 6, 7].

Example 2:
Input: arr = [4, 2, 3, 1, 6, 5], k = 3
Output: [1, 2, 3, 4, 5, 6]
Explanation: The array satisfies the k = 3 condition. Sorting it gives [1, 2, 3, 4, 5, 6].





# Sort a K-Sorted Array: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given an array and a number k.
Every element is at most k positions away from its spot in the sorted array.
I need to return the array sorted in ascending order."

"I have a few quick questions before I start."

"Is the k-sorted guarantee always true?
I mean, can I trust it, or should I handle arrays that break it?"
→ I'll assume I can trust it.

"Should I return a new array, or sort in place?"
→ I'll assume a new array is fine.

"Can there be duplicates or negative numbers?"
→ I'll assume yes. Neither one changes the approach.

"Can k be 0, or bigger than the array?"
→ I'll assume yes to both, and I'll handle them.

"Can the array be empty?"
→ I'll assume yes, and then I return an empty list.

"Okay, so the array is almost sorted.
I should be able to do better than a full sort."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
arr = [3, 1, 2, 5, 4, 6], k = 2
```
"Sorted is [1, 2, 3, 4, 5, 6].
The 3 is 2 spots from where it belongs, and the 5 and 4 are 1 spot away.
That fits k = 2. Answer: [1, 2, 3, 4, 5, 6]."

"A few edge cases:"
- "Empty array: Answer: []."
- "One element: Answer: that element."
- "k = 0: it's already sorted, so nothing moves."
- "k is bigger than the array: the whole array is the window.
  It works like a plain sort."
- "Duplicates, like [2, 1, 2] with k = 1: Answer: [1, 2, 2]."
- "Negatives, like [-1, -3, -2] with k = 2: Answer: [-3, -2, -1]."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

Data structure: array

"My first idea is insertion sort.
I go left to right.
For each number, I slide it left past every bigger number,
until it lands in its right spot."

"This works because after each step,
everything to the left of my position is sorted."

"Normally, insertion sort is O(n²).
But here, every number is at most k spots from its final place.
So each number slides left at most k steps."

- **Time: O(n * k).**
  - "There are n numbers."
  - "Each one slides at most k steps, because of the k-sorted guarantee."
  - "Without the guarantee, it would be O(n²)."
- **Space: O(1).**
  - "I move numbers around inside the same array."
  - "I only need one variable to hold the number I'm sliding."
- "The problem is that when k is big, n * k gets slow.
  I'm also comparing a number against up to k others, one at a time,
  when I only need to know which one is the smallest."

## 4. Optimal solution

Data structure: min-heap

"The bottleneck is that I look at up to k numbers one by one
just to find the smallest."

"Here's what the guarantee tells me.
The smallest number in the whole array has to be
within the first k + 1 positions,
because it's at most k spots away from index 0."

"So instead of sliding numbers around,
I can keep a window of the next k + 1 numbers,
and always pull out the smallest one."

"The data structure I will use is a min-heap of size k + 1,
because it gives me the smallest number in the window right away,
and adding or removing one is only log k."

"As I go, first I push the first k + 1 numbers into the heap."

"When the heap is full, I pop the smallest.
That number is in its final spot, so I add it to the answer.
Then I push the next number from the array."

"When I run out of numbers, I pop everything left in the heap,
and add it to the answer, one by one."

"At the end, I return the answer."

- **Time: O(n log k).**
  - "Every number gets pushed once and popped once."
  - "The heap never holds more than k + 1 numbers, so each push or pop costs log k."
- **Space: O(k) extra.**
  - "The heap holds at most k + 1 numbers."
  - "The answer list is the output, so I don't count it."
- "So I go from O(n * k) down to O(n log k).
  The bigger k is, the more the heap helps.
  If k is tiny, like 1 or 2, insertion sort is already close to O(n)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll import heapq.
In Python, it gives me a min-heap on a regular list."

"Then I'll make a class called Solution,
and a function called SortKsorted that takes self, arr, and k."

"I'll start with an empty list called heap.
This is my window of k + 1 numbers."

"And an empty list called ans.
This is the sorted output."

"I'll store the length of arr in n."

"Then I set i to 0.
i is my position in the array, and I'll reuse it across all three loops."

"The first loop fills the window.
It runs while i is less than n, and i is less than k + 1.
I check both, because the array might be shorter than k + 1."

"Inside it, I push arr[i] into the heap,
and add 1 to i."

"That's k + 1 pushes, and each one costs log k."

"The second loop handles the rest of the array.
It runs while i is less than n."

"Inside it, I pop the smallest number from the heap,
and store it in smallest."

"I can safely add smallest to the answer.
The number that belongs in this spot is already in the window,
because it's at most k spots away.
And arr[i] is too far away to belong here."

"So I append smallest to ans."

"Then I push arr[i] into the heap,
and add 1 to i.
The window slides forward by one."

"The heap stays at k + 1 numbers, so each pop and push costs log k."

"The third loop empties the heap.
It runs while the heap isn't empty."

"Each time, I pop the smallest, and append it to ans.
There are no more numbers to add,
so the last k + 1 numbers come out in sorted order."

"Finally, I return ans."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[3, 1, 2, 5, 4, 6], k = 2:
  First loop: I push 3, 1, 2. The heap holds 1, 2, 3.
  Second loop: i = 3. I pop 1, so ans is [1]. I push 5. The heap holds 2, 3, 5.
  i = 4. I pop 2, so ans is [1, 2]. I push 4. The heap holds 3, 4, 5.
  i = 5. I pop 3, so ans is [1, 2, 3]. I push 6. The heap holds 4, 5, 6.
  Third loop: I pop 4, 5, 6.
  The answer is [1, 2, 3, 4, 5, 6], which matches."
- "Empty array: n is 0, so none of the loops run, and I return []."
- "One element: the first loop pushes it, and the third loop pops it."
- "k = 0: the window is 1 number.
  Each round, I pop one and push the next, so the array stays in order."
- "k bigger than the array: the first loop pushes everything,
  the second loop never runs, and the third loop pops it all in sorted order."
- "Duplicates [2, 1, 2], k = 1: the heap holds 1, 2.
  I pop 1, and push 2. Then I pop 2, then 2. The answer is [1, 2, 2]."
- "Negatives: the heap compares them the same way."

"The output matches what I expected for all of them."

"To recap, time is O(n log k) and extra space is O(k)."

"If I wanted to sort in place, I could write the output back into arr.
That would still be O(k) extra space for the heap."
"""

import heapq

class Solution:
    def SortKsorted(self, arr, k):
        heap = []                 # at most k + 1 items -> O(k) space
        ans = []                  # n items -> O(n) space
        n = len(arr)

        i = 0
        while i < n and i < k + 1:            # k + 1 pushes
            heapq.heappush(heap, arr[i])      # O(log k) each
            i += 1                            # phase total: O(k log k)

        while i < n:                          # n - (k + 1) rounds
            smallest = heapq.heappop(heap)    # O(log k), heap size is k + 1
            ans.append(smallest)              # O(1)
            heapq.heappush(heap, arr[i])      # O(log k)
            i += 1                            # phase total: O((n - k) log k)

        while heap:                           # k + 1 leftovers
            smallest = heapq.heappop(heap)    # O(log k) each
            ans.append(smallest)              # phase total: O(k log k)

        return ans                            # overall: O(n log k) time

            

