class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sk=[]
        for i in s:
            if i=='('or i== '{' or i=='[':
                sk.append(i)
            else:
                if len(sk)==0:
                    return False
                top=sk.pop()
                if i==')' and top!='(':
                    return False
                if i=='}' and top!='{':
                    return False
                if i==']' and top!='[':
                    return False
        if len(sk)!=0:
            return False
        return True
