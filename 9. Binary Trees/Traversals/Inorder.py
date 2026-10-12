"""
Inorder Traversal

Given root of binary tree, return the Inorder traversal of the binary tree.

Example 1:
Input : root = [1, 4, null, 4, 2]
Output : [4, 4, 2, 1]

Example 2:
Input : root = [1, null, 2, 3]
Output : [1, 3, 2]



## Binary Tree Inorder Traversal

**Clarify:**
- I'm given the root of a binary tree, and I need to return the values in inorder — that's left, then root, then right
- just need a list of values, order matters

**Brute force:**
- there isn't really a slower alternative here, recursion following the definition IS the natural way to do this
- I guess I could do it iteratively with an explicit stack instead of recursion, but that's not really brute force, just a different implementation

**Optimize:**
- recursion directly matches the definition of inorder, so I just follow it: go left all the way down, visit the node, then go right
- this is already O(n), since I touch every node exactly once

**Key observation:**
- the recursive call naturally handles the "going all the way down" part for me, I don't need to manage anything manually
- the base case is just hitting a None node, meaning I've gone past a leaf, so I return and let the call stack unwind back up
- I'm not returning anything from inorder itself, I'm just appending to a result list that's shared across all the recursive calls, since it's defined outside the inner function

**Approach:**
- make an empty result list
- write a helper function inorder that takes a node
- if node is None, just return, nothing to do
- recursively call inorder on the left child first
- then append this node's value to result
- then recursively call inorder on the right child
- call inorder starting at root, then return result

**While coding:**
- first I define the class TreeNode, with val, left, and right in the constructor
- then I define a separate class Solution, since the traversal logic shouldn't live inside TreeNode itself
- inside Solution, I define inorderTraversal, taking self and root
- I create an empty list called result
- then I define a nested function called inorder, taking node
- inside inorder, first I check if node is None, if so I just return
- then I call inorder on node.left, that handles the left side first
- then I append node.val to result, that's visiting the root
- then I call inorder on node.right, that handles the right side
- after defining inorder, I call it once with root to kick everything off
- finally I return result

**Edge cases:**
- if root is None, the very first call hits the base case immediately, result stays empty, returns an empty list
- if there's only one node, no left or right children, it just appends that one value
- a tree that's just a straight line to the left or right still works fine, recursion just goes deep before coming back up

**Complexity:**
- time is O(n), since every node gets visited exactly once
- space is O(h), where h is the height of the tree, because of the recursion call stack — in the worst case, a completely unbalanced tree, that's O(n), but for a balanced tree it's O(log n)
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        def inorder(node):
            # Base case
            if node is None:
                return 
            # Left
            inorder(node.left)
            # Root
            result.append(node.val)
            # Right
            inorder(node.right)

        inorder(root)
        return result