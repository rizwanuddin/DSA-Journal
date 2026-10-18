"""
Construct Binary Tree From Preorder And Inorder Traversal - Medium

You are given two integer arrays preorder and inorder.
preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]
Example 2:

Input: preorder = [1], inorder = [1]
Output: [1]



# Construct Binary Tree from Preorder and Inorder Traversal: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given two lists, preorder and inorder.
They are the two traversals of the same binary tree.
I need to rebuild the tree and return its root.

Quick questions:
- Are all values unique? I'll assume yes.
  This matters, because I find the root by its value.
- Are the two lists always valid for the same tree? I'll assume yes.
- Can the lists be empty? I'll assume yes, and return None.

## 2. Restate

So I'm given the order a tree was visited in, in two different ways.
I need to figure out the shape of the tree from those two orders.

## 3. Example

```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

The tree is:

```
    3
   / \
  9  20
    /  \
   15   7
```

Preorder visits the node first, then left, then right.
Inorder visits left, then the node, then right.

Edge case: both lists empty returns None.

## 4. Brute force

My first idea is to use the two lists directly.
The first value in preorder is always the root.
I find that value in inorder.
Everything to its left in inorder is the left subtree.
Everything to its right in inorder is the right subtree.
Then I cut both lists into a left part and a right part,
and repeat the same steps on each part.

This works because each part describes a smaller tree
in the same two traversal orders.

The cost is O(n^2) in the worst case.
Searching for the root in inorder takes O(n).
Slicing the lists copies up to n values at each call.
A skewed tree is the worst case, because it goes n levels deep
and every level copies almost everything.

## 5. Key observation

Preorder tells me who the root is.
The root is always the first value.

Inorder tells me how the rest is split.
The root's position in inorder separates the left side from the right side.

The position gives me the size of the left subtree.
If the root is at index mid in inorder, the left subtree has mid nodes.

That size also tells me how to cut preorder.
After the root, the next mid values in preorder are the left subtree.
Everything after that is the right subtree.

So one value and one position let me split both lists correctly.
The same problem repeats on each half, so recursion fits.

## 6. Approach

Instead of trying to figure out the whole tree at once,
I can find the root, split both lists, and trust recursion for the two halves.

The data structure I will use is the recursion call stack,
because every half is a smaller version of the same problem.

As I go through the lists, I will take the first value of preorder as the root.

When I find that root in inorder, I will use its position
to split both lists into a left part and a right part.

When a list is empty, I will return None.
That's my base case.

At the end, I return the root.

## 7. While coding

First I make a class called Solution.

Then I make a function called buildTree that takes self, preorder, and inorder.

First thing inside it, I check if preorder is empty, and if so I return None.
That's my base case.
An empty list means there is no tree here, and it stops the recursion.
I only need to check one list, because both lists always have the same length.

Then I create the root node.
Its value is preorder[0], because preorder visits the root first.

Then I find that same value in inorder, using index, and store it as mid.
The position mid is also the number of nodes in the left subtree.
This works because values are unique.

Now I build the left subtree.
I call buildTree on two slices.
For preorder, I take from index 1 up to mid + 1.
I skip index 0, because that's the root.
Then I take the next mid values, which are the left subtree.
For inorder, I take everything before mid.
Both slices have mid values, so they describe the same left subtree.
I store the result in root.left.

Then I build the right subtree.
For preorder, I take everything from mid + 1 to the end.
That's what is left after the root and the left subtree.
For inorder, I take everything after mid.
I store the result in root.right.

And at the end I return root, so the parent call can attach it.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty lists: returns None right away.
- One node: mid is 0, both slices are empty, so the node has no children.
- Left-skewed tree: preorder is the reverse of inorder.
  mid is always the last index, and the right side is always empty.
- Right-skewed tree: both lists are the same.
  mid is always 0, and the left side is always empty.
- Duplicate values: not allowed, because index would find the wrong one.

For my example:
- The root is 3, and mid is 1 in inorder.
- Left preorder is [9], and left inorder is [9]. That builds the node 9.
- Right preorder is [20, 15, 7], and right inorder is [15, 20, 7].
- The root of the right side is 20, and mid is 1.
- Its left is [15] and its right is [7].

This matches the tree.

If I'm asked to make it faster, there are two fixes.
First, I put every inorder value and its index into a hash map once.
Then finding the root is O(1), instead of O(n).
Second, I stop slicing.
I pass index boundaries for the inorder range instead,
and keep one pointer that moves forward through preorder.
I must build the left subtree before the right,
because the pointer moves in preorder order.

If the tree could be very deep, Python's recursion limit is about 1000.
In that case I would need an iterative version with a stack.

## 9. Complexity

Time: O(n^2) in the worst case
- Each call does one index search, which is O(n).
- Each call also slices lists, which copies up to n values.
- There are n calls, one per node.
- Skewed trees hit the worst case.

Space: O(n^2) in the worst case
- Every call holds its own slices.
- On a skewed tree, there are n calls at once, with slices of size n, n - 1, and so on.
- On a balanced tree, it's much smaller.

With the hash map and index boundaries, both become O(n).
The map takes O(n) space, and the call stack takes O(h).
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root