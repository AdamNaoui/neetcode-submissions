# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res=[]
        nodes=[(root,1)]

        while nodes:
            node,lvl=nodes.pop(0)
            
            if lvl> len(res):
                res.append([])
            
            res[-1].append(node.val)

            if node.left:
                nodes.append((node.left,lvl+1))
            
            if node.right:
                nodes.append((node.right,lvl+1))
        return res
        