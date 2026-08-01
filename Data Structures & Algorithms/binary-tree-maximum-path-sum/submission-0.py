# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0,-1001

            left_max_straight_path,left_max_path=helper(node.left)
            right_max_straight_path,right_max_path=helper(node.right)

            new_max_straight_path=max([left_max_straight_path+node.val,right_max_straight_path+node.val,node.val])

            new_max_path=max([left_max_path,right_max_path,new_max_straight_path,left_max_straight_path+right_max_straight_path+node.val])

            return new_max_straight_path,new_max_path
        
        straight,res=helper(root)
        return res
