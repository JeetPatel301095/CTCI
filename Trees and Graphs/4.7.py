def BuildOrder(proj,depend):
    listDict = dict()
    workOrder = list()
    for i in proj:
        listDict[i] = list()
    for i in depend:
        listDict[i[1]].append(i[0])
    while len(listDict.keys())!=0:
        j = len(listDict.keys())
        for i in listDict.copy().keys():
            if len(listDict[i]) == 0:
                workOrder.append(i)
                listDict.pop(i)
                for k in listDict.copy().keys():
                    if i in listDict[k]:
                        listDict[k].remove(i)
        if j == len(listDict.keys()):
            raise Exception("Work Order Cannot be Created")
    return workOrder

proj = ["a","b","c","d","e","f"]
depend = [["a","d"],["f","b"],["b","d"],["f","a"],["d","c"],["e","f"],["f","e"]]
try:
    a=BuildOrder(proj,depend)
    print(a)
except Exception as e:
    print(e)