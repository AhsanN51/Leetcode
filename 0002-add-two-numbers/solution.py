# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        c1=l1
        c2=l2
        ans=ListNode(-1)
        ca=ans
        car=0
        while c1 or c2:
            s=car
            car=0
            
            s+=c1.val if c1 else 0
            s+=c2.val if c2 else 0

            c1=c1.next if c1 else None
            c2=c2.next if c2 else None

            if s>9:
                car=1
                s=s-10
            cur=ListNode(s)
            ca.next=cur
            ca=ca.next   
        if car>0:
            cur=ListNode(car)
            ca.next=cur   
        return ans.next
