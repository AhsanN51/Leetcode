class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
      
        """
        d={}
        for i in nums1:
            d[i]=d.get(i,0)+1
        r=[]
        for i in nums2:
            if i in d and d[i]>0:
                r.append(i)
                d[i]-=1
        return r
