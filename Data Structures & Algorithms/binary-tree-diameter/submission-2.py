# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node): # returns max_depth and diameter
            if not node:
                return 0,0
            
            left_depth,left_diameter= helper(node.left)
            if node.left:
                left_depth+=1

            right_depth,right_diameter= helper(node.right)
            if node.right:
                right_depth+=1

            new_depth=max(left_depth,right_depth)
            new_diameter=max([left_diameter,right_diameter,left_depth+right_depth])

            return new_depth,new_diameter
        
        _,res=helper(root)
        return res

        