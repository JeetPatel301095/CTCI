

class Stack:
    def __init__(self,capacity):
        self.currentStack = list()
        self.stackDict:Dict[int,List[int]] = dict()
        self.counter = 0
        self.capacity = capacity

    def push(self,item):
        if len(self.currentStack) < self.capacity:
            self.currentStack.append(item)
        else:
            temp:List[int] = self.currentStack.copy()
            self.stackDict[self.counter] = temp
            self.counter+=1
            self.currentStack.clear()
            self.currentStack.append(item)

    def pop(self) ->int:
        if len(self.currentStack) == 0:
            if len(self.stackDict) != 0:    
                if len(self.stackDict) == self.counter:
                    self.counter-=1
                self.currentStack = self.stackDict.pop(self.counter)
                self.counter-=1    
        self.currentStack.pop()

    def popAt(self, stackNumber):
        if len(self.stackDict) == 0:
            raise Exception("Sorry the Stack is Empty")
        if stackNumber == len(self.stackDict):
            self.currentStack.pop()
        elif stackNumber < len(self.stackDict):
            self.stackDict[stackNumber].pop()
        else:
            raise Exception("No such Stack")
        


s= Stack(10)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)

s.pop()
s.pop()
s.pop()
s.pop()

s.popAt(1)
s.popAt(2)

print(s.stackDict)
print(s.currentStack)