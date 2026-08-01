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
            
        nodes=[(root,1)]

        res=0
        while nodes:
            node,depth=nodes.pop()
            res=max(res,depth)

            if node.left:
                nodes.append((node.left,depth+1))

            if node.right:
                nodes.append((node.right,depth+1))

        return res