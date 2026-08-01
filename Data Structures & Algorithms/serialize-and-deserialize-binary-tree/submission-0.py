# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def max_depth(self,root):
        if not root:
            return 0

        return 1+max(self.max_depth(root.left),self.max_depth(root.right))
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        max_depth=self.max_depth(root)
        # bfs level order
        nodes=[(root,1)]
        string=""

        while nodes:
            node,lvl=nodes.pop(0)
            string+= str(node.val) if node else "None"
            
            if lvl+1<=max_depth:
                nodes.append((node.left if node else None,lvl+1))
                nodes.append((node.right if node else None,lvl+1))
            
            if nodes:
                string+=":"
            
        print(string)
        return string
            


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        array_data=[""]+data.split(":") # added a buffer at index 0 to be 1-indexed
        def dfs(index):
            if index>=len(array_data):
                return None
            
            if array_data[index]=="None":
                return None
            
            node=TreeNode(int(array_data[index]))
            node.left=dfs(2*index)
            node.right=dfs(2*index+1)
            return node
            
        return dfs(1)
