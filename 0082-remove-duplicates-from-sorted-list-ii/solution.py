# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dn=ListNode(-101,head)
        cr=head
        prev=dn
        while cr:
            f=False
            while cr.next!=None and cr.val==cr.next.val  :
                cr=cr.next
                f=True
            if f:
                prev.next=cr.next
            else:
                prev=prev.next
            cr=cr.next
        return dn.next

