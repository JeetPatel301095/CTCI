
class Node: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None
        self.parent = None

def sortedArrayToBST(arr ,a = None):
    if not arr: 
        return None

    mid = (len(arr)) // 2
    root = Node(arr[mid])
    if a!= None:
        root.parent = a
    root.left = sortedArrayToBST(arr[:mid],root) 
    root.right = sortedArrayToBST(arr[mid+1:],root) 
    return root 

def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.data,end=" ")  
        inOrder(root.right)



def Successor(val, root):
    a = locateNode(val,root)

    if a.right == None:
        b= a.parent
    else:
        return a.right
    if a==b.right:
        t= root
        while t.right!= None:
            t=t.right
        if t == a:
            print("The Entered Node is the Last Node")
            return None
        else:
            c= b.parent
            return c
    else:
        return b

def locateNode(val,root):
    if val == root.data:
        return root
    elif val<root.data:
        b=locateNode(val,root.left)
        return b
    else:
        b=locateNode(val,root.right)
        return b
        
                
            


arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(arr) 
print("PreOrder Traversal of constructed BST ")
inOrder(root)
print()
x = Successor(1,root)
print(1,x.data)
x = Successor(2,root)
print(2,x.data)
x = Successor(3,root)
print(3,x.data)
x = Successor(4,root)
print(4,x.data)
x = Successor(5,root)
print(5,x.data)
x = Successor(6,root)
print(6,x.data)
x = Successor(7,root)
if x != None:
    print(7,x.data)


# This code is contributed by Ishita Tripathi 
