from typing import Dict

class TreeNode:
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def minimalTree(arr, root, i): 
    if i < len(arr): 
        temp = TreeNode(arr[i])  
        root = temp

        root.left = minimalTree(arr, root.left, 2 * i + 1)

        root.right = minimalTree(arr, root.right, 2 * i + 2)
    return root

def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.data,end=" ")  
        inOrder(root.right)

def listOfDepths(nodeDict,level,root):
    if root == None:
        return
    # print(root.data)
    if level not in nodeDict.keys():
        a = ListNode(root.data)
        nodeDict[level] = a
    else:
        temp = nodeDict[level]
        while temp.next != None:
            temp = temp.next
        a = ListNode(root.data)
        temp.next = a

    listOfDepths(nodeDict,level+1,root.left)
    listOfDepths(nodeDict,level+1,root.right)
        


arr = [1, 2, 3, 4, 5, 6, 6, 6, 6] 
n = len(arr) 
root = None
root = minimalTree(arr, root, 0)  
inOrder(root)
print()
nodeDict : Dict[int,ListNode] = dict()
print(nodeDict)
listOfDepths(nodeDict,0,root)

for keys in nodeDict.keys():
    temp = nodeDict[keys]
    while temp !=None:
        print(f"{temp.val}  --> ",end="")
        temp = temp.next
    print("None")