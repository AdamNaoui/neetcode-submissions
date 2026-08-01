"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        all_nodes={}

        nodes=[node]

        while nodes:
            n=nodes.pop()
            new_node=Node(n.val)
            all_nodes[n.val]=(new_node,n)

            for nei in n.neighbors:
                if nei.val not in all_nodes:
                    nodes.append(nei)

        print(all_nodes)
        for val in all_nodes.keys():

            new,old= all_nodes[val]

            new_neis=[]
            for nei in old.neighbors:
                new_neis.append(all_nodes[nei.val][0])
            
            new.neighbors=new_neis
            all_nodes[val]=(new,old)


        print()
        return all_nodes[node.val][0]
        

        