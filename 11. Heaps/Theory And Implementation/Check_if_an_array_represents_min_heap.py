"""
Check if an array represents a min heap

Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, 
otherwise return false.A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys 
present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.

Example 1:
Input: nums = [10, 20, 30, 21, 23]
Output: true
Explanation: Each node has a lower or equal value than its children.

Example 2:
Input: nums = [10, 20, 30, 25, 15]
Output: false
Explanation: The node with value 20 has a child with value 15, thus it is not a min-heap.



# Check if an Array Is a Min-Heap: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given an array of numbers.
I need to return True if it represents a valid min-heap,
and False if it doesn't."

"A valid min-heap means every parent is smaller than or equal to its children."

"I have a few quick questions before I start."

"Is the heap stored as an array, where the children of index i
are at 2i + 1 and 2i + 2?"
→ I'll assume yes.

"If a parent equals its child, is that still valid?"
→ I'll assume yes, since the rule is smaller than or equal.

"Can the array be empty?"
→ I'll assume yes, and an empty array counts as a valid heap.

"Can there be negative numbers or duplicates?"
→ I'll assume yes. Neither one changes the rule.

"Should I avoid changing the array?"
→ I'll assume yes, I'm only checking it.

"Okay, so I just need to make sure no child is ever smaller than its parent."

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
"Every parent is smaller than its children. Answer: True."

```
nums = [1, 3, 5, 2, 9]

        1
      /   \
     3     5
    / \
   2   9
```
"2 is a child of 3, and it's smaller. Answer: False."

"A few edge cases:"
- "Empty array: Answer: True."
- "One element: Answer: True."
- "All equal values, like [4, 4, 4]: equal is allowed. Answer: True."
- "A node with only a left child, like [1, 0]: 0 is smaller than 1.
  Answer: False."
- "A problem deep down at the bottom level: I still need to catch it."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
For every node, I walk through its whole subtree,
and make sure nothing below it is smaller."

"This works because it checks exactly what a min-heap promises:
every value is the smallest in its own subtree."

"The time is O(n log n).
The root checks all n nodes.
Each level below checks fewer nodes per subtree,
and there are log n levels, so it adds up to about n log n."

"The space is O(1) extra, if I walk the subtree with index math."

"The problem is that I'm comparing nodes that are far apart,
even though I don't need to.
The same comparisons get repeated for every ancestor."

## 4. Optimal solution

"The bottleneck is checking every node against its whole subtree."

"Instead of comparing every node with everything below it,
I can just compare each node with its direct children."

"That's enough, because the rule chains down.
If a parent is smaller than its child,
and that child is smaller than its own child,
then the parent is smaller than the grandchild too.
So if every parent-child pair is fine, the whole heap is fine."

"I also only need to check nodes that have children.
In an array of size n, those are indexes 0 to n // 2 - 1.
Everything after that is a leaf, and leaves have nothing to compare."

"The data structure is just the array itself,
because I can jump to any node's children with simple math."

"As I go through each parent from index 0 to n // 2 - 1,
I look at its left child and its right child."

"When a child exists and is smaller than the parent,
I return False right away."

"At the end, if no pair broke the rule, I return True."

"The time is O(n).
I visit about half the nodes, and each one does two comparisons."

"The space is O(1), because I only use a few index variables."

"So I go from O(n log n) down to O(n)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called isMinHeap that takes self and nums."

"I store the length of the array in n.
I need it to know where the parents end,
and to check if a child index is inside the array."

"Then I loop i from 0 up to n // 2.
That covers every index that has at least one child.
The rest are leaves, so I can skip them."

"Inside the loop, I compute left as 2 * i + 1,
and right as 2 * i + 2.
Those are the two children of i."

"I set smallest to i.
That's just the index of the parent I'm comparing against."

"Then I check if left is inside the array,
and nums[left] is smaller than nums[smallest].
If both are true, the left child is smaller than its parent,
so the heap is broken, and I return False right away.
I check the bounds first, so I never index outside the array."

"Then I do the same check for right.
If the right child exists and is smaller than the parent,
I return False."

"The last parent might only have a left child,
and the bounds check on right handles that safely."

"If the loop finishes, every parent was smaller than or equal to its children,
so I return True."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "[1, 3, 5, 7, 9, 8]: n is 6, so I check i = 0, 1, and 2.
  At 0, the children are 3 and 5. Both are bigger than 1.
  At 1, the children are 7 and 9. Both are bigger than 3.
  At 2, the left child is 8, which is bigger than 5,
  and the right child would be at 6, which is outside the array.
  So I return True. That matches."
- "[1, 3, 5, 2, 9]: n is 5, so I check i = 0 and 1.
  At 0, the children are 3 and 5, which are fine.
  At 1, the left child is 2, which is smaller than 3.
  So I return False. That matches."
- "Empty array: n is 0, the loop never runs, so I return True."
- "One element: n // 2 is 0, the loop never runs, so I return True."
- "All equal: no child is strictly smaller, so I return True."
- "[1, 0]: at i = 0, the left child 0 is smaller than 1, so I return False."
- "A problem at the bottom: the loop checks every parent,
  including the ones right above the leaves, so it gets caught."

"The output matches what I expected for all of them."

"To recap, time is O(n) and space is O(1)."
"""
class Solution():
    def isMinHeap(self, nums):
        n = len(nums)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and nums[left] < nums[smallest]:
                return False
            if right < n and nums[right] < nums[smallest]:
                return False
        return True
