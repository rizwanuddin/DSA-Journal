"""
Lowest Common Ancestor of a Binary Search Tree - Medium

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, 
return the lowest common ancestor (LCA) of the two nodes.
The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q 
are descendants. The ancestor is allowed to be a descendant of itself.

Example 1:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5

Example 2:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
Output: 3
Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.



# Lowest Common Ancestor of a Binary Search Tree: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary search tree, and two nodes p and q.
I need to return their lowest common ancestor.
That's the deepest node that has both p and q as descendants.
A node counts as a descendant of itself.

Quick questions:
- Is this a BST, not a general binary tree? I'll assume yes.
  So left values are smaller and right values are bigger.
- Are all values unique? I'll assume yes.
- Are p and q guaranteed to be in the tree? I'll assume yes.
- Can p and q be the same node? I'll assume they are different.
- Can the tree be empty? I'll assume no, since p and q must exist in it.

## 2. Restate

So I'm looking for the lowest node that has both p and q below it.
A node can be its own ancestor.
So if p is above q, the answer is p.

## 3. Example

```
        6
      /   \
     2     8
    / \   / \
   0   4 7   9
      / \
     3   5
```

p = 2 and q = 8.
2 is on the left of 6, and 8 is on the right.
They split at 6, so the answer is 6.

p = 2 and q = 4.
2 is an ancestor of 4, and a node can be its own ancestor.
So the answer is 2.

Edge case: one of the nodes is the root.
Then the answer is the root.

## 4. Brute force

My first idea is to find the path from the root to p.
Then I find the path from the root to q.
Both paths start at the root.
I walk down both paths together, and the last node they share is the answer.

This works because the common ancestors of p and q
are exactly the nodes shared by both paths.
The last shared one is the lowest.

In a BST, I can find each path by using the ordering.
That takes O(h) time per path.
But storing the paths costs O(h) extra space.
On a general binary tree, this would be O(n) time and space.

It's correct, but it does extra work.
It builds two full paths when I only need the point where they split.

## 5. Key observation

The BST ordering already tells me where p and q are.
Compare p and q with the current node:
- If both are smaller, they are both in the left subtree.
- If both are bigger, they are both in the right subtree.
- Otherwise, they are on different sides, or one of them is the current node.

In the third case, this node is the split point.
No lower node can have both of them below it.
So this node is the answer.

I don't need to store any paths.
I just walk down from the root, one step at a time,
and stop at the first node where p and q don't go the same way.

## 6. Approach

Instead of building two paths and comparing them,
I can walk down once and stop at the point where p and q split.

The data structure I will use is just the recursion call stack,
because I only need to move down one side at a time,
and the BST ordering tells me which side.

As I go down the tree, at each node I compare p and q with the node's value.

When both are smaller than the node, I will go left.

When both are bigger than the node, I will go right.

When neither of those is true, I stop.
That means p and q are on different sides, or one of them equals this node.

At the end, I return the current node.

## 7. While coding

First I make a class called Solution.

Then I make a function called lowestCommonAncestor that takes self, root, p, and q.

First, I check if both p and q have values smaller than root.val.
If so, they are both in the left subtree.
So I return the same function called on root.left.
I pass p and q along unchanged, because I'm still looking for the same two nodes.

Next, I check if both p and q have values bigger than root.val.
If so, they are both in the right subtree.
So I return the same function called on root.right.

If neither check was true, I get to the last line.
That means one of three things.
p is smaller and q is bigger, or the reverse.
Or one of them is equal to root.val.
In all of those, this is the split point, so I return root.

I don't need a base case for None.
Since p and q are guaranteed to be in the tree,
I will always stop at a real node before falling off.
If that wasn't guaranteed, I would add a check for None.

## 8. Testing

Before I finish, I want to test the edge cases.
- p and q on different sides of the root: the root is the split, so I return it.
- One node is an ancestor of the other: it hits the equal case,
  because that node's value is neither smaller nor bigger than itself.
  So I return it.
- One node is the root: same thing, the root is returned.
- Both nodes deep in the left subtree: I keep going left until they split.
- Skewed tree: the recursion goes up to n levels deep.

For my example, p = 3 and q = 5.
At 6, both are smaller, so I go left to 2.
At 2, both are bigger, so I go right to 4.
At 4, 3 is smaller and 5 is bigger, so they split here.
I return 4.

If the tree could be very deep, Python's recursion limit is about 1000.
Since I only move in one direction and never need to come back,
I can easily make this a loop with a current pointer.
That removes the stack and gives O(1) space.

If the tree is a general binary tree and not a BST,
this approach doesn't work.
The ordering doesn't tell me where p and q are.
I would use a recursion that searches both sides and checks
where p and q are found.

## 9. Complexity

Time: O(h), where h is the tree height
- I go down one path from the root, and never visit both sides.
- At each node, I do constant work.
- O(log n) if balanced, O(n) if skewed.

Space: O(h)
- Only the call stack, no extra structures.
- O(log n) if balanced, O(n) if skewed.
- With the iterative version, it becomes O(1).
"""
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root