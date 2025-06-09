# Last updated: 6/9/2025, 10:58:25 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Edge Cases
        if not head or not head.next:
            return None

        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        #Edge Case. Removing the head
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        if n == 1:
            slow.next = None
        else:
            slow.next = slow.next.next

        return head