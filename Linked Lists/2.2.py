from LinkedClass import linkedList,Node

def returnKthToLast(f:linkedList,k:int):
    re: Node = f.head
    fast: Node = f.head
    for i in range(k):
        fast = fast.next
    while fast != None:
        re=re.next
        fast=fast.next

    return re


a: Node = Node(3)
b: Node = Node(4)
c: Node = Node(2)
d: Node = Node(9)
e: Node = Node(1)
f: Node = Node(8)
g: Node = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

v:linkedList = linkedList(a)

print(v)

a:int = returnKthToLast(v,4)

print(a)
