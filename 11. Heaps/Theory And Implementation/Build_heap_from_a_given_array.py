"""
Build heap from a given Array - Medium

Given an array of integers nums, convert it in-place into a min-heap.

A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is 
recursively true for all nodes in a Binary Tree.

Since multiple valid min-heaps can be formed from the same input array, the output may not be unique.
Therefore, the platform will validate the returned array and print:
True if the returned array is a valid min-heap.
False if the returned array is not a valid min-heap.

Example 1:
Input: nums = [6, 5, 2, 7, 1, 7]
Output: [1, 5, 2, 7, 6, 7]
Explanation: nums[0] <= nums[1], nums[2]
nums[1] <= nums[3], nums[4]
nums[2] <= nums[5]

Example 2:
Input: nums = [2, 3, 4, 1, 7, 3, 9, 4, 6]
Output: [1, 2, 3, 3, 7, 4, 9, 4, 6]
Explanation: nums[0] <= nums[1], nums[2]
nums[1] <= nums[3], nums[4]
nums[2] <= nums[5], nums[6]
nums[3] <= nums[7], nums[8]



# Build a Min-Heap from an Array: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given an array of numbers in any order.
I need to rearrange it so it becomes a valid min-heap.
That means every parent is smaller than or equal to its children."

"I have a few quick questions before I start."

"Is it a min-heap, not a max-heap?"
→ I'll assume min-heap.

"Is the heap stored as an array, where the children of index i
are at 2i + 1 and 2i + 2?"
→ I'll assume yes.

"Should I change the array in place?"
→ I'll assume yes, and I won't return anything.

"Can there be duplicates or negative numbers?"
→ I'll assume yes. Neither one breaks the heap rules.

"Can the array be empty?"
→ I'll assume it can, and then there's nothing to do.

"Okay, so I just need to move values around
until every parent is smaller than its children."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
nums = [9, 5, 6, 2, 3]

        9
      /   \
     5     6
    / \
   2   3
```
"After building the heap, one valid answer is [2, 3, 6, 5, 9].

        2
      /   \
     3     6
    / \
   5   9

Every parent is smaller than its children."

"A few edge cases:"
- "Empty array: nothing changes."
- "One element: it's already a heap."
- "Already sorted, like [1, 2, 3, 4]: it's already a valid min-heap,
  so nothing moves."
- "Reverse sorted, like [5, 4, 3, 2, 1]: lots of swaps,
  but it should still end up valid."
- "All the same value: nothing moves."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I build the heap one element at a time, like inserting into a heap."

"I start with just the first element, which is a heap on its own.
Then I add the next element at the end,
and move it up, swapping with its parent while it's smaller.
I repeat this for every element."

"This works because after each insert, the heap is valid again,
so by the end, the whole array is a valid heap."

"The time is O(n log n).
There are n inserts,
and each one can move up the whole height of the heap, which is log n."

"The space is O(1) extra, since I do it in place."

"Another simple option is to just sort the array,
because a sorted array is always a valid min-heap.
That's also O(n log n)."

"The problem is that a lot of elements end up moving
a long way up the tree.
I can do better by fixing the heap from the bottom up instead."

## 4. Optimal solution

"The bottleneck is that inserting one by one makes many elements
travel a long way up."

"Instead of inserting elements one at a time,
I can fix the heap from the bottom up,
by moving values down instead of up."

"The key thing is that leaves are already valid heaps.
A leaf has no children, so there's nothing to break."

"In an array of size n, the last non-leaf node is at index n // 2 - 1.
Everything after that is a leaf."

"So I start at n // 2 - 1, and go backward to index 0.
At each node, I sift its value down,
swapping with the smaller child until both children are bigger."

"By the time I fix a node, both of its subtrees are already valid heaps,
because I worked bottom up.
So sifting down one value is enough to make that whole subtree valid."

"The data structure is just the array itself,
because a heap stored in an array lets me jump to any child with simple math."

"As I go from the last non-leaf node back to the root,
I sift each value down into place."

"When a node is smaller than both children, I stop for that node."

"At the end, the whole array is a valid min-heap."

"The time is O(n).
That's surprising at first, but here's the reason in simple words.
Half the nodes are leaves, and they don't move at all.
A quarter of them can move down only 1 level.
An eighth can move down 2 levels, and so on.
Only the root can move all the way down.
When I add all of that up, it comes out to about n."

"The space is O(1), because I only use a few index variables."

"So I go from O(n log n) down to O(n)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called buildHeap that takes self and nums."

"Inside it, I'll define a helper called heapify that takes nums and ind.
It sifts the value at ind down until it's in the right place."

"I store the length of the array in n.
I need it to check if a child index is inside the array."

"I set i to ind.
That's the current position of the value I'm moving."

"Then I start a while True loop.
I'll break out once the value is in the right place."

"Inside it, I compute left as 2 * i + 1, and right as 2 * i + 2.
Those are the two children of i."

"I set smallest to i.
I'm assuming the current value is the smallest
until I find a smaller child."

"Then I check if left is inside the array,
and nums[left] is smaller than nums[smallest].
If so, smallest becomes left.
I check the bounds first, so I never index outside the array."

"Then I do the same check for right.
If it's smaller, smallest becomes right.
Doing them one after the other means smallest ends up as the smaller child."

"If smallest is still i, the value is already smaller than both children,
or there are no children. So I break."

"Otherwise, I swap nums[i] and nums[smallest].
Now the smallest of the three is on top."

"Then I set i to smallest, and keep checking from the new position."

"Now back in buildHeap, I store the length of nums in n."

"Then I set start to n // 2 - 1.
That's the last node that has at least one child.
Everything after it is a leaf, so I can skip those."

"I start a while loop that runs while start is 0 or more."

"Inside it, I call
"""
class Solution:
    def buildHeap(self, nums):
        def heapify(nums, ind):
            n = len(nums)
            i = ind
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i
                if left < n and nums[left] < nums[smallest]:
                    smallest = left
                if right < n and nums[right] < nums[smallest]:
                    smallest = right
                if smallest == i:
                    break
                nums[i], nums[smallest] = nums[smallest], nums[i]
                i = smallest
        
        n = len(nums)
        start = n // 2 - 1 
        while start >= 0:
            heapify(nums, start)
            start -= 1
        
