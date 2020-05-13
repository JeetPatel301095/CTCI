from typing import Dict,List

class Graph:
    def __init__(self):
        self.nodeSet = set()
        self.graphDict :Dict[int,List[int]] = dict()

    def addEdge(self,v1,v2):
        self.nodeSet.add(v1)
        self.nodeSet.add(v2)
        if v1 not in self.graphDict.keys():
            r: List[int] = list()
            r.append(v2)
            self.graphDict[v1] = r
        else:
            self.graphDict[v1].append(v2)
        

    def isRoute(self,v1,v2):
        ans = ""
        print(v1,v2)
        if v1 not in self.nodeSet or v2 not in self.nodeSet:
            ans= v1 if v1 not in self.nodeSet else v2
        if v1 not in self.graphDict.keys() and v2 not in self.graphDict.keys():
            ans= "No Edges with these vertices"
        if v2 in self.graphDict[v1]:
            ans = "Route Exists"
        else:
            for i in self.graphDict[v1]:
                ans=self.isRoute(i,v2)
        
        return ans


g:Graph = Graph()

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(5,1)

a=g.isRoute(1,5)

print(a)
print(g.graphDict)
print(g.nodeSet)