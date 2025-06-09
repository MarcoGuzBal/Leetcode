# Last updated: 6/9/2025, 12:46:26 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None

        slow = head
        fast = head
        cycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break

        if cycle:
            curr = head

            while curr != slow:
                curr = curr.next
                slow = slow.next

            return curr
        else:
            return None
        