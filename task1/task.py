import json
import os
print(os.getcwd())
def parseGraph(node, graph):
    for key, value in node.items():
        if key not in graph:
            graph[key] = []

        for child in value:
            graph[key].append(child)
            parseGraph({child: value[child]}, graph)
        
        if not value:
            graph[key] = []


def parseJson(fileName):
    graph = {}
    with open(fileName, 'r') as jsonFile:
        data = json.load(jsonFile)
        parseGraph(data, graph)
        print(graph)
        return graph

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
        
if __name__ == "__main__":
    graph = {}
    fileName = './task1/test2.json'
    graph = parseJson(fileName=fileName)

    for key, value in graph.items():
        print(f"{key}: {value}")

    descendants = getDescendants(graph=graph, num='3')
    neibs = getNeib(graph=graph, num="3")
    print("descendants", descendants)
    print("neibs", neibs)


