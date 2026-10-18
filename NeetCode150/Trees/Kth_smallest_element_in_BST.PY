"""
Kth Smallest Element In a Bst - Medium

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
A binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3], k = 1
Output: 1

Example 2:
Input: root = [4,3,5,2,null], k = 4
Output: 5




# Kth Smallest Element in a BST: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given the root of a binary search tree and an integer k.
I need to return the kth smallest value in the tree.

Quick questions:
- Is k 1-indexed? I'll assume yes, so k = 1 means the smallest.
- Is k always valid, between 1 and the number of nodes? I'll assume yes.
- Can the tree be empty? I'll assume no, because k must be valid.
- Can values be negative or zero? I'll assume yes.

## 2. Restate

So I'm looking for the kth value if I sorted all the nodes.
Since it's a BST, I want to use its ordering instead of sorting.

## 3. Example

```
    3
   / \
  1   4
   \
    2
```

Sorted order is 1, 2, 3, 4.
k = 1 returns 1.
k = 3 returns 3.

Edge case: a single node with k = 1 returns that node's value.

## 4. Brute force

My first idea is to collect every value in a list.
Then I sort the list, and return the element at index k - 1.

This works because sorting puts the values in order.
It costs O(n log n) time and O(n) space.

I can do a bit better by using the BST.
An in-order traversal already gives sorted values.
So I can collect them in order and skip the sort.
That is O(n) time and O(n) space.

It's still wasteful.
I build the whole list, even if k is 1 and I only need the first value.

## 5. Key observation

An in-order traversal of a BST visits nodes in increasing order.
Left subtree first, then the node, then the right subtree.

So the kth node I visit is the kth smallest.

I don't need to store the values.
I only need a counter that counts nodes as I visit them.
When the counter reaches k, I have my answer.

Once I have the answer, I can stop.
I don't need to visit the rest of the tree.

That changes the cost.
I walk down to the leftmost node, which takes h steps.
Then I visit k nodes.
So it's O(h + k), not always O(n).

## 6. Approach

Instead of collecting and sorting all the values,
I can walk the tree in order and count, then stop at the kth node.

The data structure I will use is the recursion call stack,
plus a counter and a result variable,
because the in-order traversal needs to go down and come back up,
and the counter tells me when I've reached the kth node.

As I go through the tree, I will visit the left subtree first.

When I come back from the left, I will count the current node.

When the count equals k, I will save this node's value and stop.

After that, I will skip the right subtree, and every other node,
because the answer is already found.

When I reach None, I will just return.

At the end, I return the result.

## 7. While coding

First I make a class called Solution.

Then I make a function called kSmallestBST that takes self, root, and k.

Before anything else, I set count to 0.
This counts how many nodes I've visited in sorted order.

Then I set result to None.
This will hold the answer once I find it.
I'm using None as "not found yet", because 0 can be a valid node value.

Then I define an inner function called helper that takes a node.
It does the in-order traversal.

Inside helper, I declare count and result as nonlocal.
This lets me change the outer variables.
Without it, Python would create new local variables instead.

First thing after that, I check if node is None, and if so I return.
That's my base case.
There is nothing to visit, and it stops the recursion.

Then I call helper on node.left.
This is the first step of in-order, so all smaller values are visited first.

When that call comes back, I check if result is not None.
If so, I already found the answer somewhere in the left subtree.
So I return right away.
This stops me from counting this node, and from going into the right subtree.
I compare with None, not with 0 or False,
because the answer itself could be 0.

If I haven't found it yet, I count this node.
I add 1 to count.

Then I check if count is equal to k.
If so, this is the kth smallest.
I save node.val in result, and return.
Returning here skips the right subtree, which I don't need anymore.

If count is not k yet, I call helper on node.right.
This continues the in-order traversal to the bigger values.

After defining helper, I call helper on root once.
That kicks off the traversal.

And finally I return result.

## 8. Testing

Before I finish, I want to test the edge cases.
- One node, k = 1: the left is None, count becomes 1, and I save the value.
- k = 1: I go to the leftmost node, and it is the first one counted.
- k = n: I go through the whole tree, and the last node is the answer.
- A node value of 0: result is 0, which is not None, so it's still detected.
- Skewed tree: the recursion goes n levels deep.
- Duplicate values: not allowed in a BST, so I don't worry about it.

For my example with k = 3:
- Go left from 3 to 1, then 1 has no left child.
- Count 1, it becomes 1. Not equal to 3. Go right to 2.
- At 2, count becomes 2. Not equal to 3. Both children are None.
- Back at 3, count becomes 3. This equals k, so result is 3.
- I return, and I never visit 4.

If I'm asked what happens when the tree is changed often,
and I need to find the kth smallest many times,
I can store the size of each subtree in every node.
Then I can find the kth smallest by going down one path, in O(h).

If the tree could be very deep, Python's recursion limit is about 1000.
In that case I would use an iterative in-order traversal with a stack.
I'd go left as far as I can, pop a node and count it, then go right.

## 9. Complexity

Time: O(h + k)
- I walk down to the leftmost node first, which takes h steps.
- Then I visit at most k nodes in order, and stop.
- Worst case, k is close to n, so it's O(n).

Space: O(h), where h is the tree height
- Only the call stack, plus a counter and a result variable.
- O(log n) if balanced, O(n) if skewed.
"""
class Solution:
    def kSmallestBST(self, root, k):
        count = 0
        result = None
        def helper(node):
            nonlocal count, result
            if node is None:
                return 
            helper(node.left)
            if result is not None:
                return
            count += 1
            if count == k:
                result = node.val
                return 
            helper(node.right)
        helper(root)
        return result