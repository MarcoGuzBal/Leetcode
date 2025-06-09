# Last updated: 6/9/2025, 11:51:37 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Edge Cases:
        # Reverse only first or last node
        # No head.next

        if not head:
            return None

        dummy = ListNode(0, head)

        curr = head
        prevPerm = dummy

        for _ in range(left - 1):
            prevPerm = curr
            curr = curr.next
        
        # Reverse Linked List
        prev = None
        for _ in range((right - left) + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Re arrange Pointers
        prevPerm.next.next = curr
        prevPerm.next = prev

        return dummy.next


        

        



    