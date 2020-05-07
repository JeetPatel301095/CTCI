from LinkedClass import linkedList,Node

def deleteMiddle(ll1:linkedList) ->None:
    print(ll1)
    re:Node = ll1.head
    double:Node = ll1.head.next.next
    while double.next != None and double.next.next != None:
        re=re.next
        double= double.next.next
    re.next = re.next.next


a: Node = Node(1)
b: Node = Node(2)
c: Node = Node(3)
d: Node = Node(4)
e: Node = Node(5)
f: Node = Node(6)
# g: Node = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# f.next = g

v:linkedList = linkedList(a)

# print(v)

deleteMiddle(v)

print(v)