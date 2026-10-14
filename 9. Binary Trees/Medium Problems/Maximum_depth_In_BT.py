"""
Maximum Depth in BT

Given root of the binary tree, return its maximum 
depth. A binary tree's maximum depth is number of 
nodes along the longest path from root node down to 
the farthest node.

Example 1:
Input : root = [1, 2, 3, null, null, null , 6]
Output : 3
Explanation : The path from root node 1 to node with value 6 has maximum depth with 3 nodes along path.

Example 2:
Input : root = [3, 9, 20, null, null, 15 , 7]
Output : 3
Explanation : The path from root node 3 to node with value 15 has maximum depth with 3 nodes along path.
There exists other paths to reach the solution.
"""
class Solution:
    def maximumDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maximumDepth(root.left)
        right_depth = self.maximumDepth(root.right)
        deeper_side = max(left_depth, right_depth)
        return deeper_side + 1

