"""
K-th Largest element in an array

Given an array nums, return the kth largest element in the array.

Example 1:
Input: nums = [1, 2, 3, 4, 5], k = 2
Output: 4

Example 2:
Input: nums = [-5, 4, 1, 2, -3], k = 5
Output: -5





# Kth Largest Element in an Array: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given an unsorted array of numbers and a number k.
I need to return the kth largest number.
That's the number at position k if I sorted the array from biggest to smallest."

"I have a few quick questions before I start."

"Do duplicates count separately?
For example, in [5, 5, 4], is the 2nd largest 5?"
→ I'll assume yes, each copy counts.

"Is k always between 1 and the length of the array?"
→ I'll assume yes.

"Can the numbers be negative?"
→ I'll assume yes.

"Am I allowed to change the input array?"
→ I'll ask this one out loud.
If not, I'll work on a copy, or use the version that builds its own heap.

"Do I have to avoid sorting?"
→ I'll assume it's a bonus, not a rule.

"Okay, so I need the number with exactly k - 1 numbers ahead of it."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
nums = [3, 2, 1, 5, 6, 4], k = 2
```
"From biggest to smallest: 6, 5, 4, 3, 2, 1.
The 2nd largest is 5. Answer: 5."

```
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
```
"From biggest to smallest: 6, 5, 5, 4, 3, 3, 2, 2, 1.
The 4th largest is 4, since both 5s count. Answer: 4."

"A few edge cases:"
- "k = 1: the biggest number."
- "k = n: the smallest number."
- "One element: return it."
- "All the same, like [5, 5] with k = 2: Answer: 5."
- "Negatives, like [-1, -5, -3] with k = 2: Answer: -3."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

Data structure: array

"My first idea is the simplest one.
I sort the array from biggest to smallest,
and return the number at index k - 1."

"This works because after sorting,
the kth largest is sitting right at position k - 1."

- **Time: O(n log n).** "That's the cost of sorting every number."
- **Space: O(1) or O(n).** "O(1) if I sort in place, O(n) if I sort a copy."
- "The problem is that I put every number in perfect order,
  when I only need one of them."

## 4. Optimal solution

"The bottleneck is sorting everything, when I only need the kth number."

### Approach 1: heap of everything, pop k times

Data structure: max-heap (negatives in a min-heap)

"Instead of sorting everything, I can put all the numbers in a heap,
and pop the biggest one k times.
The kth pop is my answer."

"The data structure I will use is a max-heap,
because it gives me the biggest number left every time I pop."

"Python only has a min-heap.
So I'll store every number as a negative,
and the biggest number becomes the smallest negative, right at the top."

"As I go through the array, I add each number as a negative to a new list.
Then I heapify the whole list at once."

"When I pop k times, the last pop is the kth largest.
At the end, I flip the sign back and return it."

- **Time: O(n + k log n).**
  - "Building the list is O(n)."
  - "Heapify is O(n), because most numbers are near the bottom and barely move."
  - "Each of the k pops costs log n, because the heap fixes itself on the way down."
- **Space: O(n).** "The new list holds every number as a negative."
- "It doesn't change the input array."

### Approach 2: build the heap inside the array, no extra memory

Data structure: max-heap inside the array

"Instead of making a new list, I can turn the array itself into a max-heap."

"As I go, I first build the max-heap.
I start at index n // 2 - 1, the last number with a child,
and go backward to 0, pushing each one down into place."

"When the heap is built, I repeat k - 1 times.
I swap the top, the biggest number, with the last number of the heap.
Then I shrink the heap by one, so the number I just moved is out of reach.
Then I push the new top down to fix the heap."

"After k - 1 rounds, I've moved the k - 1 biggest numbers out of the way.
So the top of the heap is the kth largest, and I return nums[0]."

- **Time: O(n + k log n).**
  - "Building the heap is O(n)."
  - "Each of the k - 1 rounds costs log n, to push one number down."
- **Space: O(1).**
  - "Everything happens inside the same array."
  - "My push-down is a loop, not recursion, so there's no stack either."
- "The catch is that it changes the order of the input array."

"Out of these two, Approach 2 is better on memory,
and Approach 1 is safer because it leaves the input alone."

"If the interviewer wants better, there are two more options.
A min-heap of size k is O(n log k) time and O(k) space.
Quickselect is O(n) on average, but O(n²) in the worst case."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?
And is it okay if I change the input array?"

## 6. Code while talking out loud

### Approach 1

"First, I'll import heapq."

"Then I'll make a class called Solution,
and a function called Kth_largest that takes self, nums, and k."

"I'll start with an empty list called heap."

"And I'll set ans to 0.
It'll hold the last number I pop."

"Then I loop over each num in nums,
and append -num to heap.
I'm making them negative because heapq is a min-heap,
and I want the biggest number on top.
This builds a new list, so the input stays the same."

"Then I call heapq.heapify on heap.
That turns the whole list into a heap in O(n)."

"Next, I loop k times."

"Each time, I pop from the heap, flip the sign back,
and store it in ans.
Each pop gives me the biggest number that's left."

"After k pops, ans holds the kth largest, and I return it."

### Approach 2

"First, I'll make a class called Solution,
and a function called kthLargestElement that takes self, nums, and k."

"Inside it, I'll write a helper called heapify
that takes i, nums, and size.
It pushes the number at index i down until it's in place.
I pass size, so later I can shrink the heap
without touching the numbers I've moved out."

"In heapify, I start a while True loop, and I'll break when the number is in place."

"I compute left as 2 * i + 1, and right as 2 * i + 2.
Those are the children of i."

"I set largest to i.
I'm assuming the current number is the biggest until I find a bigger child."

"Then I check if left is less than size, so it's inside the heap,
and nums[largest] is less than nums[left].
If so, largest becomes left.
I check size first, not the full length,
so I never look at the numbers I moved out."

"Then I do the same check for right.
So largest ends up as the biggest of the three."

"If largest is still i, the number is in place, so I break."

"Otherwise, I swap nums[i] with nums[largest],
and set i to largest, to keep pushing it down."

"Back in the main function, I store the length of nums in n."

"Then I set start to n // 2 - 1.
That's the last number that has a child.
Everything after it is a leaf, so I skip those."

"I loop while start is 0 or more.
Each time, I call heapify on start with size n,
then subtract 1 from start.
I go backward, so a number's children are fixed before the number itself."

"Now the array is a max-heap, with the biggest number at index 0."

"Next, I set end to n - 1, the last index of the heap.
And I set rounds to 0, to count how many biggest numbers I've moved out."

"I loop while rounds is less than k - 1.
I only need to remove k - 1 numbers, so the kth biggest ends up on top."

"Each round, I swap nums[0] with nums[end].
The biggest number goes to the end, out of the heap."

"Then I call heapify on index 0 with size end.
Using end as the size means the heap stops right before the moved numbers."

"Then I subtract 1 from end, and add 1 to rounds."

"When the loop ends, the top of the heap is the kth largest,
so I return nums[0]."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[3, 2, 1, 5, 6, 4], k = 2, Approach 1:
  the heap holds -6, -5, -4, -3, -2, -1.
  The first pop is -6. The second pop is -5.
  I return 5. That matches."
- "Same input, Approach 2:
  building the max-heap gives [6, 5, 4, 3, 2, 1].
  There's k - 1 = 1 round.
  I swap 6 with the last number, and fix the heap.
  The top is now 5. I return 5. That matches."
- "[3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4:
  the 3 biggest numbers, 6, 5, and 5, come out first,
  so the 4th is 4. Both approaches return 4. That matches."
- "k = 1: Approach 1 does one pop. Approach 2 does zero rounds,
  and returns nums[0], the biggest."
- "k = n: Approach 2 does n - 1 rounds, and the last number left on top
  is the smallest. When end is 1, heapify gets size 1, so it does nothing."
- "One element: no rounds, and I return it."
- "[5, 5], k = 2: with strict less-than, equal numbers don't swap.
  I return 5."
- "[-1, -5, -3], k = 2: negatives work the same way. I return -3."

"The output matches what I expected for all of them."

"To recap, both approaches are O(n + k log n) time.
Approach 1 uses O(n) space, and Approach 2 uses O(1) but changes the array."

"Also, Approach 2 pops the k - 1 biggest numbers, not k,
so it saves one round compared to popping k times."
"""
# approach 1
import heapq
class Solution:
    def Kth_largest(self, nums, k):
        heap = []
        ans = 0
        for num in nums:
            heap.append(-num)
        heapq.heapify(heap)
        for _ in range(k):
            ans = -heapq.heappop(heap)
        return ans


# approach 2
class Solution:
    def kthLargestElement(self, nums, k):
        def heapify(i, nums, size):
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                if left < size and nums[largest] < nums[left]:
                    largest = left
                if right < size and nums[largest] < nums[right]:
                    largest = right
                if largest == i:
                    break
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        n = len(nums)

        start = n // 2 - 1
        while start >= 0:
            heapify(start, nums, n)
            start -= 1

        end = n - 1
        rounds = 0
        while rounds < k - 1:
            nums[0], nums[end] = nums[end], nums[0]
            heapify(0, nums, end)
            end -= 1
            rounds += 1

        return nums[0]
    ## just so you now neither are optimal....QuickSelect method is the optimal one with O(n)