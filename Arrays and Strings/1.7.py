from typing import List

def rotateMatrix(a:List[List[int]]) ->List[List[int]]:
    ans:List[List[int]] = [[0 for x in range(len(a))] for y in range(len(a))]
    lenMat = len(a) -1
    for i in range(len(a)):
        for j in range(len(a[i])):
            ans[lenMat-j][i] = a[i][j]
    return ans

c : List[List[int]] = [[1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,15,16]]
d = rotateMatrix(c)
for i in d:
    print(i)