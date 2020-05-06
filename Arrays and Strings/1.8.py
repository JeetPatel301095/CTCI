from typing import List

def zeroMatrix(a:List[List[int]]) ->List[List[int]]:
    rowList: List[int] = list()
    colList: List[int] = list()
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                if i not in rowList:
                    rowList.append(i)
                if j not in colList:
                    colList.append(j)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i in rowList or j in colList:
                a[i][j]=0
        
    return a

c : List[List[int]] = [[1,2,3,0],[4,5,0,11],[7,8,9,12],[0,14,15,16]]
d = zeroMatrix(c)
print(d)