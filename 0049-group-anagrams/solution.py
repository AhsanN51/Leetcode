class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for st in strs:
            sl=list(st)
            sl.sort()
            s="".join(sl)
            print(st)
            if s in dic:
                dic[s].append(st)
            else:
                dic[s]=[st]
        return dic.values()            
