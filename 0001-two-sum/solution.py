class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            v=target-nums[i]
            if v in dic:
                return [i,dic[v]]
            else:
                dic[nums[i]]=i
