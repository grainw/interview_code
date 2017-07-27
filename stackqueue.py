class Solution:
    def __init__(self):
        self.stack1= []
        self.stack2 = []
    def push(self,value):
        self.stack1.append(value)
    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()

class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2==[]:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()
q = Solution()
q.push(1)
print q.stack1
q.pop()
print q.stack1
q.push(2)
print q.stack1
q.push(3)
print q.stack1
q.pop()
print q.stack1

