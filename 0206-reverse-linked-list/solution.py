# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur=head
        prv=None
        nxt=None
        while cur:
            nxt=cur.next
            cur.next=prv
            prv=cur
            cur=nxt
        head=prv
        return head
