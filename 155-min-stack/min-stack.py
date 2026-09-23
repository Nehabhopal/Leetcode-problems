class MinStack(object):
    def __init__(self):
        self.items = []

    def push(self, val):
        self.val=val
        if len(self.items)==0:
            self.items.append([val,val])
        else:
            mini=min(self.items[-1][1],val)
            self.items.append([val,mini])
    
    def getMin(self):
        if len(self.items)==0:
            return 0
        return self.items[-1][1]
        
    def pop(self):
        if len(self.items)==0:
            print("stack has no items")
        x=self.items.pop()
        return x
    
    def top(self):
        if len(self.items)==0:
            print("stack has no items")
        return self.items[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()