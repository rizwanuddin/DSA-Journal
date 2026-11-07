"""
Deletion of the Kth element of Linked List

Given the head of a singly linked list and an integer k, delete the kth node of the linked list and return the head of the modified list.

Example 1:
Input: linkedList = [3, 4, 5], k = 2
Output: linkedList = [3, 5]
Explanation:
The 2nd node with value 4 was removed.

Example 2:
Input: linkedList = [1, 2, 3], k = 1
Output: [2, 3]
Explanation:
The 1st Node was removed, note that the value of the head has changed.
"""
class Solution:
    def removeNode(self, head, k):
        if head is None:
            return None
        if k == 1:
            head = head.next
            return 
        prev = head
        for _ in range(1, k - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head