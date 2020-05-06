from typing import List

def URLify(a:str ,b:int)->str:
    a=a[:b]
    c:List[str] = a.split()
    for i in c.copy():
        if i == '':
            c.remove(i)
    d:str ="%20".join(c)
    return d

c = URLify("Mr    John Smith      ",16)
print(c)