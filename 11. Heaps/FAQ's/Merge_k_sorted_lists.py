"""
Merge K sorted Lists

Given heads of k sorted linked lists as an array called heads, merge them into one single sorted linked list and 
return the head of that list.

Example 1:
Input: heads = [[head -> 1 -> 2 -> 3 -> 4], [head -> -4 -> -3], [head -> -5 -> -3 -> 1 -> 2 -> 3 -> 4]]
Output: head -> -5 -> -4 -> -3 -> -3 -> 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4
Explanation:
head -> -5 -> -4 -> -3 -> -3 -> 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4
The nodes in bold come from the 3rd list, the underlined nodes come from the 2nd list, rest are from the 1st list.

Example 2:
Input: heads = [[head -> -5 -> -4 -> -1], [head -> 10 -> 11 -> 12]]
Output: head -> -5 -> -4 -> -1 -> 10 -> 11 -> 12
Explanation:
head -> -5 -> -4 -> -1 -> 10 -> 11 -> 12
The nodes in bold come from the 1st list, rest are from the 2nd list.



# Merge K Sorted Lists: My Thought Process

## What is the problem exactly stating?

"So what is the problem exactly stating?
It is stating that I'll be given K sorted linked lists.
My task is to take all the values from all of them,
put them together in sorted order into one list,
and return the head of that new list."

"I'm given a list of heads, correct?
If I'm given the head, I can access the entire list.
That's why a list of heads is enough."

"Quick things I'd confirm:
can some of the lists be empty? I'll assume yes.
Can the whole input be empty? Then I just return None.
Can values repeat or be negative? I'll assume yes, it doesn't matter."

## Brute force

"So if this problem comes up in an interview,
what is the extreme naive solution I can think of?"

"I'll take all the elements from the first list,
from the second list, and so on till the kth list,
and put them into an array.
Once I do that, I have all the integers in one array, agreed?"

"What is the next step? Sort that array.
Now all the integers are in sorted fashion."

"Once I have that, I convert the array into a linked list,
and return the head of that new list.
Quite simple."

### Time complexity

"Now what will be the time complexity?"

"First portion, the traversal.
I have K lists.
To ease out computations, I'll assume each list is of length n.
So traversing one list takes big O of n,
and doing it for all K lists is nothing but n into k."

"Next portion, the sort.
Sort usually takes M logarithmic of M, if the array is of size M.
Now what is M?
It's all the elements combined, which is nothing but n into k.
So the sort is n into k, into logarithmic of n into k."

"Next portion, converting the array back into a list.
That's a linear traversal, so big O of M again,
where M is n into k."

"So the overall time complexity will be
n into k, plus M log M, plus M, where M is n into k.
The sort dominates, so near about big O of M log M."

### Space complexity

"Am I using any extra space? Yes.
I'm using an array that stores all the elements, that's big O of M.
And I'm creating a whole new list, that's another big O of M.
So the space is somewhere in terms of big O of M, where M is n into k."

"Obviously the interviewer will not be happy with this,
and he'll ask me to optimize."

## Optimal

"In order to optimize, I'll be using a minimum heap.
In case you don't know about it, nothing to worry about.
Just remember, it's a data structure that always gives you the minimum value."

"Here's the key thing.
Every list is already sorted, right?
So the smallest element overall has to be one of the heads, agreed?"

"So what I'll do is, I'll take all the heads,
and put them into the min-heap.
I'll store the value first, then the node,
because the heap compares by the first thing in the tuple."

"I'll also store the index of the list in the middle, as a tie-breaker.
Why? If two values are equal, Python moves on to compare the next item.
It can't compare two nodes, so it would crash.
The index is a number, so it can always be compared.
Super simple fix."

"Now I need to build the new list,
so I'll use the concept of a dummy node,
and have a temp pointing to it."

"What is the next step?
I ask the heap, give me the minimum.
I take it out, make temp point to it, and move temp forward."

"Now that node is taken, so what comes after it in its own list?
Its next. If its next is not null, I put the next into the heap.
If it's null, that list is done, nothing to put."

"I keep doing this till the heap is empty.
When the heap is empty, all the nodes are linked in sorted order."

"Where is my head?
Can I say dummy node dot next is my head? I can.
So I return dummy dot next."

"And I'm reusing the same nodes that were given to me.
I'm only changing the links, no new nodes are created."

### Time complexity

"Now let's discuss the time complexity."

"First portion, I have a for loop that pushes all the heads.
The add operation takes logarithmic of the size of the heap.
The heap never holds more than K elements,
so each push is logarithmic of K.
The loop runs K times, so this portion is K into logarithmic of K."

"Next portion, the while loop.
For how many times is the while loop running?
It runs till the heap is empty.
At every iteration, I take one node and attach it to the new list.
So eventually every element goes through the heap, agreed?
Assuming each list is of size n, the total number of elements is n into k.
So the while loop is running n into k times."

"How many operations am I doing inside it?
One pop and one push.
That's two operations on the heap,
and each one is logarithmic of K, because the heap is at most size K.
So it's two into logarithmic of K per iteration."

"So the overall time complexity is somewhere near
K logarithmic of K, for the for loop,
plus n into k, into logarithmic of K, for the while loop."

"If I compare with the brute force,
that was n into k, into log of n into k.
Now it's n into k, into log of K.
Since K is the number of lists, it's much smaller than all the elements combined,
so this is better."

### Space complexity

"What about the space complexity?
Can I say it's big O of K? I can.
I'm only using the heap, and at max it stores K elements,
one from each list.
I'm reusing the nodes, so nothing extra there."

## Code

"First, I make an empty list called pq, that's my min-heap."

"Then I loop over every index i in lists.
If lists[i] is not null, I push the tuple value, i, node into pq.
I check for null, because some lists can be empty."

"Then I create a dummy node with value 0, and set temp to it."

"Now I loop while pq is not empty."

"Inside, I pop the minimum, and unpack it into val, i, and node."

"I make temp.next point to node, so it's attached to my new list."

"Then I check, does node have a next?
If yes, I push node.next's value, the same i, and node.next into pq."

"Then I move temp to temp.next."

"Once the heap is empty, I return dNode.next,
which is the head of the merged list.
Done and dusted."

## Quick check

```
lists = [1 → 4 → 5, 1 → 3 → 4, 2 → 6]
```

- "The heap starts with 1, 1, 2."
- "I pop 1 from list 0, and push 4. Then I pop 1 from list 1, and push 3."
- "I pop 2, and push 6. I pop 3, and push 4. I pop 4, then the other 4, and push 5."
- "I pop 5, then 6."
- "The merged list is 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6. Perfect."

"Empty input or all empty lists: nothing goes into the heap,
so I return dummy.next, which is None."
"""
import heapq

class Solution:
    def mergeKLists(self, lists):
        pq = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        dNode = ListNode(0)
        temp = dNode

        while pq:
            val, i, node = heapq.heappop(pq)
            temp.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            temp = temp.next

        return dNode.next          

            