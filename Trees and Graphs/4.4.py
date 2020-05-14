# Tree from an array

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

def checkBalance(root):
    i,val = parse(root)
    print(i)
    return val

def parse(root):
    if root == None:
        return (-1,True)
    i,val1 = parse(root.left)
    j,val2 = parse(root.right)
    if not val1 or not val2:
        return (i if i>j else j,False)
    i,j = i+1,j+1
    if i-j > 1 or j-i > 1:
        return (i if i>j else j, False)
    else:
        return (i if i>j else j, True)

arr = [1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 8, 7, 5, 4] 
n = len(arr) 
root = None
root = minimalTree(arr, root, 0)  
inOrder(root)
print()
b = checkBalance(root)
print(b)