"""
Level Order Traversal

Given the root of a binary tree, return the level order traversal of its 
nodes' values. (i.e., from left to right, level by level).

Example 1:
Input : root = [3, 9, 20, null, null, 15, 7]
Output : [ [3] , [9, 20] , [15, 7] ]

Example 2:
Input : root = [1, 4, null, 4 2]
Output : [ [1] , [4] , [4, 2] ]




## Binary Tree Level Order Traversal

**Clarify:**
- given the root of a binary tree, return the values level by level, top to bottom, left to right within each level
- output is a list of lists, one inner list per level

**Brute force:**
- not really a brute force case here, BFS using a queue is just the natural way to process level by level
- I guess I could do it recursively tracking depth and appending to the right sublist, but that's a different approach, not really a slower brute force

**Optimize:**
- this needs a queue, not a stack, because I want to process nodes in the order I discovered them, first in first out
- that's exactly what deque gives me, and it's O(n) overall since every node gets visited once

**Key observation:**
- the tricky part is separating nodes level by level, not just getting one big flat list
- I do that by grabbing the queue's current size BEFORE I start popping for this level, since that size tells me exactly how many nodes belong to the current level
- while processing those nodes, I add their children to the queue, but those children belong to the NEXT level, so they won't get touched until the next while loop iteration

**Approach:**
- if root is None, return an empty list right away
- start a queue with just the root in it
- while the queue isn't empty:
  - grab the current queue size, that's how many nodes are in this level
  - loop exactly that many times, popping from the front, appending the value to this level's list, and pushing any children onto the queue
  - once that loop finishes, append the completed level list to the result
- return result

**While coding:**
- first I import deque from collections
- I define the function levelOrder, taking root
- first thing, I check if root is None, if so I return an empty list
- I create queue as a deque containing just root
- I create an empty list called result
- I start a while loop that runs while queue is not empty
- inside, I create an empty list called level
- I grab level_size as the current length of the queue, this is important, I capture it BEFORE adding any new nodes
- I loop using range of level_size
- inside that inner loop, I pop from the front of the queue using popleft, and call it node
- I append node.val to level
- I check if node.left exists, if so I add it to the queue
- I check if node.right exists, if so I add it to the queue
- once the inner loop finishes, I append level to result
- after the while loop ends, I return result

**Edge cases:**
- if root is None, I return an empty list immediately, no traversal happens
- if there's only one node, result ends up being a single list containing just that one value
- if the tree is completely unbalanced, like a straight line, each level just naturally ends up with one node in it, still works fine

**Complexity:**
- time is O(n), every node gets added to the queue and popped exactly once
- space is O(n) in the worst case, since the last level of a wide tree could hold up to n/2 nodes in the queue at once, plus result holds every node's value overall
"""
from collections import deque
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result