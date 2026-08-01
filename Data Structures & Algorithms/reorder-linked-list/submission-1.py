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
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        i=0
        while fast.next and fast.next.next:
            fast=fast.next.next
            i+=1
            slow=slow.next

        middle_next=slow.next
        if not middle_next:
            return 
        slow.next=None
        print(middle_next.val)
        right_part=self.reverseList(middle_next)
        left_part=head
        j=0
        print(i)
        while j<i+1:
            next_left=left_part.next
            if right_part:
                next_right=right_part.next
                left_part.next=right_part
                right_part.next=next_left

            left_part=next_left
            right_part=next_right
            j+=1
        
        

        