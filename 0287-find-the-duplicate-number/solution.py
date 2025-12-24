class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=nums[0]
        f=nums[0]
        while True:
            s=nums[s]
            f=nums[nums[f]]
            if s==f:
                break
        p1=nums[0]
        p2=s
        while p1!=p2:
            p1=nums[p1]
            p2=nums[p2]
        return p1
