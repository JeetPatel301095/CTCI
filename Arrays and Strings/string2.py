from collections import defaultdict
from typing import DefaultDict

def checkPermutation(a:str,b:str) -> bool:
    c:DefaultDict[str,int] = defaultdict(int)
    for i in a:
        c[i]+=1
    for i in b:
        c[i]-=1
    for j in c.values():
        if j !=0:
            return False
    return True

c = checkPermutation("abc","cba")
print(c)