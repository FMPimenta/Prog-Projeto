# 2019-2020 Programação 2 (LTI)
# Grupo 1
# 54973 Francisco Pimenta
# 55477 Oleksandra Butyrska

import sys
from Person import Person
from Edge import Edge
from Graph import Graph


def printPath(path):
    """
    Path in string form

    Requires: path a list of nodes
    Ensures: the path in string form
    """

    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result



def propagationTime(path, network):
    '''
    Calculates the propagation time between the source and destination of a path

    Requires: path is a list containing the nodes of the path and network is a
    list which contains all Person tpye objects in the social network
    Ensures: the propagation time between the source and the destination of the
    given path in hours
    '''

    totalTime = 0
    i = 0

    #For every 2 consecutive elements of the path list calculates the propagation time
    #between them
    while i+1 < len(path):
        src = Person.stringToPerson(path[i], network)
        dest = Person.stringToPerson(path[i+1], network)
        edge = Edge(src, dest)
        
        totalTime += edge.getWeight()
        i += 1
    
    return totalTime



def writeOutput(outputFileName, outputLine):
    '''
    Writes a given string in the given output file

    Requires: outputFileName, outputLine are string
    Ensures: If a file with the name in outputFileName doesn't exist creates
    it and writes the string in the outputLine, otherwise it appends the
    given string to the end of the file
    '''

    outputFile = open(outputFileName, 'a')

    outputFile.write(outputLine)

    outputFile.close()

    

def DFS(graph, network, source, destination, path, shortest):
    """
    Finds the shortest path between two given nodes

    Requires:
    graph a Graph type object;
    source and destination are strings with the name of a node in the graph;
    path and shortest lists of nodes
    Ensures: a path from source to destination in graph where the total
    weight of the edges is the least possible
    """
    
    path = path + [source]
    if source == destination:
        return path
    for node in graph.childrenOf(source):
        if node not in path and Person.stringToPerson(node, network).getImmune()\
        == "No":
            if shortest == None or propagationTime(path, network) <\
            propagationTime(shortest, network):
                newPath = DFS(graph, network, node, destination, path, shortest)
                if newPath != None:
                    shortest = newPath

    return shortest



def search(graph, network, source, destination):
    """
    Wrapper method for DFS

    Requires:
    graph  a Graph;
    source and destination are nodes
    Ensures: a path from source to destination in graph where the total weight
    of the edges is the least possible
    """

    outputFileName = sys.argv[3]

    
    if Person.stringToPerson(source, network).getImmune() == "No":
        searchResult = DFS(graph, network, source, destination, [], None)
        if searchResult != None:
            writeOutput(outputFileName, \
            str(f'{propagationTime(searchResult, network)} \n'))
        else:
            writeOutput(outputFileName, str('No contagion between ' + source + \
            ' and ' + destination + ".\n"))
    else:
        writeOutput(outputFileName, str('No contagion between ' + source + \
        ' and ' + destination + ".\n"))




        
