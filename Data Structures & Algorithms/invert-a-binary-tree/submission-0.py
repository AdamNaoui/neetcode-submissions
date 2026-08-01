# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        old_right=root.right
        old_left=root.left

        root.right=self.invertTree(old_left)
        root.left=self.invertTree(old_right)
        return root
        