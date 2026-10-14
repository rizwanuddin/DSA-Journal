"""
Check for balanced binary tree

Given a binary tree root, find if it is height-balanced or not.
A tree is height-balanced if the difference between the heights of left and right subtrees is not more than one for all nodes of the tree. 

Example 1:
Input : [3, 9, 20, null, null, 15, 7]
Output : Yes

Example 2:
Input : [1, 2, null, null, 3]
Output : No
"""
class Solution:
    def checkBalancedTree(self, root):
        def height(node):
            if node is None:
                return 0

            leftHeight = height(node.left)
            if leftHeight == -1:
                return -1

            rightHeight = height(node.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        return height(root) != -1