"""
Diameter of Binary Tree - Easy
The diameter of a binary tree is defined as the length of the longest path 
between any two nodes within the tree. The path does not necessarily have 
to pass through the root.
The length of a path between two nodes in a binary tree is the number of 
edges between the nodes. Note that the path can not include the same node 
twice.
Given the root of a binary tree root, return the diameter of the tree.

Example 1:
Input: root = [1,null,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:
Input: root = [1,2,3]
Output: 2





# Diameter of Binary Tree: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
I need to return its diameter.
That's the length of the longest path between any two nodes.

Quick questions:
- Do I measure length in edges or in nodes? I'll assume edges.
- Does the path have to pass through the root? I'll assume no.
- Can the tree be empty? I'll assume it can, and return 0.

## 2. Restate

So I'm finding the longest path between any two nodes.
The path can be anywhere in the tree.
I count its length in edges.

## 3. Example

```
      1
     / \
    2   3
   / \
  4   5
```

The longest path is 4 -> 2 -> 1 -> 3.
It has 3 edges, so the answer is 3.
5 -> 2 -> 1 -> 3 also has 3 edges.

The longest path doesn't always go through the root.
A big subtree on one side can hold a longer path on its own.

Edge case: an empty tree or a single node returns 0.

## 4. Brute force

My first idea is to treat every node as the top of a path.
For each node, I compute the height of its left subtree.
I also compute the height of its right subtree.
The longest path that bends at this node is left height + right height.
Then I take the max over all nodes.

This works because every path has exactly one highest node.
So trying every node as the top covers every path.

The problem is the repeated work.
For every node, I recompute heights from scratch.
That is O(n) per node, so O(n^2) in the worst case.
A skewed tree is the worst case.

## 5. Key observation

The repeated work is computing the height of the same subtrees again and again.
I can compute each height once, from the bottom up.

At each node, I already have the left height and the right height.
So I can check the path that bends at this node at the same time.
No second pass is needed.

At each node, I need two different things:
- The path that bends here, which is left height + right height.
  This is a candidate for the answer.
  It can't go up to the parent, because that would fork the path.
- The height of this node, which is 1 + the bigger side.
  This is what I return to the parent.

So the answer is not the return value.
I need a separate variable to remember the best candidate seen anywhere.

## 6. Approach

Instead of recomputing heights for every node,
I can compute each height once, bottom-up, and use it right away.

The data structure I will use is the recursion call stack,
plus one variable for the best diameter so far,
because the longest path may not pass through the root,
so I need to remember the best one I see anywhere.

As I go through the tree, at each node I get the height of the left subtree
and the height of the right subtree.

When I have both heights, I will check the path through this node,
which is left height + right height,
and update my best if it's bigger.

When I'm done with the node, I return its height to the parent:
1 plus the bigger of the two heights.

When I reach None, I return 0.

At the end, I return the best diameter I tracked.

## 7. While coding

First I make a class called Solution.

Then I make a function called diameter that takes self and root.

Before anything else, I set self.best to 0.
Starting at 0 is fine, because a path length can never be negative.
I'm using self so the inner function can update it.

Then I define an inner function called height that takes a node.
It returns the height of the subtree at this node.

First thing inside height, I check if node is None, and if so I return 0.
That's my base case.
An empty subtree has height 0, and it stops the recursion.

Then I call height on node.left and store it as left_height.

Then I call height on node.right and store it as right_height.

Now I check the longest path that bends at this node.
That path goes down the left side, then down the right side.
Its length in edges is left_height + right_height.
I update self.best with the bigger of the old value and this one.

At the end of height, I return 1 plus the bigger of left_height and right_height.
The 1 counts this node.
I return only the taller side, because the parent can only continue down one branch.

After defining height, I call height on root once.
That kicks off the recursion and lets it run through the whole tree.
I ignore its return value, because the answer lives in self.best.

And finally I return self.best.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty tree: height returns 0, best stays 0, so the answer is 0.
- One node: both heights are 0, so the answer is 0.
- Skewed tree: one side is always 0, so the answer is n - 1 edges,
  and the recursion goes n levels deep.
- Longest path not through the root: self.best remembers it from the lower node.

For my example, at node 2 the heights are 1 and 1, so the candidate is 2.
At the root, the heights are 2 and 1, so the candidate is 3.
3 is the answer.

If the tree could be very deep, Python's recursion limit is about 1000.
In that case I would convert it to an iterative post-order traversal.

## 9. Complexity

Time: O(n)
- Each node is visited once, with constant work per visit.

Space: O(h), where h is the tree height
- Only the call stack, plus one variable.
- O(log n) if balanced, O(n) if skewed.
"""
class Solution:
    def diameter(self, root):
        self.best = 0
        def height(node):
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            self.best = max(self.best, left_height + right_height)
            return 1 + max(left_height, right_height)
        height(root)
        return self.best