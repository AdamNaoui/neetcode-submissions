# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        
        groups_count=count//k

        curr=head
        for i in range(groups_count):
            if i==0:
                next_tails=[curr]
            else:
                next_tails.append(curr)
            prev=None
            for j in range(k):
                next_curr=curr.next
                curr.next=prev
                prev=curr
                curr=next_curr

            print(prev.val)
            if i ==0:
                final_head=prev
            else:
                next_tail=next_tails.pop(0)
                next_tail.next=prev

            curr=next_curr
        
        if groups_count*k !=count:
            next_tail=next_tails.pop(0)
            next_tail.next=curr
        return final_head
                
