"""
Balanced Binary Tree - Easy

Given a binary tree, return true if it is 
height-balanced and false otherwise.
A height-balanced binary tree is defined as a binary 
tree in which the left and right subtrees of every 
node differ in height by no more than 1.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: true

Example 2:
Input: root = [1,2,3,null,null,4,null,5]
Output: false

Example 3:
Input: root = []
Output: true




# Balanced Binary Tree: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
I need to return True if the tree is height-balanced, otherwise False.
Height-balanced means that at every node,
the left and right subtree heights differ by at most 1.

Quick questions:
- Does the rule apply to every node, or only the root? I'll assume every node.
- Can the tree be empty? I'll assume yes, and treat it as balanced.

## 2. Restate

So I'm checking every node in the tree.
At each node, the left and right heights can't differ by more than 1.
If any node breaks that rule, the answer is False.

## 3. Example

```
    3                 1
   / \               / \
  9  20             2   2
    /  \           / \
   15   7         3   3
                 / \
                4   4
```

The left tree is balanced.
At every node, the two heights differ by 0 or 1.

The right tree is not balanced.
At the root, the left height is 3 and the right height is 1.
The difference is 2, so it fails.

Edge case: an empty tree returns True.

## 4. Brute force

My first idea is to check every node separately.
For each node, I compute the height of its left subtree.
I also compute the height of its right subtree.
If they differ by more than 1, I return False.
Otherwise I move on to check the children.

This works because it checks the rule at every node, one by one.

The problem is the repeated work.
For every node, I recompute heights from scratch.
That is O(n) per node, so O(n^2) in the worst case.
A skewed tree is the worst case.

## 5. Key observation

The repeated work is computing the same subtree heights again and again.
I can compute each height once, from the bottom up.

When I compute a node's height, I already have both child heights.
So I can check the balance rule at that same moment.
No second pass is needed.

At each node, I need two different things:
- The check: is abs(left height - right height) more than 1?
  If yes, the tree is not balanced.
- The height: 1 + the bigger side.
  This is what I return to the parent.

The return value is the height, not the answer.
So I need a separate variable to remember if any node failed.

## 6. Approach

Instead of recomputing heights for every node,
I can compute each height once, bottom-up, and check the rule right away.

The data structure I will use is the recursion call stack,
plus one boolean flag,
because the height is what flows up to the parent,
so I need a separate place to remember a failure.

As I go through the tree, at each node I get the height of the left subtree
and the height of the right subtree.

When the two heights differ by more than 1, I will set the flag to False.

When I'm done with the node, I return its height to the parent:
1 plus the bigger of the two heights.

When I reach None, I return 0.

At the end, I return the flag.

## 7. While coding

First I make a class called Solution.

Then I make a function called balancedBT that takes self and root.

Before anything else, I set condition to True.
I'm assuming the tree is balanced until I find a node that breaks the rule.

Then I define an inner function called helper that takes a node.
It returns the height of the subtree at this node.

Inside helper, I declare condition as nonlocal.
This lets me change the outer variable.
Without it, Python would create a new local variable instead.

First thing after that, I check if node is None, and if so I return 0.
That's my base case.
An empty subtree has height 0, and it stops the recursion.

Then I call helper on node.left and store it as left_height.

Then I call helper on node.right and store it as right_height.

Now I compute the height of the current node.
It's 1 plus the bigger of left_height and right_height.
The 1 counts this node itself.

Then I check the balance rule.
If the absolute difference between left_height and right_height is more than 1,
I set condition to False.

At the end of helper, I return height, so the parent gets this subtree's height.

After defining helper, I call helper on root once.
That kicks off the recursion and lets it run through the whole tree.
I ignore its return value, because the answer lives in condition.

And finally I return condition.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty tree: helper returns 0, condition stays True.
- One node: both heights are 0, the difference is 0, so True.
- Skewed tree with 2 nodes: heights 1 and 0, difference 1, so still True.
- Skewed tree with 3 or more nodes: the top node sees a difference of 2,
  so False. The recursion goes n levels deep.
- Imbalance deep in a subtree: the flag remembers it,
  even if the nodes above look fine.

For my unbalanced example, at the root the left height is 3 and the right is 1.
The difference is 2, so condition becomes False.

One improvement I could mention:
right now, I keep going after I find a failure.
I could stop early by returning -1 as a signal for "unbalanced".
The Big-O stays the same, but it can finish faster.

If the tree could be very deep, Python's recursion limit is about 1000.
In that case I would convert it to an iterative post-order traversal.

## 9. Complexity

Time: O(n)
- Each node is visited once, with constant work per visit.

Space: O(h), where h is the tree height
- Only the call stack, plus one flag.
- O(log n) if balanced, O(n) if skewed.
"""
class Solution:
    def balancedBT(self, root):
        condition = True
        def helper(node):
            nonlocal condition
            if node is None:
                return 0
            left_height = helper(node.left)
            right_height = helper(node.right)
            height = 1 + max(left_height, right_height)
            if abs(left_height - right_height) > 1:
                condition = False
            return height
        helper(root)
        return condition