"""
Convert Min Heap to Max Heap - Medium

Given a min-heap in array representation named nums, convert it into a max-heap and return the resulting array.

A min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and 
the same property is recursively true for all nodes in the Binary Tree. A max-heap is a complete binary tree where the key at 
the root is the maximum among all keys present in a binary max-heap and the same property is recursively true for all nodes in 
the Binary Tree. Since there can be multiple answers, the compiler will return true if it's correct, else false.

Example 1:
Input: nums = [10, 20, 30, 21, 23]
Output: [30, 21, 23, 10, 20]
Explanation:
In the input min heap, 10 is the root (largest).
After conversion, 30 becomes the root (largest).
Now every parent node is larger than its children:
30 > 21, 30 > 23
21 > 10, 23 > 20
Hence it is a valid max heap.

Example 2:
Input: nums = [-5, -4, -3, -2, -1]
Output: [-1, -2, -3, -4, -5]
Explanation:
In the input min heap, -5 is the root (largest among negatives).
After conversion, -1 becomes the root (largest among negatives).
Now every parent node is larger than its children:
-1 > -2, -1 > -3
-2 > -4, -3 > -5
Hence it is a valid max heap.




# Build a Max-Heap from an Array: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given an array of numbers.
I need to rearrange it so it becomes a valid max-heap,
and return it.
That means every parent is bigger than or equal to its children,
so the biggest value ends up at the top."

"I have a few quick questions before I start."

"Is the input already a min-heap, or can it be in any order?"
→ I'll assume it can be in any order.
If it's a min-heap, that doesn't help me, so I'll treat it like any array.

"Is the heap stored as an array, where the children of index i
are at 2i + 1 and 2i + 2?"
→ I'll assume yes.

"Can I change the array in place, and return it?"
→ I'll assume yes.

"If there are several valid max-heaps, can I return any of them?"
→ I'll assume yes.

"Can there be duplicates, negatives, or an empty array?"
→ I'll assume yes to all three.

"Okay, so I just need to move values around
until every parent is bigger than its children."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
nums = [1, 3, 5, 7, 9, 8]

        1
      /   \
     3     5
    / \   /
   7   9 8
```
"This is a min-heap right now.
After building the max-heap, one valid answer is [9, 7, 8, 1, 3, 5].

        9
      /   \
     7     8
    / \   /
   1   3 5

Every parent is bigger than its children."

"A few edge cases:"
- "Empty array: return []."
- "One element: it's already a max-heap."
- "Sorted from biggest to smallest, like [5, 4, 3, 2, 1]:
  it's already a valid max-heap, so nothing moves."
- "Sorted from smallest to biggest, like [1, 2, 3, 4, 5]:
  lots of swaps, but it still ends up valid."
- "All the same value: nothing moves."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I build the heap one element at a time, like inserting into a heap."

"I start with just the first element.
Then I add each next element at the end,
and move it up, swapping with its parent while it's bigger."

"This works because after each insert, the heap is valid again,
so by the end, the whole array is a valid max-heap."

"The time is O(n log n).
There are n inserts,
and each one can move all the way up the heap, which is log n levels."

"The space is O(1) extra, since I do it in place."

"Another simple option is to sort the array from biggest to smallest.
A sorted array like that is always a valid max-heap.
That's also O(n log n)."

"The problem is that a lot of elements travel a long way up the tree.
I can do less work by fixing the heap from the bottom up instead."

## 4. Optimal solution

"The bottleneck is that inserting one at a time
makes many elements move a long way up."

"Instead of inserting elements one by one,
I can fix the heap from the bottom up, by moving values down."

"The key thing is that leaves are already valid heaps.
They have no children, so there's nothing to fix."

"The last node that has a child is at index n // 2 - 1.
Everything after that is a leaf."

"So I start at n // 2 - 1, and go backward to index 0.
At each node, I sift its value down,
swapping with the bigger child until both children are smaller."

"I swap with the bigger child, not just any child.
That way, the value that moves up is the biggest of the three,
so the parent stays bigger than both children."

"By the time I reach a node, both of its subtrees are already valid,
because I'm working from the bottom up.
So sifting down that one value fixes its whole subtree."

"The data structure is just the array itself,
because I can jump to any child with simple index math."

"As I go from the last parent back to the root,
I sift each value down into place."

"When a node is bigger than both children, I stop for that node."

"At the end, I return the array."

"The time is O(n).
Half the nodes are leaves, and they don't move at all.
A quarter can only move down 1 level.
An eighth can move down 2 levels, and so on.
Only the root can move all the way down.
When I add it all up, it comes out to about n."

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

"Then I start a while True loop,
and I'll break once the value is in the right place."

"Inside it, I compute left as 2 * i + 1, and right as 2 * i + 2.
Those are the two children of i."

"I set largest to i.
I'm assuming the current value is the biggest
until I find a bigger child."

"Then I check if left is inside the array,
and nums[left] is bigger than nums[largest].
If so, largest becomes left.
I check the bounds first, so I never index outside the array."

"Then I do the same check for right.
If it's bigger, largest becomes right.
Doing them one after the other means largest ends up as the bigger child."

"If largest is still i, the value is already bigger than both children,
or there are no children. So I break."

"Otherwise, I swap nums[i] and nums[largest].
Now the biggest of the three is on top."

"Then I set i to largest, and keep checking from the new position."

"Now back in buildHeap, I store the length of nums in n."

"Then I set start to n // 2 - 1.
That's the last node with at least one child.
Everything after it is a leaf, so I skip those."

"I start a while loop that runs while start is 0 or more."

"Inside it, I call heapify on start,
which sifts that value down into place."

"Then I subtract 1 from start, to move to the previous node."

"I go backward, so every node's children are fixed
before I fix the node itself."

"When the loop ends, every node down to the root is fixed,
so I return nums."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "First example: n is 6, so start is 2.
  At index 2, the value is 5, and its only child is 8.
  8 is bigger, so they swap. The array is [1, 3, 8, 7, 9, 5].
  Then start is 1. The value is 3, and its children are 7 and 9.
  9 is bigger, so they swap. The array is [1, 9, 8, 7, 3, 5].
  Then start is 0. The value is 1, and its children are 9 and 8.
  9 is bigger, so they swap. The array is [9, 1, 8, 7, 3, 5].
  Now 1 is at index 1, and its children are 7 and 3.
  7 is bigger, so they swap. The array is [9, 7, 8, 1, 3, 5].
  1 has no children now, so it stops.
  The result is [9, 7, 8, 1, 3, 5], which matches."
- "Empty array: start is -1, the loop never runs, and I return []."
- "One element: start is -1, the loop never runs."
- "Sorted biggest to smallest: every parent is already bigger,
  so every heapify call breaks right away."
- "Sorted smallest to biggest: values get swapped down level by level,
  and the result is still a valid max-heap."
- "All the same value: no child is ever strictly bigger, so nothing moves."

"The output matches what I expected for all of them."

"To recap, time is O(n) and space is O(1)."
"""
class Solution:
    def buildHeap(self, nums):          
        def heapify(nums, ind):
            n = len(nums)
            i = ind
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                if left < n and nums[left] > nums[largest]:
                    largest = left
                if right < n and nums[right] > nums[largest]:
                    largest = right
                if largest == i:
                    break
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        n = len(nums)
        start = n // 2 - 1
        while start >= 0:
            heapify(nums, start)
            start -= 1
        return nums                  