class Stack:
    def __init__(self):
        self.stacklist = list()
    
    def push(self,item):
        # print(item)
        self.stacklist.append(item)
    
    def pop(self)->int:
        return self.stacklist.pop()

    def isEmpty(self)->bool:
        if len(self.stacklist) == 0:
            return True
        else:
            return False

class myQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def push(self,item):
        self.s1.push(item)

    def pop(self)->int:
        ans:int =0
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())
        ans = self.s2.pop()
        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())
        return ans

    def __str__(self):
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())
        ans = self.s2.stacklist.copy()
        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())
        return str(ans)


a:myQueue = myQueue()
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)
a.push(7)
a.push(8)
a.push(9)

print(a.pop())
print(a)