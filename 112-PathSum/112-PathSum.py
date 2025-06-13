# Last updated: 6/13/2025, 3:17:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # DFS PreOrder, Keeping a sum variable
        # When we reach a leaf node, we check if the path is equal to targetSum
        # After the node is fully processed, we then remove that subtract that value from our sum
        # The way its subtracted is by going back in the call stack

        def dfs(root, pathSum):
            if not root:
                return False
            else: 
                pathSum += root.val
                if not root.left and not root.right:
                    if pathSum == targetSum:
                        return True
                return dfs(root.left, pathSum) or dfs(root.right, pathSum)

        return dfs(root, 0)

        
