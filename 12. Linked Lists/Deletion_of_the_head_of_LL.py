"""
Deletion of the head of LL

Given the head of a singly linked list, delete the head of the linked list and return the head of the modified list. The head is the first node of 
the linked list.
Note : Please note that this section might seem a bit difficult without prior knowledge on what linkedList is, we will soon try to add basics 
concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!

Example 1:
Input: linkedList = [1, 2, 3]
Output: [2, 3]
Explanation:
The first node was removed.

Example 2:
Input: linkedList = [1]
Output: []
Explanation:
Note that the head of the linked list gets changed.



# Delete the Head of a Linked List: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given the head of a singly linked list.
I need to remove the first node,
and return the head of the list that's left."

"I have a few quick questions before I start."

"Can the list be empty, where head is None?"
→ I'll assume yes, and then I just return None.

"If there's only one node, should I return None?"
→ I'll assume yes, since the list becomes empty.

"Is it a singly linked list, with only next pointers?"
→ I'll assume yes.

"Do I need to free the memory of the removed node?"
→ I'll assume no. In Python, the garbage collector cleans it up
once nothing points to it.

"Okay, so the new head is just the second node."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
1 → 2 → 3 → None
```
"Removing 1 leaves 2 → 3. Answer: [2, 3]."

```
1 → None
```
"Removing the only node leaves an empty list. Answer: []."

"A few edge cases:"
- "Empty list, head is None: Answer: None."
- "Two nodes, like 4 → 7: Answer: [7]."
- "Repeated values, like 2 → 2 → 2: only the first one goes.
  Answer: [2, 2]."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I walk through the whole list, and copy every value except the first
into a brand new linked list.
Then I return the head of the new list."

"This works because the new list has everything except the first node."

"The time is O(n), because I walk through every node."

"The space is O(n), because I build a whole new list."

"The problem is that I'm copying the entire list,
when only the very first node needs to change.
Every node after the head is already in the right place."

## 4. Optimal solution

"The bottleneck is copying the whole list,
when the rest of the list is already correct."

"Instead of building a new list,
I can just move the head forward by one node."

"The data structure is the linked list itself.
The second node already points to the rest of the list,
so if I return it as the new head, the first node is gone."

"As I start, I check if the head is None.
If it is, there's nothing to remove, so I return None."

"When the head exists, I set head to head.next."

"At the end, I return the new head.
If there was only one node, head.next is None,
so I correctly return an empty list."

"The time is O(1), because I only touch the first node."

"The space is O(1), because I don't create anything new."

"So I go from O(n) time and space down to O(1) for both."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution,
and a function called removeHead that takes self and head."

"Before anything else, I check if head is None.
If it is, the list is empty, so there's nothing to remove,
and I return None.
This also stops me from trying to read head.next on None,
which would crash."

"Then I set head to head.next.
That moves the head forward to the second node.
Now nothing in my code points to the old first node,
so it's effectively removed, and Python will clean it up."

"Finally, I return head.
That's the start of the list without the old first node."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "1 → 2 → 3: head isn't None, so head becomes the node 2.
  I return 2 → 3. That matches."
- "1 → None: head isn't None, so head becomes head.next, which is None.
  I return None, which is an empty list. That matches."
- "Empty list: head is None, so I return None right away."
- "4 → 7: head becomes 7, and I return [7]."
- "2 → 2 → 2: head moves to the second 2, and I return [2, 2]."

"The output matches what I expected for all of them."

"To recap, time is O(1) and space is O(1)."

"If this were C or C++, I'd also save the old head in a temporary variable,
and free its memory before returning,
so I don't leak memory."
"""
class Solution:
    def removeHead(self, head):
        if head is None:
            return None
        head = head.next
        return head