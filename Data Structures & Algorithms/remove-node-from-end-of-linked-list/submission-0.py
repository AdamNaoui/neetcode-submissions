# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        while curr:
            n-=1
            curr=curr.next
        n*=-1
        if n==0:
            return head.next
        i=1
        curr=head
        while i<n:
            curr=curr.next
            i+=1
        curr.next=curr.next.next if curr.next else None
        return head
        

    

    

    