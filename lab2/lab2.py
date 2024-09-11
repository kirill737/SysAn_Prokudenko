import sys
sys.path.append("./lab1")
from lab1 import parseJson

def getDescendants(graph, num, descendants=[]):
    if num in graph:
        descendants += graph[num]
        for node in graph[num]:
            getDescendants(graph=graph, num=node, descendants=descendants)
    return descendants

def getNeib(graph, num):
    for _, neib in graph.items():
        if num in neib:
            return neib

graph = {}
parseJson("./lab1/test.json", graph)

descendants = getDescendants(graph=graph, num='4')
neibs = getNeib(graph=graph, num="4")
print("descendants", descendants)
print("neibs", neibs)
