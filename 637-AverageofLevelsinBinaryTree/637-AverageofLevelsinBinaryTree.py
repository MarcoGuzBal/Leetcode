# Last updated: 6/13/2025, 4:00:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        result = []

        while queue:
            level = []
            for i in range(len(queue)):
                popped = queue.popleft()
                level.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            result.append(sum(level)/len(level))

        return result
                