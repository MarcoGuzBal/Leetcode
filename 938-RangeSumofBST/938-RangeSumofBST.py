# Last updated: 6/12/2025, 3:55:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = [0]
        def dfs(node, low, high):
            if node:
                dfs(node.left, low, high)
                if node.val <= high and node.val >= low:
                    sum[0] += node.val
                dfs(node.right, low, high)
        dfs(root, low, high)
        return sum[0]