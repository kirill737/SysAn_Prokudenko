import sys
import json
from math import log2
sys.path.append("./task1")




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
        return graph
# Сколькими управляет +
def calcR1(graph, num): 
    r1 = 0
    # for _, values in graph.items():
    #     if num in values:
    #         r1 += 1
    for key, values in graph.items():
        if key == num:
            r1 = len(values)
    return r1

# Сколько управляют им +
def calcR2(graph, num):
    r2 = 0
    for _, values in graph.items():
        if num in values:
            r2 += 1
    return r2

# Сколькими управляет через 1
def calcR3(graph, num): # Сколько опосред нач
    r3 = 0
    for el in graph[num]:
        r3 += len(graph[el])
    return r3

# Сколько управляют им через 1
def calcR4(graph, num): # Сколько опосред подч
    r4 = 0
    if num in graph:
        for value in graph[num]:
            r4 += len(graph[value])
    return r4

# Сколько соседей на одном уровне с общим начальником
def calcR5(graph, num):
    r5 = 0
    for _, values in graph.items():
        if num in values:
            r5 = len(values) - 1
            break
    return r5

def getTable(graph):
    table = []
    for i in range(len(graph)):
        table.append([
            calcR1(graph, str(i + 1)),
            calcR2(graph, str(i + 1)),
            calcR3(graph, str(i + 1)),
            calcR4(graph, str(i + 1)),
            calcR5(graph, str(i + 1))
        ])
    return table
        # print(f"{i + 1}: r1: {calcR1(graph, str(i + 1))} r2: {calcR2(graph, str(i + 1))} r3: {calcR3(graph, str(i + 1))} r4: {calcR4(graph, str(i + 1))} r5: {calcR5(graph, str(i + 1))}")
filename = './task1/test2.json'

def calcEnthropy(graph):
    table = getTable(graph)
    n = len(table)
    E = 0
    for row in table:
        H = 0
        for elem in row:
            if elem != 0:
                p = elem / (n - 1)
                H -= p * log2(p)
        E += H
    return E
# graph = parseJson(filename)
# print(graph.items()[0])
def main():
    graph = parseJson(filename)
    enthropy = calcEnthropy(graph)
    print(f"Энтропия: {round(enthropy, 3)}")