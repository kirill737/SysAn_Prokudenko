import json

def parseGraph(graph, node, parent=None):
    for key, value in node.items():
        # print(key, value)
        if parent:
            if parent not in graph:
                graph[parent] = []
            graph[parent].append(key)
        if isinstance(value, dict):
            parseGraph(graph=graph, node=value, parent=key)

def parseJson(fileName, graph):
    try:
        with open(fileName, 'r') as jsonFile:
            data = json.load(jsonFile)
    except:
        print("Json file is not exist.")
    parseGraph(graph=graph, node=data)

if __name__ == "__main__":
    graph = {}
    fileName = './lab1/test.json'
    parseJson(fileName=fileName, graph=graph)

    for key, value in graph.items():
        print(f"{key}: {value}")


