"""
Same Tree - Easy

Given the roots of two binary trees p and q, return true if 
the trees are equivalent, otherwise return false.
Two binary trees are considered equivalent if they share the 
exact same structure and the nodes have the same values.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:
Input: p = [1,2,3], q = [1,3,2]
Output: false
"""
class Solution:
    def isSameTree(self, p, q):

        # Both are None → same
        if p is None and q is None:
            return True

        # Only one is None → different structure
        if p is None or q is None:
            return False

        # Values are different
        if p.val != q.val:
            return False

        # Compare left with left
        left_same = self.isSameTree(p.left, q.left)

        # Compare right with right
        right_same = self.isSameTree(p.right, q.right)

        # Both sides must be the same
        return left_same and right_same