class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def __str__(self) -> str:
        return str(self.val)


class Stack:
    def __init__(self,top:Node = None):
        self.top = top

    def isEmpty(self) ->bool:
        if self.top == None:
            return True
        return False

    def push(self,item:int) -> None:
        temp:Node = Node(item)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.isEmpty():
            raise Exception("Sorry, The Stack is Already Empty")
        ret = self.top.val
        self.top = self.top.next
        return ret.val

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.val

    def __str__(self) -> str:
        a:str = ""
        temp:Node = self.top
        while temp != None:
            a+= str(temp)+"  "
            temp=temp.next
        return a

# a:Node = Node(2)
# b:Node = Node(3)
# c:Node = Node(4)
# d:Node = Node(5)
# s:Stack = Stack()
# s.push(b)
# s.push(c)
# s.push(d)
# print(s)
# print(s.peek())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.peek())
