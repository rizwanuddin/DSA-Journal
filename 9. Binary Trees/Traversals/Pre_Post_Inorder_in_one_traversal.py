"""
Pre, Post, Inorder in one traversal

Given a binary tree with root node. Return the In-order,Pre-order and Post-order traversal of the binary tree.

Example 1:
Input : root = [1, 3, 4, 5, 2, 7, 6 ]
Output : [ [5, 3, 2, 1, 7, 4, 6] , [1, 3, 5, 2, 4, 7, 6] , [5, 2, 3, 7, 6, 4, 1] ]
Explanation : The In-order traversal is [5, 3, 2, 1, 7, 4, 6].
The Pre-order traversal is [1, 3, 5, 2, 4, 7, 6].
The Post-order traversal is [5, 2, 3, 7, 6, 4, 1].

Example 2:
Input : root = [1, 2, 3, null, null, null, 6 ]
Output : [ [2, 1, 3, 6] , [1, 2, 3, 6] , [2, 6, 3, 1] ]
Explanation : The In-order traversal is [2, 1, 3, 6].
The Pre-order traversal is [1, 2, 3, 6].
The Post-order traversal is [2, 6, 3, 1].

"""
class Solution:
    def allTraversals(self, root):
        if root is None:
            return [[], [], []]
        result = []
        preorder = []
        inorder = []
        postorder = []
        stack = [(root, 1)]
        while stack:
            node, state = stack.pop()
            if state == 1:
                preorder.append(node.val)
                stack.append((node, 2))
                if node.left:
                    stack.append((node.left, 1))
            elif state == 2:
                inorder.append(node.val)
                stack.append((node, 3))
                if node.right:
                    stack.append((node.right, 1))
            else:
                postorder.append(node.val)
        result = [inorder, preorder, postorder]
        return result
                

"""
Preorder  = ROOT → LEFT → RIGHT
Inorder   = LEFT → ROOT → RIGHT
Postorder = LEFT → RIGHT → ROOT



1st time we reach 1
→ before exploring LEFT
→ PREORDER

2nd time we reach 1
→ LEFT is finished, before RIGHT
→ INORDER

3rd time we reach 1
→ LEFT and RIGHT are finished
→ POSTORDER

-------------
(node, 1)
→ add node to PREORDER
→ change to (node, 2)
→ go LEFT


(node, 2)
→ add node to INORDER
→ change to (node, 3)
→ go RIGHT


(node, 3)
→ add node to POSTORDER
→ DONE with this node
---------------
"""
