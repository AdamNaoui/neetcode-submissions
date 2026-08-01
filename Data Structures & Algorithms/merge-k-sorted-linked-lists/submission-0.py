# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head,curr=None,None
        candidates=set(lists)

        while candidates:
            min_node=None
            for node in candidates:
                if not min_node or node.val<min_node.val:
                    min_node=node
            
            candidates.remove(min_node)
            if min_node.next:
                candidates.add(min_node.next)
            
            if not head:
                head=min_node
                curr=min_node
                continue
            
            curr.next=min_node
            curr=min_node
        if curr:
            curr.next=None
        return head
        