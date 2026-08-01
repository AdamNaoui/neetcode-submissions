# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,node:ListNode):
        if not node:
            return None
        
        curr=node
        prev=None

        while curr:
            next_curr=curr.next    
            curr.next=prev
            prev=curr
            curr=next_curr
            
        
        return prev
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversed_l1=l1
        reversed_l2=l2

        res=None
        curr=None
        carry_on=0

        while reversed_l1 or reversed_l2:
            l1_val= reversed_l1.val if reversed_l1 else 0
            l2_val= reversed_l2.val if reversed_l2 else 0

            summ=l1_val+l2_val+carry_on

            new_val=summ % 10
            new_node=ListNode(new_val)

            carry_on=summ//10
            if reversed_l1:
                reversed_l1=reversed_l1.next
            if reversed_l2:
                reversed_l2=reversed_l2.next
            
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

        

            

