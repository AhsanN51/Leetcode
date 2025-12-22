class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i,val in enumerate(nums):
            if val in d and abs(i-d[val])<=k:
                return True
            else:
                d[val]=i
        return False
