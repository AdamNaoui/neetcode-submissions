# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        
        root=TreeNode(preorder[0])
        
        if len(preorder)==1:
            return root
        
        root_inorder_index=inorder.index(root.val)

        left_node=self.buildTree(preorder[1:root_inorder_index+1],inorder[0:root_inorder_index])

        right_node=self.buildTree(preorder[root_inorder_index+1:],inorder[root_inorder_index+1:])

        root.left=left_node
        root.right=right_node

        return root