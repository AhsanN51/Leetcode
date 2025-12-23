# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dum=ListNode(0,head)
        cur=dum
        nums=set(nums)
        while cur.next:
            if cur.next.val in nums:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dum.next
