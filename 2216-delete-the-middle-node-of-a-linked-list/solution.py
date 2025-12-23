# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None
        s,f=head,head
        while f and f.next:
            prev=s
            s=s.next
            f=f.next.next
        prev.next=s.next
        return head
