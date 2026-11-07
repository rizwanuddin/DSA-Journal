"""
Traversal in Linked List

Given the head of a singly Linked List. Traverse the entire Linked List and return its elements in an array in the order of 
their appearance.

Example 1:
Input: linkedList = [5, 4, 3, 1, 0]
Output: [5, 4, 3, 1, 0]
Explanation:
The nodes in the Linked List are 5 -> 4 -> 3 -> 1 -> 0, with the head pointing to node with value 5.

Example 2:
Input: linkedList = [1]
Output: [1]
Explanation:
Only one node (head) present in the list.



# Linked List Traversal: My Thought Process

## 1. Clarify the prompt

"Before I jump in, I want to make sure I understand the problem correctly."

"So I'm given the head of a singly linked list.
Each node has a value and a pointer to the next node.
I need to visit every node from the head to the end,
and return all the values in order, as a list."

"I have a few quick questions before I start."

"Can the list be empty, where head is None?"
→ I'll assume yes, and then I return an empty list.

"Is it a singly linked list, with only next pointers?"
→ I'll assume yes.

"Can the list have a cycle?"
→ I'll assume no, so it always ends at None.

"Should I leave the list unchanged?"
→ I'll assume yes. I'm only reading it.

"Can the values be negative or repeated?"
→ I'll assume yes. It doesn't matter, since I'm just collecting them.

"Okay, so I just need to walk from node to node,
collecting each value, until I fall off the end."

## 2. Test cases

"Let me write down a few test cases before I think about the approach."

```
1 → 2 → 3 → 4 → None
```
"Answer: [1, 2, 3, 4]."

"A few edge cases:"
- "Empty list, head is None: Answer: []."
- "One node, like 5 → None: Answer: [5]."
- "Repeated values, like 2 → 2 → 2: Answer: [2, 2, 2]."
- "Negative values, like -1 → 0 → 3: Answer: [-1, 0, 3]."

"Do these expected outputs match what you have in mind?"

## 3. Brute force

"I want to be upfront: there isn't a faster way to do this.
I have to visit every node at least once to read its value,
so any solution is at least O(n) time."

"My first idea could be to do it with recursion.
I read the current node's value,
then call the same function on the next node,
until I reach None."

"That works, and it's O(n) time.
But it's O(n) space for the call stack,
because every node adds one more call.
On a long list, it could also hit Python's recursion limit of about 1000."

"So the time can't improve,
but I can bring the extra space down."

## 4. Optimal solution

"The bottleneck in the recursive version is the call stack,
not the time."

"Instead of using recursion,
I can walk the list with a simple loop and one pointer."

"The data structures I'll use are one pointer called curr,
and a list called res for the answer.
The pointer keeps track of where I am,
and the list stores the values in order,
since appending to a list is O(1)."

"As I go through the list, I add curr's value to res,
then move curr to the next node."

"When curr becomes None, I've passed the last node, so I stop."

"At the end, I return res."

"The time is O(n), because I visit each node exactly once."

"The space is O(1) extra, because I only use one pointer.
The output list is O(n), but that's the answer itself."

"So the time stays O(n), and the extra space goes from O(n) down to O(1)."

## 5. Ask for feedback

"Does this approach sound reasonable to you?
Should I go ahead and code it?"

## 6. Code while talking out loud

"First, I'll make a class called Solution,
and a function called LLTraversal that takes self and head."

"I'll set curr to head.
I'm using a separate pointer, so I don't lose track of the head
in case I need it later."

"Then I'll create an empty list called res.
This will hold the values in order."

"Now I start a while loop that runs as long as curr isn't None.
When curr is None, I've gone past the last node."

"Inside the loop, I append curr.val to res.
That records the value of the node I'm on."

"Then I set curr to curr.next.
That moves me forward to the next node.
On the last node, next is None, so the loop will stop."

"After the loop, I return res."

## 7. Testing

"Before I finish, I'll trace through my test cases."

- "1 → 2 → 3 → 4: curr starts at 1.
  I add 1, then move to 2. I add 2, then move to 3.
  I add 3, then move to 4. I add 4, then move to None.
  The loop stops, and I return [1, 2, 3, 4]. That matches."
- "Empty list: curr is None from the start,
  so the loop never runs, and I return []."
- "One node: I add 5, then curr becomes None.
  I return [5]."
- "Repeated values: I don't compare anything,
  so I just collect each 2, and return [2, 2, 2]."
- "Negative values: same thing, I return [-1, 0, 3]."

"The output matches what I expected for all of them."

"To recap, time is O(n) and space is O(1) extra,
plus O(n) for the output."

"If the list could have a cycle, this loop would never stop.
In that case, I'd first check for a cycle with a slow and a fast pointer,
which is Floyd's algorithm."
"""
class Solution:
    def LLTraversal(self, head):
        curr = head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
            
            
