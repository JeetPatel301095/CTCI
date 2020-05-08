class Node:
    __slots__ = ['val' , 'next']

    def __init__(self,val) ->None:
        self.val = val
        self.next = None

    def __str__(self) ->str: 
        return str(self.val)


class linkedList:
    __slots__ =['head','tail']

    def __init__(self,a:Node):
        self.head :Node = a

    def __str__(self) -> str:
        a:str = ""
        re: Node = self.head
        while re != None:
            a+=str(re)+"  "
            re = re.next
        return a


# a: Node = Node(4)
# b: Node = Node(3)
# c: Node = Node(2)
# d: Node = Node(1)

# a.next = b
# b.next = c
# c.next = d

# v:linkedList = linkedList(a)
# print(v)
            