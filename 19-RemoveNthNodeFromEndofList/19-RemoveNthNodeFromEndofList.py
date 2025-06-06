# Last updated: 6/6/2025, 2:29:20 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size+=1
            curr = curr.next
        skipwhen = size - n 
        print(skipwhen)
        curr2 = head
        counter = 0
        if skipwhen ==0:
            return head.next
            
        while curr2:
            counter+=1
            if counter==skipwhen:
                curr2.next = curr2.next.next
                break
            curr2 = curr2.next
        return head