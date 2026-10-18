"""
Validate Binary Search Tree - Medium

Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
A valid binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [1,2,3]
Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.




# Validate Binary Search Tree: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
I need to return True if it's a valid binary search tree, otherwise False.

A valid BST means, for every node:
- All values in its left subtree are smaller than the node.
- All values in its right subtree are bigger than the node.
- This must hold for the whole subtree, not just the direct children.

Quick questions:
- Are duplicates allowed? I'll assume no, so the inequalities are strict.
- Can the tree be empty? I'll assume yes, and treat it as valid.
- Can values be negative? I'll assume yes.

## 2. Restate

So I'm checking that every node respects the BST rule
against everything above it, not only its parent.
If any node breaks the rule, the answer is False.

## 3. Example

```
    2
   / \
  1   3
```

Valid. 1 is smaller than 2, and 3 is bigger than 2.

```
    5
   / \
  1   4
     / \
    3   6
```

Not valid.
4 is in the right subtree of 5, but 4 is smaller than 5.

A trickier one:

```
    5
   / \
  4   6
     / \
    3   7
```

Not valid.
The 3 is smaller than its parent 6, which is fine.
But it sits in the right subtree of 5, and it's smaller than 5.
So checking only the parent is not enough.

Edge case: an empty tree returns True.

## 4. Brute force

My first idea is to check every node against its whole subtrees.
For each node, I look at every value in its left subtree
and make sure they are all smaller.
I look at every value in its right subtree
and make sure they are all bigger.
Then I repeat this for every node.

This works because it follows the definition exactly.

The problem is the repeated work.
Each node scans its entire subtree.
Deep nodes get scanned again by every ancestor above them.
That is O(n) per node, so O(n^2) in the worst case.
A skewed tree is the worst case.

## 5. Key observation

The repeated work is rescanning the same subtrees from every ancestor.
I can avoid it by flipping the question.

Instead of asking, "what is below me?",
I ask, "what range am I allowed to be in?"

Every node has a lower bound and an upper bound.
The bounds come from the ancestors above it.

- When I go to the left child, the upper bound becomes the current node's value.
  The lower bound stays the same.
- When I go to the right child, the lower bound becomes the current node's value.
  The upper bound stays the same.

So I carry the bounds down as I go.
At each node, I only check one thing:
is my value strictly between the lower and the upper bound?

This is one pass, so it's O(n).

## 6. Approach

Instead of scanning the subtrees of every node,
I can pass a valid range down the tree, and check each node once.

The data structure I will use is the recursion call stack,
because each call needs to remember its own range,
and the range changes depending on which side I go to.

As I go down the tree, at each node I check
that its value is strictly between the lower and the upper bound.

When the value is outside the range, I will return False right away.

When it's inside the range, I will check the left child
with the upper bound set to this node's value,
and the right child with the lower bound set to this node's value.

When I reach None, I will return True, because an empty tree has nothing to break.

At the end, I return True only if both sides are valid.

## 7. While coding

First I make a class called Solution.

Then I make a function called validBST that takes self and root.

Inside it, I define an inner function called isValid.
It takes a node, a left bound, and a right bound.
The left bound is the smallest value this node is allowed to be, exclusive.
The right bound is the biggest value this node is allowed to be, exclusive.

First thing inside isValid, I check if node is None, and if so I return True.
That's my base case.
An empty subtree can't break the rule, and it stops the recursion.

Then I check the range.
If it's not true that left is less than node.val and node.val is less than right,
I return False.
I'm using strict less than on both sides,
because duplicates are not allowed.

If the node passed, I check its children.
I return isValid on node.left, and isValid on node.right.
I'm using and, because both sides have to be valid.

For the left child, I pass left as the lower bound, and node.val as the upper bound.
Everything on the left must be smaller than this node.

For the right child, I pass node.val as the lower bound, and right as the upper bound.
Everything on the right must be bigger than this node.

After defining isValid, I call it on root.
I start with negative infinity as the lower bound, and infinity as the upper bound.
That means the root can be any value.
I'm not using something like 0 or a max integer,
because values can be negative, and they can be very large.
Infinity is safe for every value.

And I return that result.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty tree: returns True.
- One node: it's inside negative infinity and infinity, so True.
- Duplicate values, like 2 with a left child of 2: the check is strict,
  so 2 is not less than 2, and it returns False.
- A node that breaks the rule because of a grandparent, not its parent:
  the bounds carry the grandparent's value down, so I catch it.
- Very large or very small values: infinity handles them.
- Skewed tree: the recursion goes n levels deep.

For my tricky example:
- At 5, the range is (-inf, inf). Valid.
- At 6, the range is (5, inf). Valid.
- At 3, the range is (5, 6), and 3 is not bigger than 5. Returns False.

If the tree could be very deep, Python's recursion limit is about 1000.
In that case, I would use an iterative in-order traversal.
In a valid BST, in-order gives strictly increasing values.
I'd check that each value is bigger than the previous one.

## 9. Complexity

Time: O(n)
- Each node is visited once, with constant work per visit.
- It can stop early when it finds a bad node.

Space: O(h), where h is the tree height
- Only the call stack, no extra structures.
- O(log n) if balanced, O(n) if skewed.
"""
class Solution:
    def validBST(self, root):
        def isValid(node, left, right):
            if node is None:
                return True
            if not (left < node.val < right):
                return False
            return (isValid(node.left, left, node.val) and isValid(node.right, node.val, right))
        return isValid(root, float("-inf"), float("inf"))
