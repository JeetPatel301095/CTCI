from typing import DefaultDict
from collections import defaultdict

def palindromePermutation(a:str) ->bool:
    a=a.lower()
    count: int =0
    b: DefaultDict(str,int) = defaultdict(int)
    for i in a:
        if i == " ":
            continue
        b[i]+=1
    for i in b.values():
        if i%2 ==0:
            continue
        else:
            count+=1
    if count>1:
        return False
    else:
        return True
    print(b)

c = palindromePermutation("Tact Coa")
print(c)
c = palindromePermutation("itnin")
print(c)