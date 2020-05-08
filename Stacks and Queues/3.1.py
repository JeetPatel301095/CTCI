from StackClass import Stack,Node
from typing import List

def threeInOne(s1:Stack,s2:Stack,s3:Stack) ->List[int]:
    ans : List[int] = list()
    while not s1.isEmpty():
        ans.append(s1.pop())
    while not s2.isEmpty():
        ans.append(s2.pop())
    while not s3.isEmpty():
        ans.append(s3.pop())
    return ans


a1: Node = Node(2)
a2: Node = Node(3)
a3: Node = Node(4)
a4: Node = Node(5)
a5: Node = Node(6)
a6: Node = Node(7)

s1:Stack = Stack()
s2:Stack = Stack()
s3:Stack = Stack()

s1.push(a1)
s1.push(a2)
s1.push(a3)
s1.push(a4)
s1.push(a5)
s1.push(a6)

s2.push(a2)
s2.push(a1)
s2.push(a4)
s2.push(a3)
s2.push(a6)
s2.push(a5)

s3.push(a2)
s3.push(a3)
s3.push(a6)
s3.push(a1)
s3.push(a5)
s3.push(a4)

b = threeInOne(s1,s2,s3)
print(b)