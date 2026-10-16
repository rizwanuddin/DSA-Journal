"""
Subtree of Another Tree - Easy

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values 
of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be 
considered as a subtree of itself.

Example 1:
Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2:
Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false




# Subtree of Another Tree: My Thought Process

## 1. Understanding

I want to make sure I understand the problem correctly.
I'm given two binary trees, root and subRoot.
I need to return True if some node in root has a subtree
that is exactly the same as subRoot.
Same means same structure and same values.

Quick questions:
- Does the match need to include all descendants? I'll assume yes.
  So a node and only some of its children does not count.
- Can subRoot be empty? I'll assume no, it has at least one node.
- Can root be empty? I'll assume it can, and return False.
- Can values repeat? I'll assume yes, so matching a value is not enough.

## 2. Restate

So I'm looking for a node in root where the tree below it
is a perfect copy of subRoot.
If I find one, I return True.
If I check every node and none match, I return False.

## 3. Example

```
root:        subRoot:
    3           4
   / \         / \
  4   5       1   2
 / \
1   2
```

Starting at the node 4 in root, the tree below it is 4 with children 1 and 2.
That is exactly subRoot, so the answer is True.

Now add one extra node, 0, under the node 2 in root.
The node 4 in root now has a bigger subtree than subRoot.
So it no longer matches, and the answer is False.

Edge case: subRoot is the same as root, which returns True.

## 4. Brute force

There isn't a much slower idea than this one.
My first idea is to treat every node in root as a possible match.
At each node, I compare the tree below it with subRoot, node by node.
If they are identical, I return True.

This works because a matching subtree must start at some node in root.
So trying every node covers every possibility.

The cost is O(m * n).
m is the number of nodes in root.
n is the number of nodes in subRoot.
Each of the m nodes may start a comparison that goes up to n nodes deep.

This is the standard solution, and it's good enough here.
If I'm asked to go faster, I can serialize both trees
and check if one string is inside the other.
That gets O(m + n).

## 5. Key observation

The problem splits into two smaller problems.

The first one is, are these two trees identical?
That is a simple recursion on two trees at the same time.

The second one is, which node in root should I start from?
That is a search through root, and the answer could be any node.

So I write them as two separate functions.
One checks if two trees are the same.
The other walks through root and calls the first one at each node.

## 6. Approach

Instead of trying to do everything in one function,
I can write a sameTree helper, and call it at every node of root.

The data structure I will use is the recursion call stack,
because both tasks are naturally recursive on trees.

As I go through root, at each node I will check if the tree
starting there is the same as subRoot.

When sameTree returns True, I will return True right away.

When it returns False, I will search the left and right subtrees.

When I reach None in root, I will return False,
because I ran out of nodes without finding a match.

At the end, I return whatever the search finds.

For sameTree, I compare two nodes at a time.
If both are None, they match.
If only one is None, they don't match.
If the values are different, they don't match.
Otherwise, both the left sides and the right sides must match.

## 7. While coding

First I make a class called Solution.

Then I make a function called isSubtree that takes self, root, and subRoot.
This is the search through root.

Before anything else, I check if root is None, and if so I return False.
That's my base case.
It means I ran out of nodes without finding a match.

Then I call a helper called sameTree on root and subRoot.
I'll write that helper in a moment.
If it returns True, I return True right away.
This checks whether the tree starting at this node is exactly subRoot.

If it didn't match here, I search the children.
I return isSubtree on root.left, or isSubtree on root.right.
I'm using or, so it stops as soon as one side finds a match.
subRoot stays the same in each call, because I'm always looking for the same tree.

Now I write the helper.
I make a function called sameTree that takes self, a, and b.
a walks through the tree from root, and b walks through subRoot.

First, if a is None and b is None, I return True.
Both trees ended at the same spot, so they match.

Next, if a is None or b is None, I return False.
By now, I know both can't be None, because the line above handled it.
So this means only one of them ended, which means the shapes are different.

Then I check if a.val is not equal to b.val, and if so I return False.
The values don't match.

Finally, I return sameTree on the left children, and sameTree on the right children.
I'm using and, because both sides have to match.
If the left side fails, it won't even check the right side.

## 8. Testing

Before I finish, I want to test the edge cases.
- Empty root: returns False right away.
- subRoot same as root: sameTree matches at the very first node, so True.
- Match is deep in the tree: the search keeps going down until it finds it.
- Extra child below the match: sameTree fails because one side is None
  and the other isn't, so it correctly returns False.
- Same values but different shape: the None check catches it.
- Repeated values: a value match alone is not enough,
  because sameTree checks the whole structure below it.
- Skewed tree: recursion goes n levels deep.

If the tree could be very deep, Python's recursion limit is about 1000.
In that case I would use an iterative approach, or the serialization idea.

## 9. Complexity

Time: O(m * n)
- m is the number of nodes in root.
- n is the number of nodes in subRoot.
- isSubtree visits each node in root once.
- At each node, sameTree can go up to n nodes deep.
- Worst case, that is m times n.

Space: O(h), where h is the height of root
- Only the call stack, no extra structures.
- sameTree only goes as deep as the tree it is currently inside.
- O(log m) if balanced, O(m) if skewed.
"""
class Solution:
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    def sameTree(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        return (self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right))
            