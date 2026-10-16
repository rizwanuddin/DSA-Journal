"""
Binary Tree Maximum Path Sum - Hard

Given the root of a non-empty binary tree, return the maximum path sum of 
any non-empty path.
A path in a binary tree is a sequence of nodes where each pair of adjacent
 nodes has an edge connecting them. A node can not appear in the sequence 
 more than once. The path does not necessarily need to include the root.
The path sum of a path is the sum of the node's values in the path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40





# Binary Tree Maximum Path Sum: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
Each node has a value, and values can be negative.
I need to return the maximum sum of any path in the tree.

Quick questions:
- Does the path have to pass through the root? I'll assume no.
- Can the path start and end at any node? I'll assume yes.
- Can a node appear twice in a path? I'll assume no.
- Does the path need at least one node? I'll assume yes.
- Can the tree be empty? I'll assume no, at least one node.

## 2. Restate

So I'm looking for the best path anywhere in the tree.
It can start and end at any node.
It follows parent-child edges and never reuses a node.
I return the biggest sum.

## 3. Example

```
   -10
   /  \
  9    20
      /  \
     15   7
```

The best path is 15 -> 20 -> 7.
The sum is 42.
It doesn't pass through the root.

Edge case: a single node with value -3.
The path must have at least one node, so the answer is -3.

## 4. Brute force

My first idea is to treat every node as the top of a path.
For each node, I find the best downward sum on its left.
I also find the best downward sum on its right.
Then I combine them with the node's value.

This works because every path has exactly one highest node.
So trying every node as the top covers all paths.

The problem is the repeated work.
For every node, I recompute the downward sums from scratch.
That is O(n) per node, so O(n^2) in the worst case.
A skewed tree is the worst case.

## 5. Key observation

The repeated work is the best downward sum from each node.
I can compute it once, from the bottom up, and hand it to the parent.

At each node, I need two different numbers:
- The best path that bends at this node, using both sides.
  This is a candidate for the answer.
  It can't go up to the parent, because that would fork the path.
- The best path going down one side only.
  This is what I return to the parent.
  The parent can extend only one branch.

Also, if a child's sum is negative, I should skip that branch.
Taking 0 instead means "don't go that way".

So the answer is not the return value.
I need a separate variable to track the best candidate seen anywhere.

## 6. Approach

Instead of recomputing downward sums for every node,
I can compute each one once, bottom-up, and return it to the parent.

The data structure I will use is the recursion call stack,
plus one variable for the best sum so far,
because the best path may not pass through the root,
so I need to remember the best one I see anywhere.

As I go through the tree, at each node I get the best downward sum
from the left and from the right.
If one is negative, I use 0 instead.

When I have both sides, I will check the path using both sides,
and update my best sum if it's bigger.

When I'm done with the node, I return only one side to the parent:
the node's value plus the bigger of the two sides.

When I reach None, I return 0.

At the end, I return the best sum I tracked.

## 7. While coding

First I make a class called Solution.

Then I make a function called maxPathSum that takes self and root.

Before anything else, I set self.maxsum to negative infinity.
I'm not starting at 0, because values can be negative.
If every node is negative, starting at 0 would give a wrong answer.
I'm using self so the helper can update it.

Then I define an inner function called helper that takes a node.
It returns the best sum of a path going down from this node, one side only.

First thing inside helper, I check if node is None, and if so I return 0.
That's my base case.
A missing child adds nothing to the sum.

Then I call helper on node.left, and take the max of that and 0.
I store it as left_sum.
The max with 0 is how I skip a negative branch.

Then I do the same on node.right and store it as right_sum.

Now I check the path that bends at this node.
That path uses left_sum, plus right_sum, plus node.val.
I update self.maxsum with the bigger of the old value and this one.

And at the end of helper, I return node.val plus the bigger of left_sum and right_sum.
I return only one side, because the parent can only continue down one branch.
If I returned both, the path would fork, and that's not a valid path.

After defining helper, I call helper on root once.
That kicks off the recursion and lets it run through the whole tree.
I ignore its return value, because the answer lives in self.maxsum.

And finally I return self.maxsum.

## 8. Testing

Before I finish, I want to test the edge cases.
- One positive node: both sides are 0, so the answer is node.val.
- One negative node: both sides are 0, the candidate is node.val, and
  since maxsum starts at negative infinity, the answer is that negative value.
- All negative values: every branch is skipped, so the answer is the
  single largest node.
- Best path not through the root: maxsum remembers it from the lower node.
- Skewed tree: everything goes through one side, and recursion depth is n.

For my example, node 20 gives 15 + 7 + 20 = 42.
It returns 35 to the root.
At the root, left_sum is 9, right_sum is 35, so the candidate is 34.
42 stays the answer.

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
    def maxPathsum(self, root):

        self.maxsum = float("-inf")

        def helper(node):

            if node is None:
                return 0

            left_sum = max(0, helper(node.left))
            right_sum = max(0, helper(node.right))

            # Check path using BOTH sides
            self.maxsum = max(
                self.maxsum,
                left_sum + right_sum + node.val
            )

            # Return only ONE side to parent
            return node.val + max(left_sum, right_sum)

        helper(root)

        return self.maxsum