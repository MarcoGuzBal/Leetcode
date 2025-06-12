# Last updated: 6/12/2025, 3:55:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0
        def dfs(node):
            nonlocal sum
            if node == None:
                return 0
            if low <= node.val <= high:
                sum = sum + node.val
            if node.val >= low:
                dfs(node.left)
            if node.val <= high:
                dfs(node.right)
            
            
        sum = 0
        dfs(root)
        return sum