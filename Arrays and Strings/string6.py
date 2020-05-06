from typing import List

def stringComprehension(a:str) -> str:
    ans: List[str] = list()
    i:int = 0
    while i < len(a):
        key: str = a[i]
        j:int = i+1
        count: int = 1
        while True:
            if j == len(a):
                ans.append(key)
                ans.append(str(count))
                break
            if a[j] == key:
                count+=1
                j+=1
            else:
                ans.append(key)
                ans.append(str(count))
                break
        i+=count
    return "".join(ans)

a:str = stringComprehension("aabccccc")
print(a)