
class newNode:
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

def Tree(arr, root, i): 
    if i < len(arr): 
        temp = newNode(arr[i])  
        root = temp

        root.left = Tree(arr, root.left, 2 * i + 1)

        root.right = Tree(arr, root.right, 2 * i + 2)
    return root

def commonAncestor(root,n1,n2):
    a = check(root,n1,n2)
    if a[1] and a[2]:
        return a
    else:
        raise Exception("Either node doesn't Exist")

def check(root,n1,n2):
    n1f,n2f = False,False
    if root.data == n1.data:
        n1f= True
    if root.data == n2.data:
        n2f = True

    if root.left == None and root.right != None:
        a = check(root.right,n1,n2)
        if a[1] == a[2] == True:
            if a[0]!= None:
                return (a[0],True,True)
    if root.right == None and root.right != None:
        a = check(root.left,n1,n2)
        if a[1] == a[2] == True:
            if a[0]!= None:
                return (a[0],True,True)
    if root.left == None and root.right == None:
        return (None,n1f,n2f)
    
    a = check(root.left,n1,n2)
    b = check(root.right,n1,n2)
    if n1f:
        if a[2]:
            return (None,True,True)
        if b[2]:
            return (None,True,True)
    if n2f:
        if a[1]:
            return (None,True,True)
        if b[1]:
            return (None,True,True)

    if a[0] != None:
        return (a[0],True,True)
    elif b[0] != None:
        return (b[0],True,True)
    elif a[1] and b[2] == True or a[2] and b[1] == True:
        return (root,True,True)
    elif a[1] and a[2] == True:
        return (root,True,True)
    elif b[1] and b[2] == True:
        return (root,True,True)
    else:
        return (None,a[1] or b[1] or n1f, a[2] or b[2] or n2f)

    return (None,n1f,n2f)
    

def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.data,end=" ")  
        inOrder(root.right)

arr = [4,6,7,10,11,12,13,14,15,16,17] 
n = len(arr) 
root = None
root = Tree(arr, root, 0)  
n1 = newNode(17)
n2 = newNode(11)

inOrder(root)
print()
try:
    a=commonAncestor(root,n1,n2)
    print(a[0].data,a[1],a[2])
except Exception as e:
    print(e)