# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length = 0
        arr = []
        val = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        exp = length - 1
        while head:
            
            if head.val == 1:
                val += pow(2, exp)

            exp -= 1
            head = head.next
        
        return val