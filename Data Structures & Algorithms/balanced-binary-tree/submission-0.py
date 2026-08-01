# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return (True,0)

            left_balanced,left_height=helper(node.left)
            right_balanced,right_height=helper(node.right)

            height=max(left_height,right_height)+1

            if not left_balanced or not right_balanced or abs(left_height-right_height)>1 :
                return (False,height)
            
            return (True,height)

        return helper(root)[0]
        