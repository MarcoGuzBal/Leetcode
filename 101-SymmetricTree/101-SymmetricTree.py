# Last updated: 4/14/2025, 1:01:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        leftRoot = root.left
        rightRoot = root.right

        def dfs(leftRoot, rightRoot):

            
            if not leftRoot and not rightRoot:
                return True

            if not leftRoot or not rightRoot:
                return False

            if leftRoot.val != rightRoot.val:
                return False
    
            return dfs(leftRoot.left, rightRoot.right) and dfs(leftRoot.right, rightRoot.left)

        return dfs(leftRoot, rightRoot)
