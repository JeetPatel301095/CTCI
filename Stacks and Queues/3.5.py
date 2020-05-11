
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def __str__(self) -> str:
        return str(self.val)

class Stack:
    def __init__(self):
        self.top = None

    def push(self,item):
        a: Node = Node(item)
        flag:bool = False
        if self.top == None:
            self.top = a
        else:
            if self.top.val>item:
                a.next = self.top
                self.top = a
            else:
                r:Node = self.top
                while r.next != None:
                    if r.next.val>item:
                        a.next = r.next
                        r.next = a
                        flag = True
                        break
                    r = r.next
                if not flag:
                    r.next = a
                

    def pop(self):
        if self.isEmpty():
            raise Exception("Sorry, The Stack is Already Empty")
        ret = self.top.val
        self.top = self.top.next
        return ret

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.val

    def isEmpty(self) ->bool:
        if self.top == None:
            return True
        return False

    def __str__(self) -> str:
        a:str = ""
        temp:Node = self.top
        while temp != None:
            a+= str(temp)+"  "
            temp=temp.next
        return a

s= Stack()
print(s.isEmpty())
s.push(2)
s.push(3)
s.push(1)
s.push(6)
s.push(4)
s.push(5)
print(s)
print(s.pop())
print(s)
print(s.peek())
print(s.isEmpty())