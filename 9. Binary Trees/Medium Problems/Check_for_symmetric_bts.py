"""
Check for symmetrical BTs

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input : root = [1, 2, 2, 3, 4, 4, 3]
Output : true

Example 2:
Input : root = [1, 2, 2, null, 3, null, 3]
Output : false
Explanation : When a straight line is drawn through the root node and the tree is folded around it, the rightmost node 3 
is overlapped with null node and the node 3 present at left of root node is overlapped with null nodes.
So both node 3 in tree does not show symmetric behaviour.
"""
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right, right.left)


    