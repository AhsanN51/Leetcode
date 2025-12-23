# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        prv=None
        nxt=None
        cur =s
        while cur:
            nxt=cur.next
            cur.next=prv
            prv=cur
            cur=nxt
        while head and prv:
            if head.val!=prv.val:
                return False
            else:
                head=head.next
                prv=prv.next
        return True
