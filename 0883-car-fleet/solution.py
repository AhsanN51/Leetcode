class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pr=[(p,s) for p,s in zip(position,speed)]
        pr.sort(reverse=True)
       # print(pr)
        st=[]
        for p,s in pr:
            st.append(float(target-p)/s)
            if len(st)>=2 and st[-1] <=st[-2]:
                st.pop()
        return len(st)



