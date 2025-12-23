# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head
        last=head
        l=1
        while last.next:
            l+=1
            last=last.next
        print(l,last.val)
        k=k%l
        cur=head
        for i in range(l-k-1):
            cur=cur.next
        last.next=head
        head=cur.next
        cur.next=None
        return head

        
