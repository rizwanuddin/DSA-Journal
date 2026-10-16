"""
Maximum Depth of Binary Tree - Easy

Given the root of a binary tree, return its depth.
The depth of a binary tree is defined as the number 
of nodes along the longest path from the root node 
down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: 3

Example 2:
Input: root = []
Output: 0



# Maximum Depth of Binary Tree: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
I need to return its maximum depth.
That's the number of nodes on the longest path from the root down to a leaf.

Quick questions:
- Do I count depth in nodes or in edges? I'll assume nodes.
- Can the tree be empty? I'll assume yes, and return 0.

## 2. Restate

So I'm finding the height of the tree.
I need the length of the longest root-to-leaf path, counted in nodes.

## 3. Example

```
    3
   / \
  9  20
    /  \
   15   7
```

The longest path is 3 -> 20 -> 15, which has 3 nodes.
So the answer is 3.

Edge case: an empty tree returns 0.

## 4. Brute force

There isn't a slower version worth trying.
Any answer has to look at every node, because a deep leaf could be anywhere.
So O(n) is the best possible.
The natural recursive solution already gets that.

## 5. Key observation

The depth of a tree depends only on its two subtrees.
It's one for the current node, plus whichever subtree is deeper.
Each subtree is the same problem, just smaller.
So recursion fits.

## 6. Approach

Instead of searching for the longest path directly,
I can ask each subtree how deep it is, and add one.

The data structure I will use is the recursion call stack,
because every subtree is just a smaller tree of the same shape.

As I go through the tree, I will ask the left subtree for its depth
and the right subtree for its depth.

When I reach None, I will return 0.
That's my base case.

At each node, I take the bigger of the two depths and add 1 for this node.

At the end, I return the depth that comes back for the root.

## 7. While coding

First I make a class called Solution.

Then I make a function called maxDepth that takes self and root.

Inside it, I define a helper function that takes a node.
This does the actual recursion.

First thing in the helper, I check if node is None, and if so I return 0.
That's my base case.
An empty tree has depth 0, and it also stops the recursion.

Then I call helper on node.left and store it as depth_left.
This is how deep the left subtree is.

Then I call helper on node.right and store it as depth_right.
This is how deep the right subtree is.

Now I compute the depth of the current node.
I take the max of depth_left and depth_right, because I want the longer path.
Then I add 1 to count this node itself.

I return that depth, so the parent call gets this subtree's depth.

After defining the helper, I return helper called on root.
That starts the recursion, and its result is the final answer.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty tree: returns 0.
- One node: both children return 0, so the depth is 1 + 0 = 1.
- Skewed tree: depth is n, and the recursion goes n levels deep.
- Unbalanced tree: max picks the deeper side, so the shorter side is ignored.

If the tree could be very deep, Python's recursion limit is about 1000.
In that case I would use an iterative BFS with a queue,
and count the levels.

## 9. Complexity

Time: O(n)
- Each node is visited once, with constant work per visit.

Space: O(h), where h is the tree height
- Only the call stack, no extra structures.
- O(log n) if balanced, O(n) if skewed.
"""
class Solution:
    def maxDepth(self, root):

        def helper(node):

            if node is None:
                return 0

            depth_left = helper(node.left)
            depth_right = helper(node.right)

            depth = 1 + max(depth_left, depth_right)

            return depth

        return helper(root)

"""
Call Stack Tree

helper(3)
│
├── helper(9)
│   │
│   ├── helper(None) → 0
│   └── helper(None) → 0
│
│   left  = 0
│   right = 0
│   1 + max(0, 0) = 1
│   → return 1
│
└── helper(20)
    │
    ├── helper(15)
    │   │
    │   ├── helper(None) → 0
    │   └── helper(None) → 0
    │
    │   left  = 0
    │   right = 0
    │   1 + max(0, 0) = 1
    │   → return 1
    │
    └── helper(7)
        │
        ├── helper(None) → 0
        └── helper(None) → 0

        left  = 0
        right = 0
        1 + max(0, 0) = 1
        → return 1

    BACK AT 20:

    left  = 1    ← returned by 15
    right = 1    ← returned by 7

    1 + max(1, 1) = 2
    → return 2


BACK AT 3:

left  = 1    ← returned by 9
right = 2    ← returned by 20

1 + max(1, 2) = 3

→ return 3
"""