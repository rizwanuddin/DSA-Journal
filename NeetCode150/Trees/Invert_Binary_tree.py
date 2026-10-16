"""
Invert Binary Tree - Easy

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []




# Invert Binary Tree: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
I need to swap the left and right child at every node.
Then I return the root.

Quick questions:
- Can I modify the tree in place? I'll assume yes.
- Can the tree be empty? I'll assume yes, and return None.

## 2. Restate

So I'm mirroring the tree.
Every node gets its two children swapped.

## 3. Example

```
    4              4
   / \            / \
  2   7    ->    7   2
 / \ / \        / \ / \
1  3 6  9      9  6 3  1
```

The swap happens at every level, not just the top.
Edge case: an empty tree returns None.

## 4. Brute force

There isn't a slower version worth trying.
I have to swap children at every node, so I must visit all n nodes.
That makes O(n) the best possible.
The natural recursive solution already gets that.

## 5. Key observation

The mirror of a tree is made of smaller mirrors.
Keep the root, mirror both subtrees, then swap them.
That is the same problem on smaller trees, so recursion fits.

There is one trap.
If I assign root.left first, I overwrite the original left.
So I save both results in variables before assigning.

## 6. Approach

Instead of thinking about the whole tree at once,
I can solve it for one node and trust recursion for the subtrees.

The data structure I will use is the recursion call stack,
because every subtree is just a smaller tree of the same shape.

As I go through the tree, I will invert the left subtree
and the right subtree, and save both results.

When both results are saved,
I will put the inverted right on the left
and the inverted left on the right.

When I reach None, I will return None.
That is my base case.

At the end, I return root.

## 7. While coding

First I make a class called Solution.

Then I make a function called invertTree that takes self and root.

Before anything else, I check if root is None, and if so I return None right away.
That's my base case, and it also handles an empty tree.

Then I call invertTree on root.left and store the result as left.
This gives me the fully inverted left subtree.

Then I do the same on root.right and store it as right.

I'm saving both results in variables on purpose.
If I assigned root.left right away, I would lose the original left before using it.

Now I set root.left equal to right.

And I set root.right equal to left.
Together these two lines are the swap.

At the very end I return root, so the parent call gets this node back.
The first call returns the final answer.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty tree: returns None.
- One node: both children are None, so the swap does nothing.
- Skewed tree: everything moves to the other side, recursion depth is n.

If the tree could be very deep, Python's recursion limit is about 1000.
In that case I would switch to an iterative BFS with a queue.

## 9. Complexity

Time: O(n)
- Each node is visited once, with constant work per visit.

Space: O(h), where h is the tree height
- Only the call stack, no extra structures.
- O(log n) if balanced, O(n) if skewed.
"""
class Solution:
    def invertBinarytree(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root  #this already is handled by recursion but meh just do it
        left = self.invertBinarytree(root.left)
        right = self.invertBinaryTree(root.right)
        
        root.left = right
        root.right = left
        return root 
