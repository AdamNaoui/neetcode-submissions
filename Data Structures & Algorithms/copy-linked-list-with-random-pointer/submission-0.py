"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_links={None:None}

        curr=head

        while curr:
            nodes_links[curr]=Node(curr.val,None,None)
            curr=curr.next
        
        curr=head
        while curr:
            new_node=nodes_links[curr]
            new_next=nodes_links[curr.next]
            new_random=nodes_links[curr.random]

            new_node.next=new_next
            new_node.random=new_random

            curr=curr.next
        
        return nodes_links[head]

            
        