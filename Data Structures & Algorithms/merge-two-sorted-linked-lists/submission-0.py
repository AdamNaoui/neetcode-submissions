# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1,l2=list1,list2

        res=None
        curr=None
        if not l1:
            return l2
        if not l2:
            return l1
            
        while l1 and l2:
            print(l1,l2)
            if l1.val<l2.val:
                if curr:
                    curr.next=l1
                    curr=curr.next
                else:
                    curr=l1
                l1=l1.next
            else:
                if curr:
                    curr.next=l2
                    curr=curr.next
                else:
                    curr=l2
                l2=l2.next
            
            if not res:
                res=curr

        if curr is None:
            return None
        if l1:
            curr.next=l1
        if l2:
            curr.next=l2
        return res

    