from LinkedClass import linkedList,Node
from typing import List

def removeDups(a:linkedList) ->None:
    re: Node = a.head
    visited: List[int] = [re.val]
    while re.next != None:
        if re.next.val not in visited:
            visited.append(re.next.val)
        else:
            re.next = re.next.next
            continue
        re= re.next



a: Node = Node(3)
b: Node = Node(3)
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

removeDups(v)

print(v)

