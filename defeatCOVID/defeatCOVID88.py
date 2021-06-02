# 2019-2020 Programação 2 (LTI)
# Grupo 1
# 54973 Francisco Pimenta
# 55477 Oleksandra Butyrska

import sys
from DFS import *
from Edge import Edge
from Graph import Graph
from Person import Person


def readNetwork(filename):
    """
    Read the social network input file

    Requires:filename is string with the name of the social network file
    Ensures: a list containing lists that each contain the parameters of a
    single element of the given social network
    """

    fileIn = open(filename, 'r')

    outputList = []
    network = []

    for line in fileIn:
        #Placing each individual parameter of the line into a list
        lineList = line.replace("\n","").split(", ")
        #Extracting the list of direct contacts from the lineList
        directList = lineList[3:-2]
        #Deleting the copy of the direct contacts
        del lineList[3:-2]
        #Removing < and > from the direct contacts list
        for i in range(len(directList)):
            directList[i] = directList[i].strip("<>")
        #Appending all the direct contacts to the end of the list
        lineList.append(directList)
        outputList.append(lineList)
        
    fileIn.close()

    for parameters in outputList:
        #Creating a Person object from the parameters given by each line
        person = Person(parameters)
        #Appending each Person object to the network list
        network.append(person)
        
    return network


def readPairs(filename):
    """
    Read the TestSet input file with pairs of elements from the network.

    Requires:filename is string with the name of the TestSet file
    Ensures: a list containing lists with a pair of two names.
    """

    fileIn = open(filename, 'r')
    
    outputList = []

    for line in fileIn:
        pair = line.replace("\n","").split(" ")
        outputList.append(pair)
        
    return outputList
    fileIn.close()
    

def checkNode(nodeName):
    '''
    Checks if the given node is contained in the social network

    Requires: nodeName is a string
    Ensures: If the given node is not in the social network writes
    (nodeName out of social network.) in the output file, otherwise returns True
    '''

    #tries to find a Person object whose name attribute is equal to nodeName
    try:
        node = Person.stringToPerson(nodeName, network)
    #if it can't find one:
    except:
        writeOutput(outputFileName, (f'{pair[0]} out of the social network.\n'))
    else:
        return True



#receives arguments from the cmd
inputFileName1, inputFileName2, outputFileName = sys.argv[1:]

network = readNetwork(inputFileName1)
edges = Edge.generateEdges(network)
graph = Graph.generateGraph(network, edges)
pairs = readPairs(inputFileName2)

for pair in pairs:
    #checks if both nodes in the second input file are in the social network
    if checkNode(pair[0]) == True and checkNode(pair[1]) == True:
        searchResult = search(graph, network, pair[0], pair[1])






