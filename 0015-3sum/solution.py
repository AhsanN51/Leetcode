class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=sorted(nums)
        dic=[]
        
        for i,v in enumerate(n):
            target=-v
            l=i+1
            r=len(n)-1
            while l<r:
                val=n[l]+n[r]
                if val==target:
                    ls=[v,n[l],n[r]]
                    if ls not in dic:
                        dic.append(ls)
                    l+=1
                    r-=1
                    while (l<r) and n[l]==n[l-1]:
                        l+=1
                    
                elif val<target:
                    l+=1
                elif val>target:
                    r-=1
        return dic
