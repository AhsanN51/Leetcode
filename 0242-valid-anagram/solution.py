class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        f1={}
        for c in s:
            if c in f1:
                f1[c]+=1
            else:
                f1[c]=1
        for c in t:
            if c in f1:
                f1[c]-=1
            else:
                return False
        for val in f1.values():
            if val!=0:
                return False
        return True

