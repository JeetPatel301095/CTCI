
class newNode:
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

def minimalTree(arr, root, i): 
    if i < len(arr): 
        temp = newNode(arr[i])  
        root = temp

        root.left = minimalTree(arr, root.left, 2 * i + 1)

        root.right = minimalTree(arr, root.right, 2 * i + 2)
    return root

def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.data,end=" ")  
        inOrder(root.right)

def checkBinarySearchTree(root):
    a = parseLeft(root.left,root.data)
    b = parseRight(root.right,root.data)
    if not a or not b:
        return False
    else:
        return True

def parseLeft(root,max = None, min = None):
    if root == None:
        return
    if min != None and root.data<min:
        return False
    if max != None and root.data>max:
        return False
    a= parseLeft(root.left, root.data)
    b= parseRight(root.right, root.data, max)
    if a!= None:
        if not a:
            return False
    if b!= None:
        if not b:
            return False
    return True

def parseRight(root, min = None,max = None):
    if root == None:
        return
    if min != None and root.data<min:
        return False
    if max != None and root.data>max:
        return False
    a= parseLeft(root.left, root.data, min)
    b= parseRight(root.right, root.data)
    if a!= None:
        if not a:
            return False
    if b!= None:
        if not b:
            return False
    return True 

arr = [10,8,14,2,9,13,15]
n = len(arr) 
root = None
root = minimalTree(arr, root, 0)
inOrder(root)
print()
t = checkBinarySearchTree(root)
print(t)