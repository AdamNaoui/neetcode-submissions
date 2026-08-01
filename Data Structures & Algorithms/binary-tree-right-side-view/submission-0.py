# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        nodes=[(root,0)]

        res=[]

        while nodes:
            node,lvl=nodes.pop(0)

            if not nodes or nodes[0][1]>lvl:
                res.append(node.val)
            
            if node.left:
                nodes.append((node.left,lvl+1))
            
            if node.right:
                nodes.append((node.right,lvl+1))
        return res

        