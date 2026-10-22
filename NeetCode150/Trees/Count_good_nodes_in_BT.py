"""
Count Good Nodes In Binary Tree - Medium

Within a binary tree, a node x is considered good if the path from the root of the tree 
to the node x contains no nodes with a value greater than the value of node x
Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:
Input: root = [2,1,1,3,null,1,5]
Output: 3

Example 2:
Input: root = [1,2,-1,3,4]
Output: 4




# Count Good Nodes in Binary Tree: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary tree.
A node X is "good" if, on the path from the root down to X,
no node has a value bigger than X.
I need to return how many good nodes there are.

Quick questions:
- Does the root count? I'll assume yes, since nothing is above it.
- If a node is equal to the biggest value so far, is it good?
  I'll assume yes, because no node on the path is bigger.
- Can values be negative or repeated? I'll assume yes.
- Can the tree be empty? I'll assume no, but I'll handle None anyway.

## 2. Restate

So for every node, I look at the path from the root down to it.
If it's at least as big as everything on that path, it's good.
I count all the good nodes.

## 3. Example

```
      3
     / \
    1   4
   /   / \
  3   1   5
```

- 3 (root): always good.
- 1 (left of root): the path is 3, 1. The 3 is bigger, so not good.
- 3 (under the 1): the path is 3, 1, 3. Nothing is bigger than 3, so good.
- 4: the path is 3, 4. Nothing is bigger, so good.
- 1 (under the 4): the path is 3, 4, 1. Not good.
- 5: the path is 3, 4, 5. Nothing is bigger, so good.

The answer is 4.

Edge case: a path that only goes down, like 5, 4, 3.
Only the root is good.

## 4. Brute force

My first idea is to check every node separately.
For each node, I find the path from the root down to it.
Then I take the max of that path, and compare it with the node's value.
If the node is at least as big, I count it.

This works because it follows the definition exactly.

The problem is the repeated work.
Nodes that share the same top part of a path
make me recompute the same max again and again.
Each path can be up to h long, so the cost is O(n * h).
A skewed tree is the worst case, which gives O(n^2).

## 5. Key observation

The repeated work is recomputing the max of the same path from the top.
I don't need to.
When I'm at a node, the max of the path above it is already known
by the parent.

So I can carry that max down with me as I go.
At each node, I compare the node with that max.
Then I pass down the updated max to its children.

The nice part is that each branch gets its own copy of the max.
So the left side and the right side don't affect each other.
Each path is judged only by the nodes above it.

This needs one pass, so it's O(n).

## 6. Approach

Instead of recomputing the max of the path for every node,
I can carry the max seen so far down the tree as I go.

The data structure I will use is the recursion call stack,
plus one counter,
because each call needs to remember its own max for its own path,
and the counter collects the answer across all calls.

As I go down the tree, at each node I compare its value with the max seen so far.

When the node's value is greater than or equal to the max,
I will count it as good.

After that, I will update the max to include this node,
and pass the new max to the left and right children.

When I reach None, I will just return.

At the end, I return the counter.

## 7. While coding

First I make a class called Solution.

Then I make a function called goodNodes that takes self and root.

Before anything else, I set good_count to 0.
This will hold the number of good nodes I've found so far.

Then I define an inner function called helper that takes a node and max_seen.
max_seen is the biggest value on the path from the root down to the parent.

Inside helper, I declare good_count as nonlocal.
This lets me change the outer variable.
Without it, Python would create a new local variable instead.

First thing after that, I check if node is None, and if so I return.
That's my base case.
There is nothing to count, and it stops the recursion.

Then I check if node.val is greater than or equal to max_seen.
I'm comparing the value, not the node itself.
And I'm using greater than or equal,
because a node that ties the max is still good.
No node on its path is bigger.
If it passes, I add 1 to good_count.

Then I update max_seen to the bigger of max_seen and node.val.
This is the max for the path that includes this node.
The children need this updated value, not the old one.

Then I call helper on node.left, passing the updated max_seen.

And I call helper on node.right, passing the same max_seen.
Each call gets its own copy, so the two sides don't affect each other.

After defining helper, I call it on root, with negative infinity as the starting max.
I'm using negative infinity so the root is always counted as good.
Any value is bigger than it.
I'm not using 0, because values can be negative.

And finally I return good_count.

## 8. Testing

Before I finish, I want to test the edge cases.
- One node: the root is compared with negative infinity, so it's good.
  The answer is 1.
- Equal values, like 3 then 3: the second one is greater than or equal
  to the max, so it counts.
- All negative values: starting at negative infinity handles it.
  Starting at 0 would wrongly skip them.
- Decreasing path, like 5, 4, 3: only the root is good.
- Increasing path, like 1, 2, 3: every node is good.
- Skewed tree: the recursion goes n levels deep.

For my example, the counter goes 1 at the root,
skips the 1 under the root,
reaches 2 at the 3 under it, then 3 at the 4, then skips the 1 under the 4,
and ends at 4 after the 5.

If the tree could be very deep, Python's recursion limit is about 1000.
In that case I would use an iterative DFS with a stack,
where each stack item holds a node and the max for its path.

## 9. Complexity

Time: O(n)
- Each node is visited once, with constant work per visit.

Space: O(h), where h is the tree height
- Only the call stack, plus one counter.
- O(log n) if balanced, O(n) if skewed.

"""
class Solution:
    def goodNodes(self, root):
        good_count = 0
        def helper(node, max_seen):
            nonlocal good_count
            if node is None:
                return 
            if node.val >= max_seen:
                good_count += 1
            max_seen = max(max_seen, node.val)
            helper(node.left, max_seen)
            helper(node.right, max_seen)
            
        helper(root, float("-inf"))
        return good_count