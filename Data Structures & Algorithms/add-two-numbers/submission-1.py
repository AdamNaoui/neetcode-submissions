# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=None
        curr=None
        carry_on=0

        while l1 or l2:
            l1_val= l1.val if l1 else 0
            l2_val= l2.val if l2 else 0

            summ=l1_val+l2_val+carry_on

            new_val=summ % 10
            new_node=ListNode(new_val)

            carry_on=summ//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            
            if not res:
                res=new_node
                curr=new_node
                continue
            
            curr.next=new_node
            curr=curr.next
        
        if carry_on:
            new_node=ListNode(1)
            curr.next=new_node
            
        return res

        

            

