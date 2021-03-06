# Tree from an array

class newNode:
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

def insertLevelOrder(arr, root, i): 
    if i < len(arr): 
        temp = newNode(arr[i])  
        root = temp

        root.left = insertLevelOrder(arr, root.left, 2 * i + 1)

        root.right = insertLevelOrder(arr, root.right, 2 * i + 2)
    return root

def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.data,end=" ")  
        inOrder(root.right)

arr = [1, 2, 3, 4, 5, 6, 6, 6, 6] 
n = len(arr) 
root = None
root = insertLevelOrder(arr, root, 0)  
inOrder(root)