# Last updated: 3/23/2025, 10:14:24 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        templ = left = ListNode(0)
        tempr = right = ListNode(0)
        
        curr = head
        
        while curr != None:
            
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next

            curr = curr.next

        right.next = None
        
        left.next = tempr.next
        
        return templ.next