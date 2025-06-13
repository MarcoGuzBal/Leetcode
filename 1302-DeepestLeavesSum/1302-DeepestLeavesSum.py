# Last updated: 6/13/2025, 4:03:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        answer = []
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            mySum = 0
            for _ in range(length):
                popped = q.popleft()
                mySum += popped.val
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            answer.append(mySum)
        return answer[-1]
        

                
        
