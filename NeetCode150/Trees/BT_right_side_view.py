"""
Binary Tree Right Side View - Medium

You are given the root of a binary tree. Return only the values of the nodes that are visible from the 
right side of the tree, ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,4,null,5]
Output: [1,3,5]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,2]
Output: [1,2]

Example 4:
Input: root = []
Output: []





# Binary Tree Right Side View: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
Imagine standing on the right side of the tree, looking at it.
I need to return the values of the nodes I can see, from top to bottom.

Quick questions:
- Is the answer one value per level? I'll assume yes.
- Can the tree be empty? I'll assume yes, and return an empty list.
- Can a node on the left be visible?
  Yes, if the right side has nothing at that depth.

## 2. Restate

So for each level of the tree, I want the rightmost node.
I return those values in order, from the top level to the bottom level.

## 3. Example

```
    1
   / \
  2   3
   \   \
    5   4
```

Level 0: only 1, so I see 1.
Level 1: 2 and 3, the rightmost is 3.
Level 2: 5 and 4, the rightmost is 4.
The answer is [1, 3, 4].

Another example, where the left side shows through:

```
    1
   / \
  2   3
 /
4
```

Level 2 only has 4.
It is on the left, but nothing blocks it, so I see it.
The answer is [1, 3, 4].

Edge case: an empty tree returns [].

## 4. Brute force

My first idea is to handle one level at a time on its own.
For each depth, I walk the whole tree and collect all nodes at that depth.
Then I take the last one, which is the rightmost.
I keep going until a depth has no nodes.

This works because it finds the rightmost node at every level.

The problem is the repeated work.
Each depth walks the whole tree again.
With h levels, that is O(n * h).
A skewed tree is the worst case, which gives O(n^2).

## 5. Key observation

The problem is really asking for the last node of every level.
So this is level order traversal, with one small change.
Instead of keeping the whole level, I keep only the last node.

The repeated work was walking down from the root again for every level.
A queue removes that.
It lets me go through the tree level by level, in one pass.

A queue works because it is first in, first out.
If I add the left child before the right child,
then within each level the nodes come out from left to right.
So the last node I take out of a level is the rightmost one.

To know where a level ends, I use the queue's size at the start of each round.
At that moment, the queue holds only the current level.
So the node at position size - 1 is the last one.

## 6. Approach

Instead of walking from the root again for every level,
I can process one level at a time, and pick out the last node of each.

The data structure I will use is a queue,
because it gives me first-in, first-out order,
so within each level I see nodes from left to right.

As I go through the tree, I will take the queue's current size.
That tells me how many nodes are in this level.

When I take out the last node of that level,
I will add its value to the result.

For every node I take out, I will add its left and right children to the queue,
if they exist.

When the queue is empty, there are no more levels.

At the end, I return the result.

## 7. While coding

First I import deque from collections.
I'm using a deque as the queue, because removing from the front is O(1).
With a regular list, pop(0) is O(n), because everything shifts.

Then I make a class called Solution.

Then I make a function called rightSideBT that takes self and root.

Before anything else, I check if root is None, and if so I return an empty list.
That handles the empty tree.
It also stops me from putting None into the queue,
which would crash when I try to read its value.

Then I create the queue, starting with just the root.
This is level 0.

Then I create an empty list called res.
This will hold the right side view.

Now I start a while loop that runs as long as the queue isn't empty.
Each round of this loop handles one full level.

At the start of each round, I store the current length of the queue in size.
I do this before touching the queue.
Right now, the queue holds only this level.
If I checked the length during the loop, the children I add
would change it, and levels would get mixed up.

Then I loop size times, using a for loop with an index i.
This processes exactly the nodes of this level.
The index tells me which position I'm at in the level.

Inside it, I take the node from the front of the queue with popleft.

Then I check if i is equal to size - 1.
That means this is the last node of the level, which is the rightmost one.
If so, I add its value to res.
For every other node, I skip this step.

Then I check if node.left exists, and if so I add it to the queue.
Same for node.right.
I check for existence first, so I never add None to the queue.
I add left before right, so the order stays left to right.
These children go to the back, so they wait until the next round.

When the while loop ends, every level has been processed.
So I return res.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty tree: returns [] right away.
- One node: the level has size 1, so i = 0 is the last, and I get [value].
- Left-only tree: each level has one node, and that node is the last.
  So I see every node.
- Right-only tree: same thing, every node is visible.
- Left node deeper than the right side: it is the only node at its level,
  so it is the last one, and it shows up.
- Perfect tree: I pick the last node of each level.

For my first example:
- Round 1: the queue is [1], size is 1, so I add 1.
  I add 2 and 3 to the queue.
- Round 2: the queue is [2, 3], size is 2.
  At i = 1, the node is 3, so I add 3.
  I add 5 and 4 to the queue.
- Round 3: the queue is [5, 4], size is 2.
  At i = 1, the node is 4, so I add 4.

The result is [1, 3, 4].

If I'm asked for a version without a queue,
I can do a DFS that visits the right child first.
I track the depth, and the first node I reach at each new depth
is the rightmost one for that level.
That uses recursion, so the space is O(h).

## 9. Complexity

Time: O(n)
- Each node is added to the queue once and removed once.
- Each one does constant work.

Space: O(w), where w is the maximum width of the tree
- The queue holds at most one level at a time.
- The widest level can have about n/2 nodes, so the worst case is O(n).
- The result holds at most h values, one per level.
"""
from collections import deque
class Solution:
    def rightSideBT(self, root):
        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res