class Stack:
    def __init__(self):
        self.stackList = list()
        self.minList = list()

    def push(self,item:int):
        self.stackList.append(item)
        if len(self.minList) == 0:
            self.minList.append(item)
        else:
            if self.minList[(len(self.minList)-1)]>item:
                self.minList.append(item)
            else:
                self.minList.append(self.minList[(len(self.minList)-1)])
    
    def pop(self) -> int:
        if len(self.stackList) == 0:
            raise Exception("Sorry Nothing in the Stack to Pop")
        else:
            self.minList.pop()
            return self.stackList.pop()

    def __str__(self):
        return str(self.stackList)

    def Min(self):
        return str(self.minList[len(self.minList)-1])

s: Stack = Stack()

s.push(2)
print(s)
print(s.Min())
s.push(4)
print(s)
print(s.Min())
s.push(3)
print(s)
print(s.Min())
s.push(1)
print(s)
print(s.Min())
s.pop()
print(s)
print(s.Min())