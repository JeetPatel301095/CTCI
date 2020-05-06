from typing import DefaultDict
from collections import defaultdict

def oneAway(a1:str,a2:str) -> bool:
    if a1==a2:
        return True
    if len(a1)-len(a2)>1:
        return False
    if len(a1) == len(a2):
        b1: DefaultDict = defaultdict(int)
        b2: DefaultDict = defaultdict(int)
        count: int = 0
        for i in a1:
            b1[i]+=1
        for i in a2:
            b2[i]+=1
        for i in b1.keys():
            if b1[i] != b2[i]:
                count+=1
        if count>1:
            return False
        else:
            return True
    else:
        b1: DefaultDict = defaultdict(int)
        b2: DefaultDict = defaultdict(int)
        count: int = 0
        for i in a1:
            b1[i]+=1
        for i in a2:
            b2[i]+=1
        for i in b1.keys():
            if b1[i] != b2[i]:
                count+=1
        if count>1:
            return False
        else:
            return True

c = oneAway("pale","bake")
print(c)
c = oneAway("pales","pale")
print(c)
c = oneAway("pale","ple")
print(c)
c = oneAway("pale","bale")
print(c)