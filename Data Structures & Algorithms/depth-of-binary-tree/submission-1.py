# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        nodes=[(1,root)]
        max_depth=0

        while nodes:
            depth,node=nodes.pop()

            max_depth=max(max_depth,depth)

            if node.left:
                nodes.append((depth+1,node.left))
            
            if node.right:
                nodes.append((depth+1,node.right))
        
        return max_depth
            


        