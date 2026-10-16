"""
Binary Tree Level Order Traversal - Medium

Given a binary tree root, return the level order traversal of it as a nested list, where each sublist 
contains the values of nodes at a particular level in the tree, from left to right.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []




# Binary Tree Level Order Traversal: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
I need to return its values grouped by level.
The levels go from top to bottom.
Inside each level, the values go from left to right.

Quick questions:
- Do I return a list of lists, one list per level? I'll assume yes.
- Can the tree be empty? I'll assume yes, and return an empty list.
- Can values be negative or repeated? I'll assume yes.
  It doesn't matter, because I never compare values.

## 2. Restate

So I'm visiting the tree one level at a time.
I collect the values of each level into its own list.
Then I return all the levels in one list.

## 3. Example

```
    3
   / \
  9  20
    /  \
   15   7
```

Level 0 is [3].
Level 1 is [9, 20].
Level 2 is [15, 7].
The answer is [[3], [9, 20], [15, 7]].

Edge case: an empty tree returns [].

## 4. Brute force

My first idea is to handle one level at a time on its own.
For level 0, I walk the whole tree and collect nodes at depth 0.
For level 1, I walk the whole tree again and collect nodes at depth 1.
I keep going until a level comes back empty.

This works because it visits every level, from left to right.

The problem is the repeated work.
Each level walks the whole tree again.
With h levels, that is O(n * h).
A skewed tree is the worst case, which gives O(n^2).

## 5. Key observation

The repeated work is walking down from the root again for every level.
I don't need to do that.
If I already have all the nodes of one level,
their children are exactly the nodes of the next level.

So I can move level by level, and remember the current level in a queue.

A queue is the right structure because it is first in, first out.
Nodes that were added earlier come out earlier.
So the order stays top to bottom, and left to right.

The next problem is knowing where one level ends and the next begins.
The trick is the queue's size at the start of each round.
At that moment, the queue holds only the current level.
So I process exactly that many nodes, and the children I add
belong to the next round.

## 6. Approach

Instead of walking from the root again for every level,
I can process one level at a time and collect the next level as I go.

The data structure I will use is a queue,
because it gives me first-in, first-out order,
so I visit nodes level by level, from left to right.

As I go through the tree, I will take the queue's current size.
That tells me how many nodes are in this level.

When I take a node out, I will add its value to the current level's list,
and add its left and right children to the queue, if they exist.

When I've processed that many nodes, I will add the level's list to the result.

When the queue is empty, there are no more levels.

At the end, I return the result.

## 7. While coding

First I import deque from collections.
I'm using a deque as the queue, because removing from the front is O(1).
With a regular list, pop(0) is O(n), because everything shifts.

Then I make a class called Solution.

Then I make a function called levelOrderBT that takes self and root.

Before anything else, I check if root is None, and if so I return an empty list.
That handles the empty tree.
It also protects me from putting None into the queue.

Then I create the queue, starting with just the root.
This is level 0.

Then I create an empty list called result.
This will hold one list per level.

Now I start a while loop that runs as long as the queue isn't empty.
Each round of this loop handles one full level.

At the start of each round, I make an empty list called level.
This will hold the values of this level.

Then I store the current length of the queue in lev_length.
I do this before touching the queue.
Right now, the queue holds only this level.
If I checked the length during the loop, the children I add
would change it, and levels would get mixed up.

Then I loop lev_length times, using a for loop.
This processes exactly the nodes of this level.

Inside it, I take the node from the front of the queue with popleft.

Then I add its value to the level list.

Then I check if node.left exists, and if so I add it to the queue.
Same for node.right.
I check for existence first, so I never add None to the queue.
These children go to the back, so they wait until the next round.

When the for loop is done, the level list is complete.
I add it to the result.

When the while loop ends, every level has been processed.
So I return result.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty tree: returns [] right away.
- One node: the queue has 1 node, so I get [[value]].
- Skewed tree: every level has one node, so I get n lists with one value each.
- Perfect tree: the queue holds up to about n/2 nodes at the last level.
- Missing children: the if checks skip them, so no None enters the queue.
- Negative or repeated values: no issue, I never compare values.

For my example:
- Round 1: the queue is [3], the length is 1, so level = [3].
  I add 9 and 20 to the queue.
- Round 2: the queue is [9, 20], the length is 2, so level = [9, 20].
  I add 15 and 7 to the queue.
- Round 3: the queue is [15, 7], the length is 2, so level = [15, 7].
  They have no children, so the queue ends up empty.

The result is [[3], [9, 20], [15, 7]].

## 9. Complexity

Time: O(n)
- Each node is added to the queue once and removed once.
- Each one does constant work.

Space: O(n)
- The queue holds at most one level at a time.
- The widest level can have about n/2 nodes.
- The result also holds all n values.
- If I ignore the result, the extra space is O(w), where w is the max width.
"""
from collections import deque
class Solution:
    def levelOrderBT(self, root):
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            lev_length = len(queue)
            for i in range(lev_length):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result