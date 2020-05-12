class Node:
    def __init__(self,name,typ):
        self.name = name
        self.typ = typ
        self.next = None
    
    def __str__(self) -> str:
        return str(self.name)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        if self.tail == None and self.head == None:
            return True
        else:
            return False


    def enQueue(self, name, typ):
        if self.head == None:
            a: Node = Node(name,typ)
            self.head = a
            self.tail = a
        else:
            a: Node = Node(name,typ)
            a.next = self.tail
            self.tail = a

    def deQueueAny(self):
        if self.isEmpty():
            raise Exception("Queue is already Empty")
        if self.tail == self.head:
            ret = self.tail
            self.tail = None
            self.head = None
            return ret
        a:Node = self.tail
        while a.next != self.head:
            a=a.next
        ret = a.next
        self.head = a

        return ret

    def deQueueDog(self):
        count :int =0
        position: int =-1
        ret: Node = Node("","")
        a:Node = self.tail
        while a != None:
            if a.typ == "dog":
                position = count
            count+=1
            a=a.next
        if count == 1:
            if position == 0:
                ret = self.head
                self.head = None
                self.tail = None
                return ret
        a =self.tail
        for i in range(position-1):
            a=a.next
        if a.next == self.head:
            ret = self.head
            self.head = a
            self.head.next = None
        else:  
            ret = a.next
            a.next = a.next.next
        return ret

    def deQueueCat(self):
        count :int =0
        position: int =-1
        ret: Node = Node("","")
        a:Node = self.tail
        while a != None:
            if a.typ == "cat":
                position = count
            count+=1
            a=a.next
        if count == 1:
            if position == 0:
                ret = self.head
                self.head = None
                self.tail = None
                return ret
        a =self.tail
        for i in range(position-1):
            a=a.next
        if a.next == self.head:
            ret = self.head
            self.head = a
            self.head.next = None
        else:  
            ret = a.next
            a.next = a.next.next
        return ret


    def __str__(self) ->str:
        a:str = ""
        if self.isEmpty():
            return "Empty"
        temp:Node = self.tail
        while temp != self.head:
            a+= str(temp)+"  "
            temp=temp.next
        a+=str(self.head)
        return a

q= Queue()
q.enQueue("d1","dog")
q.enQueue("c1","cat")
q.enQueue("d2","dog")
q.enQueue("c2","cat")
q.enQueue("d3","dog")
q.enQueue("c3","cat")
print(q)
a=q.deQueueDog()
print(q)
print(a)
a=q.deQueueDog()
print(q)
print(a)
a=q.deQueueDog()
print(q)
print(a)
a=q.deQueueCat()
a=q.deQueueCat()
a=q.deQueueCat()
print(q)
print(a)
