# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def dfs(root):
            if not root:
                return 

            root.left = dfs(root.left)
            result.append(root.val)
            root.right = dfs(root.right)


        dfs(root)
        return result