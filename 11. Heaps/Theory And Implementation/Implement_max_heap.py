"""
Implement Max Heap - Medium

You need to implement the Max Heap with the following given methods.

insert (x) -> insert value x to the max heap
getMax -> Output the maximum value from the max heap
exctractMax -> Remove the maximum element from the heap
heapSize -> return the current size of the heap
isEmpty -> returns if heap is empty or not
changeKey (ind, val) -> update the value at given index to val (index will be given 0-based 
indexing)
initializeHeap -> Initialize the heap
Note: When extracting max, if both left and right children are equal, you must swap with the LEFT 
child.

Example 1:
Input : operation = [ "initializeHeap", "insert", "insert", "insert", "getMax", "heapSize", "isEmpty", "exctractMax", "changeKey" , "getMax" ]
nums = [ [4], [1], [10], [0, 16] ]
Output : [ null, null, null, null, 10, 3, 0, null, null, 16 ]
Explanation :
In 1st operation we initialize the heap to empty heap.
In 2nd, 3rd, 4th operation we insert 4, 1, 10 to the heap respectively. The heap after 4th operation will be -> [10, 4, 1].
In 5th operation we output the maximum element from the heap i.e. 10.
In 6th operation we output the size of the current heap i.e. 3.
In 7th operation we output whether the heap is empty or not i.e. false (0).
In 8th operation we remove the maximum element from heap. So the ne heap becomes -> [4, 1].
In 9th operation we change the 0th index element to 16. So new heap becomes -> [16, 1]. After heapify -> [16, 1].
In 10th operation we output the maximum element of the heap i.e. 16.

Example 2:
Input : operation = [ "initializeHeap", "insert", "insert", "exctractMax", "getMax", "insert", "heapSize", "isEmpty", "exctractMax", "changeKey" , "getMax" ]
nums = [ [4], [1], [4], [0, 2] ]
Output : [ null, null, null, null, 1, null, 2, 0, null, null, 2 ]
Explanation :
In 1st operation we initialize the heap to empty heap.
In 2nd, 3rd operation we insert 4, 1 to the heap respectively. The heap after 4th operation will be -> [4, 1].
In 4th operation we remove the maximum element from heap. So the ne heap becomes -> [1].
In 5th operation we output the maximum element of the heap i.e. 1.
In 6th operation we operation we insert 4 to the heap. The heap after 6th operation will be -> [4, 1].
In 7th operation we output the size of the current heap i.e. 2.
In 8th operation we output whether the heap is empty or not i.e. false (0).
In 9th operation we remove the maximum element from heap. So the ne heap becomes -> [1].
In 10th operation we change the 0th index element to 2. So new heap becomes -> [2].
In 11th operation we output the maximum element of the heap i.e. 2.




# Implement a Max-Heap: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I need to build a max-heap class from scratch.
It should support initializeHeap, insert, getMax, extractMax,
heapSize, isEmpty, and changeKey."

"getMax returns the biggest value without removing it.
extractMax removes the biggest value.
changeKey updates the value at a given index,
and keeps the heap valid."

"I have a few quick questions before I start."

"What should getMax and extractMax do if the heap is empty?"
→ I'll assume they return None.

"When I'm moving a value down and both children are equal,
which child do I swap with?"
→ The problem says the left child, so I'll make sure ties go left.

"Is the index in changeKey always valid, and 0-based?"
→ I'll assume yes.

"Can there be duplicate values?"
→ I'll assume yes.

"Can I use Python's heapq?"
→ I'll assume no, I'll write the logic myself.
heapq is also a min-heap, so it wouldn't fit directly anyway.

"Okay, so this is the same idea as a min-heap,
but every parent has to be bigger than or equal to its children,
so the biggest value is always at the top."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
initializeHeap()
insert(4), insert(1), insert(10)   → heap is [10, 4, 1]
getMax()      → 10
heapSize()    → 3
isEmpty()     → False
extractMax()  → heap is [4, 1]
changeKey(0, 16) → heap is [16, 1]
getMax()      → 16
```

"A second one:"

```
insert(4), insert(1)   → [4, 1]
extractMax()           → [1]
getMax()               → 1
insert(4)              → [4, 1]
heapSize()             → 2
extractMax()           → [1]
changeKey(0, 2)        → [2]
getMax()               → 2
```

"A few edge cases:"
- "getMax or extractMax on an empty heap: return None."
- "extractMax with one element: the heap becomes empty."
- "changeKey to the same value: nothing moves."
- "Two equal children when sifting down: swap with the left one."
- "Duplicates, like inserting 5 twice: both stay in the heap."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I just keep all the values in a regular list."

"If the list is unsorted:
insert is O(1), because I just append.
But getMax and extractMax are O(n),
because I have to scan the whole list to find the biggest."

"If I keep the list sorted from biggest to smallest:
getMax is O(1), because the biggest is at the front.
But insert is O(n), because I have to shift values to make room.
And extractMax is O(n) too, because removing from the front shifts everything."

"changeKey is O(n) either way."

"The space is O(n) for the list."

"The problem is that one of the operations is always O(n).
If I do a lot of inserts and extracts, that gets slow."

## 4. Optimal solution

"The bottleneck is that a plain list makes me choose:
fast insert, or fast getMax, but not both."

"Instead of keeping everything fully sorted,
I can keep it only partly sorted, using a binary max-heap."

"The rule is simple: every parent is bigger than or equal to its children.
That's enough to keep the biggest value at the top,
without sorting everything."

"The data structure I'll use is a list that represents a complete binary tree,
because I can find any node's parent and children with simple math.
The children of index i are at 2i + 1 and 2i + 2,
and the parent is at (i - 1) // 2."

"I'll write two helpers that do the real work."

"Sift up: when a value might be bigger than its parent,
I keep swapping it with its parent until it fits."

"Sift down: when a value might be smaller than its children,
I keep swapping it with the bigger child until it fits.
I only swap when a child is strictly bigger,
so if both children are equal, the left one wins,
because I check it first."

"When I insert, I add the value at the end, then sift it up."

"When I extract the max, I move the last value to the top,
then sift it down."

"When I change a key, I update the value.
If it got bigger, I sift up. If it got smaller, I sift down.
That's the opposite of the min-heap, because now big values go up."

"getMax returns the first element.
heapSize and isEmpty just check the list's length."

"The time for each operation is:
insert, extractMax, and changeKey are O(log n),
because a value only moves along one path, and the height is log n.
getMax, heapSize, isEmpty, and initializeHeap are O(1)."

"The space is O(n) for the list."

"So the slowest operation goes from O(n) down to O(log n)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution,
and inside it, a class called MaxHeap."

"In the constructor, I set self.heap to an empty list.
This list holds the values in heap order."

"initializeHeap also sets self.heap to an empty list,
so the heap can be reset and reused."

"Now insert, which takes x.
I append x to the end of the list.
That keeps the tree complete, since I'm filling the next open spot.
Then I call _sift_up on the last index,
because the new value might be bigger than its parent."

"Next, getMax.
If the heap is empty, I return None.
Otherwise, I return self.heap[0], because the biggest value is always at the top."

"Next, extractMax.
If the heap is empty, I return None."

"Otherwise, I save the top value in max_val."

"Then I pop the last value off the list and store it in last.
Popping from the end is O(1), and it keeps the tree complete."

"If the heap still has values, I put last at the top,
and sift it down, because it's probably smaller than its new children."

"I check if the heap is empty first,
because if there was only one value, I already removed it,
and there's nothing to put back."

"Then I return max_val."

"heapSize returns the length of the list.
And isEmpty returns whether the length is 0."

"Now changeKey, which takes ind and val.
I save the current value in old_num, so I know which way to move.
Then I set self.heap[ind] to val."

"If val is bigger than old_num, it might be bigger than its parent,
so I sift up from ind."

"If val is smaller than old_num, it might be smaller than its children,
so I sift down from ind."

"If they're equal, nothing changed, so I do nothing."

"Now the helper _sift_up, which takes an index i.
I store self.heap in a local variable called heap, to keep the lines short."

"I loop while i is greater than 0,
and heap[i] is bigger than its parent at (i - 1) // 2.
I check i > 0 first, because the root has no parent."

"Inside the loop, I compute the parent index and store it in parent.
I swap heap[i] and heap[parent].
Then I set i to parent, and keep checking from there."

"Now the helper _sift_down, which takes an index i.
I store self.heap in heap, and its length in n."

"I start a while True loop, and I'll break once the value is in place."

"I compute left as 2 * i + 1, and right as 2 * i + 2."

"I set largest to i.
I'm assuming the current value is the biggest until I find a bigger child."

"If left is inside the list and heap[left] is bigger than heap[largest],
largest becomes left.
I check the bounds first, so I never index outside the list."

"Then I check right the same way.
I use strictly bigger here,
so if right equals left, largest stays as left.
That's how I make ties go to the left child."

"If largest is still i, the value is in the right place, so I break."

"Otherwise, I swap heap[i] and heap[largest].
Then I set i to largest, and keep going down."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "Insert 4: the heap is [4].
  Insert 1: it's smaller than 4, so it stays. The heap is [4, 1].
  Insert 10: it goes to index 2, and it's bigger than 4, so they swap.
  The heap is [10, 1, 4]."
- "getMax returns 10, heapSize returns 3, and isEmpty returns False.
  That matches."
- "extractMax: I save 10, pop 4, and put it at the top.
  The heap is [4, 1]. 4 is bigger than 1, so it stays.
  The heap is [4, 1]. That matches."
- "changeKey(0, 16): 16 is bigger than 4, so I sift up.
  It's already at index 0, so it stays. The heap is [16, 1].
  getMax returns 16. That matches."
- "Second example: after inserting 4 and 1, extractMax leaves [1].
  getMax returns 1. Insert 4 makes it [4, 1].
  heapSize returns 2. extractMax leaves [1].
  changeKey(0, 2) gives [2], and getMax returns 2. That matches."
- "Empty heap: getMax and extractMax return None."
- "One element: extractMax empties the heap and skips putting anything back."
- "Same value in changeKey: neither branch runs."
- "Equal children: the right child isn't strictly bigger than the left,
  so I swap with the left one, like the problem asks."

"The output matches what I expected for all of them."

"To recap, insert, extractMax, and changeKey are O(log n),
getMax, heapSize, isEmpty, and initializeHeap are O(1),
and space is O(n)."
"""

class Solution:
    class MaxHeap:
        def __init__(self):
            self.heap = []

        def initializeHeap(self):
            self.heap = []

        def insert(self, x):
            self.heap.append(x)
            self._sift_up(len(self.heap) - 1)

        def getMax(self):
            if not self.heap:
                return None
            return self.heap[0]

        def extractMax(self):
            if not self.heap:
                return None
            max_val = self.heap[0]
            last = self.heap.pop()
            if self.heap:
                self.heap[0] = last
                self._sift_down(0)
            return max_val

        def heapSize(self):
            return len(self.heap)

        def isEmpty(self):
            return len(self.heap) == 0

        def changeKey(self, ind, val):
            old_num = self.heap[ind]
            self.heap[ind] = val
            if val > old_num:
                self._sift_up(ind)
            elif val < old_num:
                self._sift_down(ind)

        def _sift_up(self, i):
            heap = self.heap
            while i > 0 and heap[i] > heap[(i - 1) // 2]:
                parent = (i - 1) // 2
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent

        def _sift_down(self, i):
            heap = self.heap
            n = len(heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                if left < n and heap[left] > heap[largest]:
                    largest = left
                if right < n and heap[right] > heap[largest]:
                    largest = right
                if largest == i:
                    break
                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest




