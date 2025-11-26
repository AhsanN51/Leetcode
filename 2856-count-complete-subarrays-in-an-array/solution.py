class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        discnum=len(set(nums))

        ansl=0

        for i in range(len(nums)):
            dic={}
            for j in range(i,len(nums)):
                if nums[j] in dic:
                    dic[nums[j]]+=1
                else:
                    dic[nums[j]]=1
                if len(dic) == discnum:
                    ansl += 1
            """print(dic)
            for val in dic.values():
                if val<discnum:
                    continue
            print(f"not pass {dic}")
            ansl+=1    """    

        return ansl
