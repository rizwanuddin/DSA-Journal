"""
Implement Min Heap - Medium

You need to implement the Min Heap with the following given methods.

insert (x) -> insert value x to the min heap
getMin -> Output the minimum value from min heap
exctractMin -> Remove the minimum element from the heap
heapSize -> return the current size of the heap
isEmpty -> returns if heap is empty or not
changeKey (ind, val) -> update the value at given index to val 
(index will be given 0-based indexing)
initializeHeap -> Initialize the heap

Example 1:
Input : operation = [ "initializeheap", "insert", "insert", "insert", "getMin", "heapSize", "isEmpty", "extractMin", "changeKey" , "getMin" ]
nums = [ [4], [1], [10], [0, 16] ]
Output : [ null, null, null, null, 1, 3, 0, null, null, 10 ]
Explanation : In 1st operation we initialize the heap to empty heap.
In 2nd, 3rd, 4th operation we insert 4, 1, 10 to the heap respectively. The heap after 4th operation will be -> [1, 4, 10].
In 5th operation we output the minimum element from the heap i.e. 1.
In 6th operation we output the size of the current heap i.e. 3.
In 7th operation we output whether the heap is empty or not i.e. false (0).
In 8th operation we remove the minimum element from heap. So the ne heap becomes -> [4, 10].
In 9th operation we change the 0th index element to 16. So new heap becomes -> [16, 10]. After heapify -> [10, 16].
In 10th operation we output the minimum element of the heap i.e. 10.




# Implement a Min-Heap: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I need to build a min-heap class from scratch.
It should support these operations:
initializeHeap, insert, getMin, extractMin,
heapSize, isEmpty, and changeKey."

"getMin returns the smallest value without removing it.
extractMin removes the smallest value and returns it.
changeKey updates the value at a given index,
and keeps the heap valid."

"I have a few quick questions before I start."

"What should getMin and extractMin return if the heap is empty?"
→ I'll assume None.

"Is the index in changeKey always valid?"
→ I'll assume yes.

"Can there be duplicate values?"
→ I'll assume yes. Equal values don't break the heap rule.

"Can I use Python's heapq, or should I write the heap logic myself?"
→ I'll assume I write it myself.

"Okay, so I need a structure that always gives me the smallest value quickly,
and stays fast when I add, remove, or change values."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
insert(5), insert(3), insert(8), insert(1)
getMin()      → 1
extractMin()  → 1
getMin()      → 3
heapSize()    → 3
changeKey(index of 8, 0)
getMin()      → 0
```

"A few edge cases:"
- "getMin or extractMin on an empty heap: return None."
- "extractMin on a heap with one element: return it,
  and the heap becomes empty."
- "changeKey to the same value: nothing moves."
- "Inserting duplicates, like 2 and 2: both are kept,
  and extractMin returns 2 twice."
- "initializeHeap after some inserts: the heap is empty again."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I just keep all the values in a regular list."

"If the list is unsorted:
insert is O(1), because I just append.
But getMin and extractMin are O(n),
because I have to scan the whole list to find the smallest."

"If I keep the list sorted instead:
getMin is O(1), because the smallest is at the front.
But insert is O(n), because I have to shift values to make room.
And extractMin is also O(n), because removing from the front shifts everything."

"changeKey is O(n) either way,
since I have to scan or re-sort."

"The space is O(n) for the list."

"The problem is that one of the operations is always O(n).
If I do a lot of inserts and extracts, that adds up fast."

## 4. Optimal solution

"The bottleneck is that a plain list makes me choose:
either fast insert, or fast getMin, but not both."

"Instead of keeping everything fully sorted,
I can keep it only partially sorted, using a binary heap."

"The rule is simple: every parent is smaller than or equal to its children.
That's enough to guarantee the smallest value is always at the top,
without sorting everything."

"The data structure I'll use is a list that represents a complete binary tree,
because I can find any node's parent and children with simple math.
The children of index i are at 2i + 1 and 2i + 2,
and the parent is at (i - 1) // 2."

"I'll write two helper functions that do all the real work."

"Sift up: when a value might be smaller than its parent,
I keep swapping it with its parent until it's in the right spot."

"Sift down: when a value might be bigger than its children,
I keep swapping it with the smaller child until it's in the right spot."

"When I insert, I add the value at the end, then sift it up."

"When I extract the min, I save the top value.
Then I move the last value to the top, and sift it down."

"When I change a key, I update the value.
If it got smaller, I sift up. If it got bigger, I sift down."

"getMin just returns the first element.
heapSize and isEmpty just check the length of the list."

"The time for each operation is:
insert, extractMin, and changeKey are O(log n),
because a value only moves along one path, and the height is log n.
getMin, heapSize, and isEmpty are O(1).
initializeHeap is O(1)."

"The space is O(n) for the list."

"So instead of one operation being O(n),
the slowest operation is now O(log n)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution,
and inside it, a class called MinHeap."

"In the constructor, I set self.heap to an empty list.
This list stores all the values in heap order."

"initializeHeap also sets self.heap to an empty list.
That resets the heap, so it can be reused."

"Now insert, which takes x.
I append x to the end of the list.
That keeps the tree complete, since I'm filling the next open spot.
Then I call sift up on the last index,
because the new value might be smaller than its parent."

"Next, getMin.
If the heap is empty, I return None.
Otherwise, I return self.heap[0].
The smallest value is always at the top, so this is O(1)."

"Next, extractMin.
If the heap is empty, I return None."

"Otherwise, I save the top value in min_val.
That's what I'll return."

"Then I pop the last value off the list and store it in last.
I pop from the end because that's O(1),
and it keeps the tree complete."

"If the heap still has values after the pop,
I put last at the top, in self.heap[0].
Then I sift it down,
because it's probably bigger than its new children."

"I check if the heap is empty first,
because if there was only one value,
I already popped it, and there's nothing to put back."

"Then I return min_val."

"Next, heapSize returns the length of the list."

"And isEmpty returns whether the length is 0."

"Now changeKey, which takes ind and val.
I save the old value in old, so I know which way to move.
Then I set self.heap[ind] to val."

"If val is smaller than old, it might be smaller than its parent,
so I sift up from ind."

"If val is bigger than old, it might be bigger than its children,
so I sift down from ind."

"If they're equal, nothing changed, so I don't do anything."

"Now the helper _sift_up, which takes an index i.
I store self.heap in a local variable called heap, just to keep the lines short."

"I loop while i is greater than 0,
and heap[i] is smaller than its parent at (i - 1) // 2.
I check i > 0 first, because the root has no parent."

"Inside the loop, I compute the parent index and store it in parent.
I swap heap[i] and heap[parent].
Then I set i to parent, and keep checking from there."

"Now the helper _sift_down, which takes an index i.
Again, I store self.heap in heap, and its length in n."

"I start a while True loop, and I'll break once the value is in place."

"I compute left as 2 * i + 1, and right as 2 * i + 2."

"I set smallest to i.
I'm assuming the current value is the smallest until I find a smaller child."

"If left is inside the list and heap[left] is smaller than heap[smallest],
smallest becomes left.
I check the bounds first, so I never index outside the list."

"Then I do the same check for right.
So smallest ends up as the smaller child, if either child is smaller."

"If smallest is still i, the value is in the right place, so I break."

"Otherwise, I swap heap[i] and heap[smallest].
Then I set i to smallest, and keep going down."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "Insert 5: the heap is [5].
  Insert 3: it goes to index 1, it's smaller than 5, so they swap.
  The heap is [3, 5].
  Insert 8: it goes to index 2, and it's bigger than 3, so it stays.
  The heap is [3, 5, 8].
  Insert 1: it goes to index 3, swaps with 5, then swaps with 3.
  The heap is [1, 3, 8, 5]."
- "getMin returns 1, which matches."
- "extractMin saves 1, pops 5, and puts it at the top.
  The heap is [5, 3, 8]. 5 swaps with its smaller child 3.
  The heap is [3, 5, 8], and it returns 1. That matches."
- "getMin returns 3, and heapSize returns 3. That matches."
- "changeKey at index 2, from 8 to 0. 0 is smaller, so I sift up.
  It swaps with 3. The heap is [0, 5, 3], and getMin returns 0.
  That matches."
- "Empty heap: getMin and extractMin both return None."
- "One element: extractMin pops it, the heap is empty,
  so I skip putting anything back, and return it."
- "changeKey to the same value: neither branch runs."
- "Duplicates: sift up and sift down only swap when something is
  strictly smaller, so equal values just stay where they are."
- "initializeHeap resets the list, so isEmpty returns True."

"The output matches what I expected for all of them."

"To recap, insert, extractMin, and changeKey are O(log n),
getMin, heapSize, and isEmpty are O(1),
and space is O(n)."
"""
class Solution:
    class MinHeap:
        def __init__(self):
            self.heap = []

        def initializeHeap(self):
            self.heap = []

        def insert(self, x):
            self.heap.append(x)
            self._sift_up(len(self.heap) - 1)

        def getMin(self):
            if not self.heap:
                return None
            return self.heap[0]

        def extractMin(self):
            if not self.heap:
                return None
            min_val = self.heap[0]
            last = self.heap.pop()
            if self.heap:
                self.heap[0] = last
                self._sift_down(0)
            return min_val

        def heapSize(self):
            return len(self.heap)

        def isEmpty(self):
            return len(self.heap) == 0

        def changeKey(self, ind, val):
            old = self.heap[ind]
            self.heap[ind] = val
            if val < old:
                self._sift_up(ind)
            elif val > old:
                self._sift_down(ind)

        def _sift_up(self, i):
            heap = self.heap
            while i > 0 and heap[i] < heap[(i - 1) // 2]:
                parent = (i - 1) // 2
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent

        def _sift_down(self, i):
            heap = self.heap
            n = len(heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i
                if left < n and heap[left] < heap[smallest]:
                    smallest = left
                if right < n and heap[right] < heap[smallest]:
                    smallest = right
                if smallest == i:
                    break
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest