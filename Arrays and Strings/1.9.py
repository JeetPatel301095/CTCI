def isSubstring(s1:str,s2:str)->bool:
    if s2 in s1:
        return True
    else:
        return False
    
def stringRotation(s1:str,s2:str) ->bool:
    s3:str = s2+s2
    if isSubstring(s3,s1):
        return True
    else:
        return False

d = stringRotation("waterbottle","erbottlewat")
print(d)