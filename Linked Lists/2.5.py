from LinkedClass import linkedList,Node

def sumListReverseOrder(l1:linkedList,l2:linkedList) ->linkedList:
    ans:Node = Node(0)
    sum:int = 0
    ln1: Node = l1.head
    ln2: Node = l2.head
    carry: int = 0
    count:int=0
    ansList: linkedList = linkedList(ans)
    print(type(ansList))
    while ln1 != None and ln2 != None:
        if count == 0:
            print(type(ans))
            ans.val = (ln1.val+ln2.val)%10
            carry = (ln1.val+ln2.val)/10
            count+=1
        else:
            sum = ln1.val+ln2.val + int(carry)
            carry = sum/10
            temp: Node = Node(sum%10)
            ans.next=temp
            ans=ans.next
        ln1 = ln1.next
        ln2 = ln2.next
    return ansList

a1: Node = Node(7)
a2: Node = Node(1)
a3: Node = Node(6)

a1.next = a2
a2.next = a3

a: linkedList = linkedList(a1)


b1: Node = Node(5)
b2: Node = Node(9)
b3: Node = Node(2)

b1.next = b2
b2.next = b3

b: linkedList = linkedList(b1)

c = sumListReverseOrder(a,b)
print(c)