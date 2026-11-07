"""
Heap Sort - Hard

Given an array of integers nums, sort the array in non-decreasing order using the heap sort algorithm. Sort the given array itself, 
there is no need to return anything.
A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.

Example 1:
Input: nums = [7, 4, 1, 5, 3]
Output: [1, 3, 4, 5, 7]
Explanation:1 <= 3 <= 4 <= 5 <= 7.
One possible way to get the sorted array using heapSort :

[7, 4, 1, 5, 3] -> [3, 4, 1, 5, 7]

-> [5, 4, 1, 3, 7] -> [3, 4, 1, 5, 7]

-> [4, 3, 1, 5, 7] -> [1, 3, 4, 5, 7]

-> [3, 1, 4, 5, 7] -> [1, 3, 4, 5, 7]

-> [1, 3, 4, 5, 7] -> [1, 3, 4, 5, 7]

Example 2:
Input: nums = [5, 4, 4, 1, 1]
Output: [1, 1, 4, 4, 5]
Explanation: 1 <= 1 <= 4 <= 4 <= 5.
Thus the array is sorted in non-decreasing order.




# Heap Sort: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given an array of numbers.
I need to sort it from smallest to biggest, using heap sort."

"I have a few quick questions before I start."

"Should the order be ascending, smallest to biggest?"
→ I'll assume ascending.

"Should I sort the array in place, or return a new one?"
→ I'll assume in place, and I'll also return it to be safe.

"Can the array be empty or have one element?"
→ I'll assume yes, and then there's nothing to do.

"Can there be duplicates or negative numbers?"
→ I'll assume yes. Comparing with greater-than works for both.

"Okay, so I want a sort that is always O(n log n),
and doesn't need extra memory."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
[4, 10, 3, 5, 1]  →  [1, 3, 4, 5, 10]
```

"A few edge cases:"
- "Empty array: nothing happens. Answer: []."
- "One element, like [7]: Answer: [7]."
- "Already sorted, like [1, 2, 3]: Answer: [1, 2, 3]."
- "Reverse sorted, like [3, 2, 1]: Answer: [1, 2, 3]."
- "Duplicates, like [2, 2, 1]: Answer: [1, 2, 2]."
- "Negatives, like [-1, -5, 3]: Answer: [-5, -1, 3]."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

Data structure: array

"My first idea is the simplest one, selection sort.
I scan the whole array to find the smallest number,
and swap it to the front.
Then I scan the rest to find the next smallest,
and swap it into position two, and so on."

"This works because after each round,
the front of the array holds the smallest numbers in order."

- **Time: O(n²).** "For each of the n spots, I scan the numbers that are left to find the smallest."
- **Space: O(1).** "I only swap inside the array, so I need no extra memory."
- "The problem is that I re-scan the same numbers again and again,
  just to find the smallest one."

"A middle idea is to put everything in a min-heap and pop one by one.
That's O(n log n), but it uses O(n) extra space for the heap and the new array."

## 4. Optimal solution

Data structure: max-heap, built inside the array

"The bottleneck is scanning to find the biggest or smallest every time."

"Instead of scanning every round,
I can turn the array itself into a max-heap.
Then the biggest number is always at index 0."

"The data structure I will use is a max-heap stored inside the same array,
because it gives me the biggest number right away,
and it needs no extra memory."

"As I go, first I build the max-heap.
I start at the last number that has a child, index n // 2 - 1,
and go backward to 0, pushing each one down into place.
I skip the leaves, because they have no children to fix."

"When the heap is built, I repeat these steps.
I swap the top, the biggest number, with the last number of the heap.
Now the biggest is in its final spot at the end.
Then I shrink the heap size by one, so I never touch the sorted part again.
Then I push the new top down to fix the heap."

"At the end, the whole array is sorted, and I return it."

- **Time: O(n log n).**
  - "Building the heap is only O(n), because most numbers are near the bottom and barely move."
  - "Then I do n - 1 rounds, and each round pushes one number down, which costs log n."
- **Space: O(1).**
  - "I sort inside the same array."
  - "My push-down uses a loop, not recursion, so there's no stack either."
- "So I go from O(n²) down to O(n log n), with no extra memory."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution,
and a function called heapSort that takes self and nums."

"Inside it, I'll write a helper called heapify,
which takes i, nums, and size.
It pushes the number at index i down until it's in the right place.
I pass size on purpose.
Later, the heap gets smaller, and I don't want to touch the sorted part."

"In heapify, I start a while True loop,
and I'll break when the number is in place."

"I compute left as 2 * i + 1, and right as 2 * i + 2.
Those are the two children of i."

"I set largest to i.
I'm assuming the current number is the biggest
until I find a bigger child."

"Then I check if left is less than size, so it's inside the heap,
and nums[largest] is less than nums[left].
If so, largest becomes left.
I check size first, not the full length,
so I never look at the sorted part."

"Then I do the same check for right.
So largest ends up as the biggest of the three."

"If largest is still i, the number is in place, so I break."

"Otherwise, I swap nums[i] with nums[largest],
and set i to largest, to keep pushing it down."

"Now back in heapSort, I store the length in n."

"Then I set start to n // 2 - 1.
That's the last number that has a child.
Everything after it is a leaf, so I skip those."

"Then I loop while start is 0 or more.
Each time, I call heapify on start with size n,
then subtract 1 from start.
I go backward, so a number's children are fixed before the number itself."

"When that loop ends, the whole array is a max-heap,
with the biggest number at index 0."

"Now I set end to n - 1, the last index."

"Then I loop while end is greater than 0."

"Each round, I swap nums[0] with nums[end].
The biggest number goes to the end, where it belongs."

"Then I call heapify on index 0 with size end.
Using end as the size means the heap stops right before the sorted part.
That's what keeps the sorted numbers safe."

"Then I subtract 1 from end, so the heap gets one smaller."

"When the loop ends, the array is sorted.
I return nums, in case the problem wants it back."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[4, 10, 3, 5, 1]:
  Build the heap. At index 1, the number 10 is already the biggest of its group.
  At index 0, 4 swaps with 10, then with 5. The heap is [10, 5, 3, 4, 1].
  Round 1: swap 10 to the end, and fix the heap. The array is [5, 4, 3, 1, 10].
  Round 2: swap 5 to the spot before it, and fix. The array is [4, 1, 3, 5, 10].
  Round 3: swap 4, and fix. The array is [3, 1, 4, 5, 10].
  Round 4: swap 3. The array is [1, 3, 4, 5, 10].
  That matches."
- "Empty array: start is -1 and end is -1, so neither loop runs."
- "One element: start is -1 and end is 0, so neither loop runs."
- "Already sorted [1, 2, 3]: the heap build makes 3 the top.
  Then the swaps move everything into place. The result is [1, 2, 3]."
- "Reverse sorted [3, 2, 1]: it's already a max-heap.
  The rounds swap 3 to the end, then 2. The result is [1, 2, 3]."
- "Duplicates [2, 2, 1]: I use strict greater-than,
  so equal numbers don't swap for no reason. The result is [1, 2, 2]."

"The output matches what I expected for all of them."

"To recap, time is O(n log n) and space is O(1)."

"One thing to mention is that heap sort isn't stable,
so equal numbers can end up in a different order.
If that matters, I'd use merge sort, which is O(n log n) but needs O(n) extra space."
"""
class Solution:
    def heapSort(self, nums):
        def heapify(i, nums, size):                        # added size
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                if left < size and nums[largest] < nums[left]:     # size, not n
                    largest = left
                if right < size and nums[largest] < nums[right]:   # size, not n
                    largest = right
                if largest == i:
                    break
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        n = len(nums)

        start = n // 2 - 1
        while start >= 0:
            heapify(start, nums, n)                        # whole array
            start -= 1

        end = n - 1
        while end > 0:
            nums[0], nums[end] = nums[end], nums[0]
            heapify(0, nums, end)
            end -= 1
        return nums