# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        nodes=[(root,root.val)] # store curr_node and maximum val encountered in the path
        res=0
        while nodes:
            #DFS
            node,max_val=nodes.pop()
            
            if node.val>=max_val:
                res+=1
            
            if node.left:
                nodes.append((node.left,max(max_val,node.val)))
            
            if node.right:
                nodes.append((node.right,max(max_val,node.val)))
        
        return res
        