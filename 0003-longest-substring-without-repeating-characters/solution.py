class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0

        ansl=[]
        set1=set({})
        set1.add(s[0])

        i=0
        j=1

        while j<len(s):
            while s[j] in set1 :
                set1.discard(s[i])
                i+=1
            set1.add(s[j])
            j+=1
            ansl.append(s[i:j])
        maxl=0
        for ans in ansl:
            maxl=max(maxl,len(ans))
        return maxl if maxl>0 else 1

