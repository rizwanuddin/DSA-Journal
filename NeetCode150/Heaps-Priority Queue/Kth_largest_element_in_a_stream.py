"""
Kth Largest Element In a Stream - Easy

Design a class to find the kth largest integer in a stream of values, including duplicates. 
E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
Implement the following methods:
constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

Example 1:
Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
Output:
[null, 3, 3, 3, 5, 6]
Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   // return 3
kthLargest.add(5);   // return 3
kthLargest.add(6);   // return 3
kthLargest.add(7);   // return 5
kthLargest.add(8);   // return 6




# Kth Largest Element in a Stream: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I need to design a class.
It starts with a number k and a list of numbers.
Then numbers keep coming in one at a time through add.
Every time a number is added,
I return the kth largest number out of everything I've seen so far."

"I have a few quick questions before I start."

"Do duplicates count separately?
For example, in [1, 2, 3, 3], is the 2nd largest 3?"
→ Yes, the problem says so, so each copy counts.

"Can the starting list have fewer than k numbers?"
→ I'll assume it can have k - 1,
but by the time add returns, there are always at least k numbers.

"Can the starting list be empty?"
→ I'll assume yes, if k is 1.

"Can the numbers be negative?"
→ I'll assume yes.

"Can I use Python's heapq library?"
→ I'll assume yes, since I'm not being asked to build the heap myself.

"Okay, so after every add, I need the number that would be
at position k if I sorted everything from biggest to smallest."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
k = 3, nums = [1, 2, 3, 3]
add(3) → 3
add(5) → 3
add(6) → 3
add(7) → 5
add(8) → 6
```

"After add(3), the numbers from biggest to smallest are 3, 3, 3, 2, 1.
The 3rd largest is 3."

"After add(7), they're 7, 6, 5, 3, 3, 3, 2, 1.
The 3rd largest is 5."

"A few edge cases:"
- "k = 1: I always return the biggest number so far."
- "nums starts with k - 1 numbers: the first add fills it up to k."
- "A new number smaller than the current answer:
  it can't change the kth largest, so the answer stays the same."
- "Negative numbers: they're compared the same way."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I keep every number in a list.
Every time add is called, I append the new number,
sort the whole list from biggest to smallest,
and return the number at index k - 1."

"This works because after sorting,
the kth largest is sitting right at position k - 1."

"The time is O(n log n) for every add,
where n is how many numbers I've seen so far.
And n keeps growing, so every add gets slower."

"The space is O(n), because I keep every number."

"The problem is that I'm sorting everything, every time.
But I only care about the top k numbers.
Anything smaller than those can never be the answer again."

## 4. Optimal solution

"The bottleneck is sorting all the numbers on every add,
when only the top k matter."

"Instead of keeping and sorting every number,
I can keep only the k largest numbers I've seen."

"Out of those k numbers, the answer is the smallest one.
That's exactly the kth largest overall."

"The data structure I'll use is a min-heap of size k,
because it keeps the smallest of my top k right at the top,
where I can read it in O(1).
And adding or removing a number only costs O(log k)."

"In the constructor, I start with an empty heap,
and just call add on every starting number.
That way I reuse the same logic, and the heap never grows past k + 1."

"As I add each number, I push it into the heap."

"When the heap gets bigger than k, I pop the smallest number.
That keeps only the k largest."

"At the end of each add, I return the top of the heap,
which is the kth largest."

"The time for add is O(log k),
because the heap never holds more than k + 1 numbers."

"The constructor is O(n log k),
because it calls add once for each of the n starting numbers."

"The space is O(k), because I only keep k numbers."

"So each add goes from O(n log n) down to O(log k)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll import heapq.
In Python, heapq turns a regular list into a min-heap."

"Then I'll make a class called Solution."

"In the constructor, which takes k and nums,
I start with an empty list called self.heap.
This will be my min-heap of the k largest numbers."

"Then I save k in self.k, because add needs it."

"Then I loop over each num in nums,
and call self.add on it.
I'm reusing add here, so the constructor follows the exact same rules,
and the heap never grows past k + 1.
I just ignore what add returns while I'm setting things up."

"Now the add function, which takes val."

"First, I push val into the heap with heappush.
That keeps it a valid min-heap."

"Then I check if the heap has more than k numbers.
If it does, I pop the smallest one with heappop.
That number is too small to ever be the kth largest,
so I don't need it anymore."

"If the heap has k or fewer numbers, I don't pop anything.
That handles the case where the starting list was short."

"Finally, I return self.heap[0].
That's the smallest number in my top k, which is the kth largest."

## 7. Testing

"Before I finish, I'll trace through my test case."

- "The constructor gets k = 3 and [1, 2, 3, 3].
  add(1): the heap holds 1.
  add(2): the heap holds 1, 2.
  add(3): the heap holds 1, 2, 3.
  add(3): the heap holds 1, 2, 3, 3. That's 4, so I pop 1.
  The heap holds 2, 3, 3."
- "add(3): I push 3, and the heap has 4. I pop 2.
  The heap holds 3, 3, 3. I return 3."
- "add(5): I push 5, then pop a 3. The heap holds 3, 3, 5. I return 3."
- "add(6): I push 6, then pop a 3. The heap holds 3, 5, 6. I return 3."
- "add(7): I push 7, then pop 3. The heap holds 5, 6, 7. I return 5."
- "add(8): I push 8, then pop 5. The heap holds 6, 7, 8. I return 6."
- "So the outputs are 3, 3, 3, 5, 6, which matches."
- "k = 1: the heap only keeps the biggest number, so I return it."
- "Starting with k - 1 numbers: the first add makes the heap size k,
  so nothing gets popped, and I return the top."
- "A number smaller than the current answer:
  it's pushed and then popped right away, so the answer stays the same."

"The output matches what I expected for all of them."

"To recap, add is O(log k), the constructor is O(n log k),
and space is O(k)."
"""
import heapq
class Solution:
    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

        

