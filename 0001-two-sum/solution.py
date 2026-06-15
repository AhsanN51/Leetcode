class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s ={}
        for i,v in enumerate(nums):
            n=target-v
            if n in s:
                return [i,s[n]]
            s[v]=i

