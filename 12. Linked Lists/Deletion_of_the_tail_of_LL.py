"""
Deletion of the tail of Linked List

Given the head of a singly linked list, delete the tail of the linked list and return the head of the modified list.
The tail is the last node of the linked list.

Example 1:
Input: linkedList = [1, 2, 3]
Output: [1, 2]
Explanation:
The last node was removed.

Example 2:
Input: linkedList = [1]
Output: []
Explanation:
Note that the value of head is null here.




# Delete the Tail of a Linked List: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given the head of a singly linked list.
I need to remove the last node, which is the tail,
and return the head of the list that's left."

"I have a few quick questions before I start."

"Can the list be empty, where head is None?"
→ I'll assume yes, and then I return None.

"If there's only one node, should I return None?"
→ I'll assume yes, since removing it leaves an empty list.

"Is it a singly linked list, with only next pointers?"
→ I'll assume yes, so I can't walk backward from the tail.

"Do I have a separate pointer to the tail?"
→ I'll assume no. I only have the head.

"Okay, so the tricky part is that to remove the last node,
I need to stop at the node right before it,
and cut its next pointer."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
1 → 2 → 3 → None
```
"I need to stop at 2, and set its next to None.
Answer: [1, 2]."

```
1 → None
```
"Removing the only node leaves an empty list. Answer: []."

"A few edge cases:"
- "Empty list, head is None: Answer: None."
- "Two nodes, like 4 → 7: I stop at 4. Answer: [4]."
- "Repeated values, like 2 → 2 → 2: only the last one goes.
  Answer: [2, 2]."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"My first idea is the simplest one.
I walk through the list and copy all the values into an array.
Then I build a brand new linked list from every value except the last one,
and return its head."

"This works because the new list has everything except the tail."

"The time is O(n), because I go through every node,
and then build a new list."

"The space is O(n), for the array and the new list."

"The problem is that I'm copying the whole list,
when only one pointer actually needs to change.
The second-to-last node just needs to point to None."

## 4. Optimal solution

"The bottleneck is building a whole new list,
when I only need to change one pointer."

"Instead of copying everything,
I can walk to the second-to-last node,
and set its next to None."

"The data structure is the linked list itself,
plus one pointer called curr to walk through it."

"As I start, I check two cases.
If the list is empty, or has only one node,
removing the tail leaves nothing, so I return None."

"Otherwise, I walk curr forward while curr.next.next exists.
That means I keep going as long as there are at least two nodes ahead.
When it stops, curr is the second-to-last node."

"When I get there, I set curr.next to None.
That cuts off the tail."

"At the end, I return the original head,
since the front of the list didn't change."

"The time is O(n).
In a singly linked list, I have to walk to the end
to find the node before the tail. There's no shortcut."

"The space is O(1), because I only use one pointer."

"So the time stays O(n), but the space goes from O(n) down to O(1),
and I don't rebuild anything."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution,
and a function called removeTail that takes self and head."

"Before anything else, I check if head is None, or head.next is None.
If the list is empty, there's nothing to remove.
If there's only one node, removing it leaves an empty list.
So in both cases, I return None.
I check head is None first, so I never try to read .next on None."

"Then I set curr to head.
I use a separate pointer, so head still points to the start of the list."

"Now I start a while loop that runs while curr.next.next exists."

"I'm checking two steps ahead on purpose.
If I only checked curr.next, I'd stop on the tail itself.
But I need to stop one node before the tail,
so I can change its next pointer."

"I know curr.next exists here,
because I already handled the one-node case,
so reading curr.next.next is safe."

"Inside the loop, I move curr to curr.next."

"When the loop ends, curr.next is the tail,
and curr is the node right before it."

"Then I set curr.next to None.
That disconnects the tail from the list."

"Finally, I return head,
since the start of the list didn't change."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "1 → 2 → 3: the list has more than one node, so I keep going.
  curr starts at 1. curr.next.next is 3, which exists, so curr moves to 2.
  Now curr.next.next is None, so the loop stops.
  I set 2's next to None, and return 1 → 2. That matches."
- "1 → None: head.next is None, so I return None. That matches."
- "Empty list: head is None, so I return None right away."
- "4 → 7: curr starts at 4. curr.next.next is None,
  so the loop never runs. I set 4's next to None, and return [4]."
- "2 → 2 → 2: I stop at the second 2, cut off the last one,
  and return [2, 2]."

"The output matches what I expected for all of them."

"To recap, time is O(n) and space is O(1)."

"If I had a doubly linked list with a tail pointer,
I could do this in O(1), by jumping straight to the tail
and using its previous pointer."
"""
class Solution:
    def removeTail(self, head):
        if head is None or head.next is None:
            return None
        curr = head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        return head