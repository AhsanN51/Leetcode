# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        c1=list1
        c2=list2
       
        d=ListNode(-1)
        cur=d
        while c1 and c2:
            if c2.val<=c1.val:
                cur.next=c2
                c2=c2.next 
            else:
                cur.next=c1
                c1=c1.next
            cur=cur.next
        if c1:
            cur.next=c1
        elif c2:
            cur.next=c2
        return d.next

