class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            res=target-nums[i]
            if res in dic:
                return [dic[res],i]
            else:
                dic[nums[i]]=i



