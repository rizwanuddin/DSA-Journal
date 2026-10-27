"""
Heapify Algorithm - Medium

Given an array nums representing a min-heap and two integers ind and val, set the value at index ind (0-based) to val and perform the heapify algorithm such that the 
resulting array follows the min-heap property.

Modify the original array in-place, no need to return anything.

Example 1:
Input: nums = [1, 4, 5, 5, 7, 6], ind = 5, val = 2
Output: [1, 4, 2, 5, 7, 5]
Explanation: After setting index 5 to 2, the resulting heap in array form = [1, 4, 5, 5, 7, 2]
Parent of nums[5] = nums[2] = 5 > nums[5] = 2, so they are swapped.
Final array = [1, 4, 2, 5, 7, 5]

Example 2:
Input: nums = [2, 4, 3, 6, 5, 7, 8, 7], ind = 0, val = 7
Output: [3, 4, 7, 6, 5, 7, 8, 7]
Explanation: After setting index 0 to 7, the resulting heap in array form =[7, 4, 3, 6, 5, 7, 8, 7]
The parent of nums[2] = nums[0] = 7 > nums[2] = 3, so they are swapped. No further swaps are needed.
Final array = [3, 4, 7, 6, 5, 7, 8, 7]




# Heapify (Update a Value in a Min-Heap): My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given an array that is already a valid min-heap.
That means every parent is smaller than or equal to its children.
I'm also given an index and a new value.
I need to change the value at that index,
and then fix the array so it's a valid min-heap again."

"I have a few quick questions before I start."

"Is it a min-heap, not a max-heap?"
→ I'll assume min-heap.

"Is the heap stored as an array, where the children of index i
are at 2i + 1 and 2i + 2, and the parent is at (i - 1) // 2?"
→ I'll assume yes.

"Should I change the array in place?"
→ I'll assume yes, and I won't return anything.

"Is the index always valid?"
→ I'll assume yes.

"Can there be duplicate values?"
→ I'll assume yes. Equal values don't break the heap.

"Okay, so only one value changes,
and everything else in the heap was already correct.
I just need to move that one value to the right spot."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
nums = [1, 3, 5, 7, 9, 8], ind = 4, val = 0

        1
      /   \
     3     5
    / \   /
   7   9 8
```
"I change the 9 to a 0.
0 is smaller than its parent 3, so they swap.
Then 0 is smaller than its parent 1, so they swap again.
Answer: [0, 1, 5, 7, 3, 8]."

```
nums = [1, 3, 5, 7, 9, 8], ind = 0, val = 10
```
"I change the root to 10.
Its smaller child is 3, so they swap.
Then 10's smaller child is 7, so they swap again.
Answer: [3, 7, 5, 10, 9, 8]."

"A few edge cases:"
- "The new value is the same as the old one: nothing changes."
- "I update the root to something smaller: it's already at the top, so nothing moves."
- "I update a leaf to something bigger: it has no children, so nothing moves."
- "A heap with one element: nothing to compare, nothing moves."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I change the value, and then I rebuild the whole heap from scratch."

"The easiest way is to just sort the array.
A sorted array is always a valid min-heap,
because every value is smaller than everything after it."

"This works because I'm not trusting any of the old structure.
I'm making a brand new valid heap."

"The time is O(n log n) for sorting.
Even using the standard build-heap method, it's still O(n)."

"The space is O(1) extra, since I can sort in place."

"The problem is that I'm redoing the whole heap
when only one value changed.
Everything else was already in the right place."

## 4. Optimal solution

"The bottleneck is rebuilding everything,
even though only one spot is wrong."

"Instead of rebuilding the whole heap,
I can move just the changed value up or down until it fits."

"If the new value is smaller than the old one,
it might now be smaller than its parent.
So I move it up, swapping with the parent, until the parent is smaller.
That's called sift up, or bubble up."

"If the new value is bigger than the old one,
it might now be bigger than its children.
So I move it down, swapping with the smaller child,
until both children are bigger.
That's called sift down."

"I swap with the smaller child, not just any child.
That way, the value that moves up is the smallest of the three,
so the parent stays smaller than both children."

"If the value didn't change, I don't need to do anything."

"The data structure is just the array itself.
I use index math to find parents and children,
because a heap stored in an array lets me jump straight to them."

"As I go, I compare the new value with the old value
to decide which direction to move."

"When it's smaller, I keep swapping with the parent
while it's smaller than the parent."

"When it's bigger, I keep swapping with the smaller child
while a child is smaller than it."

"At the end, the heap is valid again, and I'm done."

"The time is O(log n).
The value moves along one path, either up or down,
and the heap's height is log n."

"The space is O(1), because I only use a few index variables."

"So I go from O(n log n) down to O(log n)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution."

"Then a function called heapify that takes self, nums, ind, and val."

"Before I change anything, I save the old value at nums[ind] in old_num.
I need it to decide which way the new value should move."

"Then I set nums[ind] to val."

"I store the length of the array in n.
I need it to check if a child index is inside the array."

"And I set i to ind.
i is the current position of the value I'm moving."

"Now I check if val is smaller than old_num.
If it is, the value might need to move up."

"I start a while loop that runs while i is greater than 0,
and nums[i] is smaller than its parent at (i - 1) // 2.
I check i > 0 first, because the root has no parent."

"Inside the loop, I compute the parent index as (i - 1) // 2,
and store it in parent."

"Then I swap nums[i] and nums[parent].
Now the smaller value is on top."

"Then I set i to parent, so I keep checking from the new position."

"Otherwise, if val is bigger than old_num,
the value might need to move down."

"I start a while True loop, and I'll break out when it's in the right place."

"Inside it, I compute left as 2 * i + 1, and right as 2 * i + 2.
Those are the two children of i."

"I set smallest to i.
I'm assuming the current value is the smallest until I find a smaller child."

"Then I check if left is inside the array,
and nums[left] is smaller than nums[smallest].
If so, smallest becomes left.
I check the bounds first, so I never index outside the array."

"Then I do the same check for right.
If it's smaller, smallest becomes right.
Doing this one after the other means smallest ends up as the smaller child."

"If smallest is still i, both children are bigger or there aren't any.
The value is in the right place, so I break."

"Otherwise, I swap nums[i] and nums[smallest].
Now the smallest of the three is on top."

"Then I set i to smallest, and keep checking from the new position."

"If val equals old_num, neither branch runs.
Nothing changed, so the heap is still valid."

"Since I changed the array in place, I don't need to return anything."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "First example: I set index 4 to 0.
  0 is smaller than 9, so I move up.
  Its parent is index 1, which is 3. 0 is smaller, so they swap.
  Now i is 1. Its parent is index 0, which is 1. 0 is smaller, so they swap.
  Now i is 0, so the loop stops.
  The array is [0, 1, 5, 7, 3, 8], which matches."
- "Second example: I set index 0 to 10.
  10 is bigger than 1, so I move down.
  The children are 3 and 5. The smaller one is 3 at index 1, so they swap.
  Now i is 1. The children are 7 and 9. The smaller one is 7 at index 3, so they swap.
  Now i is 3. Its children would be at 7 and 8, which are outside the array, so I break.
  The array is [3, 7, 5, 10, 9, 8], which matches."
- "Same value: neither branch runs, so nothing changes."
- "Root made smaller: the while loop checks i > 0 first, so it never runs."
- "Leaf made bigger: both child indexes are outside the array,
  so smallest stays i, and I break right away."
- "One element: n is 1, so there's no parent and no children. Nothing moves."

"The output matches what I expected for all of them."

"To recap, time is O(log n) and space is O(1)."
"""
class Solution:
    def heapify(self, nums, ind, val):
        old_num = nums[ind]
        nums[ind] = val
        n = len(nums)
        i = ind

        if val < old_num:
            while i > 0 and nums[i] < nums[(i - 1) // 2]:
                parent = (i - 1) // 2
                nums[i], nums[parent] = nums[parent], nums[i]
                i = parent

        elif val > old_num:
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