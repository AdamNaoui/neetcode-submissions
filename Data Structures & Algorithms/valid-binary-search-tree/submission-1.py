# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        nodes=[(root,float("-inf"),float("inf"))]

        while nodes:
            node,prev_min,prev_max=nodes.pop()

            if not (prev_min<node.val<prev_max):
                return False
            
            if node.left:
                nodes.append((node.left,prev_min,node.val))
            
            if node.right:
                nodes.append((node.right,node.val,prev_max))
        
        return True

        