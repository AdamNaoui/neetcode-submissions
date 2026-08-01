# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        old=None
        curr=head
        while curr.next:
            next_node=curr.next
            curr.next=old

            old=curr
            curr=next_node
        
        curr.next=old
        return curr
            