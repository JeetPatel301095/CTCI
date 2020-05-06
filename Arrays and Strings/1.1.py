from typing import DefaultDict
from collections import defaultdict

def isUnique(a:str) ->bool:
    b:Dict[str,int] = defaultdict(int)
    for i in a:
        if b[i]==1:
            return False
        b[i]+=1
    print(b)
    return True

c=isUnique("abca")
print(c)