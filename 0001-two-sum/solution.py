class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            dif=target-nums[i]
            if dif in dic:
                return [dic[dif],i]
            else:
                dic[nums[i]]=i
            #print(dic)
