"""
Maximum path sum
In a binary tree, a path is a list of nodes where there is an edge between every pair of neighbouring nodes. 
A node may only make a single appearance in the sequence.The total of each node's values along a path is its path sum. 
Return the largest path sum of all non-empty paths given the root of a binary tree.
Note: The path does not have to go via the root.

Example 1:
Input : root = [20, 9, -10, null, null, 15, 7]
Output : 34
Explanation : The path from node 15 to node 9 has maximum path sum.
The path is 15 -> -10 -> 20 -> 9.

Example 2:
Input : root = [-10, 9, 20, null, null, 15, 7]
Output : 42
Explanation : The path from node 15 to node 7 has maximum path sum.
The path is 15 -> 20 -> 7.
"""
class Solution:
    def maxPathSum(self, root):
        self.best = float('-inf')

        def maxGain(node):
            if node is None:
                return 0

            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            self.best = max(self.best, node.val + leftGain + rightGain)

            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.best