class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=[]

    def push(self, val) :
        self.stack.append(val)
        if not self.mini:
            self.mini.append(val)
        else:
            val=min(val,self.mini[-1])
            self.mini.append(val)
            
    def pop(self) :
        if not self.stack:
            return None
        else:
            self.stack.pop()
            self.mini.pop()

    def top(self) :
        return self.stack[-1]

    def getMin(self):
        if not self.mini:
            return None
        else:
            return self.mini[-1]

