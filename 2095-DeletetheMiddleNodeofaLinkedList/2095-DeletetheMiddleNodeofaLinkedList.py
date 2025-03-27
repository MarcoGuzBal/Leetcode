# Last updated: 3/27/2025, 11:06:46 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None

        temp = ListNode(0, head)

        slow = temp
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head