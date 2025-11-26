class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #COUNTING SORT METHOD
        n=len(nums)
        mx=max(nums)

        freq=[0]*(mx+1)

        for i in nums:
            freq[i]+=1
        
        print(freq)
        
        nums[:]=[]

        for i in range(0,mx+1):
            while freq[i]>0:
                nums.append(i)
                freq[i]-=1
        
        return nums
