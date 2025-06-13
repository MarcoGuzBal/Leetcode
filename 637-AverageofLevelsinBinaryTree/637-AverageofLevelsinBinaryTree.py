# Last updated: 6/13/2025, 4:01:15 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # answer = []
        # q = deque()
        # q.append(root)

        # while q:
        #     length = len(q)
        #     mySum = 0
        #     for _ in range(length):
        #         popped = q.popleft()
        #         mySum += popped.val
        #         if popped.left:
        #             q.append(popped.left)
        #         if popped.right:
        #             q.append(popped.right)
        #     answer.append(mySum / length)
        # return answer

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