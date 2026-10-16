"""
Children Sum Property in Binary Tree

Given the root of a binary tree, return true if and only if every node’s value is 
equal to the sum of the values stored in its left and right children.
For any missing ( null ) child, its value is treated as 0.
A leaf node automatically satisfies the rule because both children are null.

Example 1:
Input: root = [1,4,3,5]
Output: false
Explanation:
The root is 1, but its children sum to 4 + 3 = 7. Since 1 ≠ 7, the tree violates the property.

Example 2:
Input: root = [10,4,6,1,3,2,4]
Output: true
Explanation:
4 = 1 + 3
6 = 2 + 4
10 = 4 + 6
All internal nodes satisfy the condition.



# Children Sum Property

**Pattern finder:** compare each node's value against the sum of its own direct children → recursive check, base case on leaf/None, no accumulation needed

## Clarify

So I'm given the root of a binary tree, and I need to check if every single node satisfies this rule — the node's own value has to equal the sum of its left and right children's values.

If a child is missing, I treat that side as zero.

A leaf node automatically passes, because it has no children to sum, so there's nothing to violate.

## Brute force

Honestly there isn't really a separate brute force here either, same as the other tree problems I've done — checking each node directly already is the efficient way to do it.

I guess the only slower version I could think of would be collecting every node into a list first with some traversal, then looping through that list afterward to check each one's children.

But that's just doing the same check in two passes instead of one, so there's no real reason to do that.

## Optimize

Since there's no slow version to speed up, the thing to figure out is how to check this rule at every node without manually writing separate logic for every level of the tree.

And that's recursion again, because I can check one node's rule, and then trust that the recursive call handles checking the rule for everything underneath it.

## Key observation

The key thing I noticed is that this check is completely local — at any given node, I only ever need that node's own value and its two direct children's values, nothing deeper.

So I don't need to carry any accumulated sum from below, I just need each node to hand its own value up to its parent, so the parent can do its own local check.

And since one bad node anywhere should make the whole tree invalid, I need some way for a failure found deep in the tree to still reach my final answer, even though each node's return value is just its own plain value, not a pass or fail signal.

## Approach

So my plan is, I make a helper function that visits every node.

If the node is None, I return 0, since a missing child contributes nothing.

Otherwise, I recurse into the left child and the right child, and get back their own values.

Then, only if the current node actually has at least one child, I check if the node's value equals the sum of those two returned values, and if it doesn't match, I mark the whole thing as invalid.

Then I just return the current node's own value upward, so its parent can do the same check.

## While coding

First I make a class called Solution, since that's the structure LeetCode wants.

Then I make a function called isChildrenSumProperty that takes self and root.

Before anything else, I set self.valid equal to True, since I'm assuming it's valid until I find a reason it isn't.

Then I define an inner function called sumHelper that takes a node.

First thing inside sumHelper, I check if node is None, and if so I return 0 right away, since that's my base case.

Then I call sumHelper on node.left and store it as leftVal, and call sumHelper on node.right and store it as rightVal.

Then I check if node.left is not None or node.right is not None, meaning this node actually has at least one child, because if it's a leaf I don't want to run the check at all.

Inside that, I check if node.val is not equal to leftVal plus rightVal, and if that's true, I set self.valid to False.

And at the very end of sumHelper, I return node.val, so that whichever call invoked this one gets this node's own value back.

After defining sumHelper, I call sumHelper on root once, just to kick off the recursion and let it run through the whole tree.

And finally I return self.valid, which by that point reflects whether any node anywhere violated the rule.

## Edge cases

A single node with no children — it's a leaf, so the check gets skipped entirely, and the tree is valid by default.

A node with only one child — I still run the check, since my condition is "at least one child exists," not "both children exist," so a missing side just counts as zero in the sum.

A violation buried deep in the tree, not at the root — since self.valid gets set the moment any node fails, it doesn't matter how deep the failure is, it still propagates correctly to my final answer.

## Complexity

Time complexity is O(n), since I visit every node in the tree exactly once.

Space complexity is O(h), where h is the height of the tree, because that's how deep my recursive call stack goes — O(log n) if the tree's balanced, O(n) if it's a skewed straight-line tree.
"""
class Solution:
    def isChildrenSumProperty(self, root):
        self.valid = True

        def sumHelper(node):
            if node is None:
                return 0

            leftVal = sumHelper(node.left)
            rightVal = sumHelper(node.right)

            if node.left is not None or node.right is not None:
                if node.val != leftVal + rightVal:
                    self.valid = False

            return node.val

        sumHelper(root)
        return self.valid