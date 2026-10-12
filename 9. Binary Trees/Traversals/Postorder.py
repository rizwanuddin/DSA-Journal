"""
Postorder Traversal

Given root of binary tree, return the Postorder traversal of the binary tree.

Example 1:
Input : root = [1, 4, null, 4, 2]
Output : [4, 2, 4, 1]


Example 2:
Input : root = [1, null, 2, 3]
Output : [3, 2, 1]



## Binary Tree Postorder Traversal

**Clarify:**
- given the root of a binary tree, return the values in postorder — that's left, then right, then root
- just need a list of values, order matters

**Brute force:**
- not really a brute force case, recursion following the definition is just the natural approach
- could also do it iteratively with a stack, but that's a different implementation, not a slower alternative

**Optimize:**
- recursion matches the definition directly, go left, go right, then visit the node last
- O(n) since every node gets touched exactly once

**Key observation:**
- the difference from preorder and inorder is just WHERE I append the value — here it's dead last, after both recursive calls finish
- that makes sense since postorder means root comes after both children are fully processed
- same base case as always, hitting a None node just means return and let the stack unwind

**Approach:**
- make an empty result list
- write a helper function postorder that takes a node
- if node is None, return, nothing to do
- recursively call postorder on the left child
- recursively call postorder on the right child
- append this node's value to result last
- call postorder starting at root, then return result

**While coding:**
- first I define the class TreeNode, with val, left, and right
- then a separate class Solution for the traversal logic
- inside Solution, I define postorderTraversal, taking self and root
- I create an empty list called result
- then I define a nested function called postorder, taking node
- inside postorder, first I check if node is None, if so I return
- then I call postorder on node.left
- then I call postorder on node.right
- then, only after both of those finish, I append node.val to result, since root comes last in postorder
- after defining postorder, I call it once with root to start things off
- finally I return result

**Edge cases:**
- if root is None, the first call hits the base case immediately, result stays empty, returns an empty list
- if there's only one node, it just appends that one value and returns
- a completely skewed tree still works fine, recursion just goes deep before the appends start happening on the way back up

**Complexity:**
- time is O(n), every node visited exactly once
- space is O(h), h being the height of the tree, from the recursion call stack — worst case O(n) for a skewed tree, O(log n) if balanced

"""
class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def postorderTraversal(self, root):
        result = []
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        postorder(root)
        return result