"""
Preorder Traversal

Given root of binary tree, return the preorder traversal of the binary tree.

Example 1:
Input : root = [1, 4, null, 4 2]
Output : [1, 4, 4, 2]
Explanation :

Example 2:
Input : root = [1]
Output : [1]
Explanation : Only root node is present.




## Binary Tree Preorder Traversal

**Clarify:**
- given the root of a binary tree, return the values in preorder — that's root, then left, then right
- just need the values as a list, order matters

**Brute force:**
- not really a brute force situation, recursion following the definition is just the natural way to do this
- could also do it iteratively using an explicit stack, but that's a different implementation, not a slower alternative

**Optimize:**
- recursion matches the definition directly, so I just follow it, visit the node first, then go left, then go right
- this is O(n) since every node gets touched exactly once

**Key observation:**
- the big difference from inorder is just WHERE I append the value — here I append it before going left or right, since root comes first in preorder
- the recursive call stack handles all the "go deep then come back" movement for me, I don't track anything manually
- base case is still just hitting a None node, so I return and let it unwind back up

**Approach:**
- make an empty result list
- write a helper function preorder that takes a node
- if node is None, return, nothing to do
- append this node's value to result first
- recursively call preorder on the left child
- recursively call preorder on the right child
- call preorder starting at root, then return result

**While coding:**
- first I define the class TreeNode, with val, left, and right
- then I define a separate class Solution for the actual traversal logic
- inside Solution, I define preorderTraversal, taking self and root
- I create an empty list called result
- then I define a nested function called preorder, taking node
- inside preorder, first I check if node is None, if so I return
- then I append node.val to result right away, since root comes first in preorder
- then I call preorder on node.left
- then I call preorder on node.right
- after defining preorder, I call it once with root to start things off
- finally I return result

**Edge cases:**
- if root is None, the first call hits the base case immediately, result stays empty, returns an empty list
- if there's only one node, it just appends that one value and returns
- a completely skewed tree, all left or all right children, still works, recursion just goes deep before unwinding

**Complexity:**
- time is O(n), every node visited exactly once
- space is O(h), h being the height of the tree, because of the recursion call stack — worst case O(n) for a skewed tree, O(log n) if it's balanced
"""
class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def preorderTraversal(self, root):
        result = []
        def preorder(node):
            if node is None:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return result
