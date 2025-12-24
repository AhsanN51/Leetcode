class MyQueue(object):

    def __init__(self):
        self.sk1=[]
        self.sk2=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while len(self.sk1)>0:
            self.sk2.append(self.sk1.pop())
        self.sk1.append(x)
        while len(self.sk2)>0:
            self.sk1.append(self.sk2.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.sk1.pop() 

    def peek(self):
        """
        :rtype: int
        """
        return self.sk1[-1] 

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.sk1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
