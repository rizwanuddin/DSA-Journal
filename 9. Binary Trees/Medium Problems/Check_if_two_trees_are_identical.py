"""
Check if two trees are identical or not

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input : p = [1, 2, 3] , q = [1, 2, 3]
Output : true

Example 2:
Input : p = [1, 2, 1] , q = [1, 1, 2]
Output : false



# Check if Two Trees Are Identical

**Pattern finder:** comparing two trees for structure + value match → recursive compare, base case on None/None

## Clarify

So I'm given two tree roots, p and q, and I need to check if they're the same tree.

Same tree means two things — the structure has to match exactly, so nodes have to exist in the same positions in both trees.

And the values have to match too, at every single corresponding node.

So even if two trees have the exact same values, if they're arranged differently, that's not identical.

## Brute force

Honestly there isn't really a separate brute force here, the direct comparison basically is the solution.

The only other idea I had was flattening both trees into a list using some traversal and just comparing the lists.

But that doesn't actually work reliably, because two different shaped trees can produce the same flattened list depending on the traversal I pick.

So I'm just going straight to comparing the trees directly, node by node.

## Optimize

Since there's no slow version to speed up, the real thing to figure out is how to compare two trees without manually checking every branch myself.

And the answer is recursion, because a tree is already a recursive structure — every subtree is just a smaller tree.

So if I can solve "are these two trees the same" for a small case, I can build the big case out of smaller ones.

## Key observation

The whole problem breaks down into two smaller versions of itself — check if the left subtrees match, and check if the right subtrees match.

So I don't need to think about the whole tree at once.

I just handle one node, and trust that the recursive call already handles everything below it correctly.

That's the leap of faith part — I don't trace three levels down in my head, I just assume identicalCheck works on anything smaller than what I'm looking at right now.

## Approach

First I handle the case where both nodes are None, because two empty trees count as identical.

Then I handle the case where only one of them is None, because that means the shapes don't match, so that's an automatic false.

Then, once I know both nodes actually exist, I check if their values are different, and if so I stop right there.

And if none of that triggers, I recurse into the left children and recurse into the right children, and both of those need to come back true for the whole thing to be true.

## While coding

First I make a class called Solution, since that's just the structure LeetCode wants.

Then inside it I make a function called identicalCheck that takes self, root1, and root2.

First thing I check is if root1 is None and root2 is None — if that's true I return True right away, since two empty trees are the same.

Next I check if root1 is None or root2 is None — meaning only one of them is empty — and if so I return False, because the shapes don't match.

Then I check if root1.val is not equal to root2.val, and if the values are different I return False immediately, no need to go further down this branch.

And if I get past all of that, both nodes exist and their values match, so now I return identicalCheck on root1.left and root2.left, anded together with identicalCheck on root1.right and root2.right.

Both sides have to come back true for me to return True overall.

## Edge cases

One tree completely empty and the other not — caught by my second if statement.

Both trees being just a single node — falls through to the value check, then the recursive calls immediately hit the both-None base case and return True.

Same values but different shapes, like one tree has a left child where the other has a right child instead — this gets caught because when I recurse into root1.left vs root2.left, one of them ends up None and the other doesn't, so it hits my second if statement.

## Complexity

Time complexity is O(n), since in the worst case I visit every node in both trees once.

Space complexity is O(h), where h is the height of the tree, because that's how deep the recursive call stack goes — O(log n) if the tree's balanced, O(n) if it's a skewed straight-line tree.
"""
class Solution:
    def identicalCheck(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.identicalCheck(root1.left, root2.left) and self.identicalCheck(root1.right, root2.right)
    
        

        

