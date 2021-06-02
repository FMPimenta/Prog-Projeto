from Person import Person
from Edge import Edge
from Graph import Graph

def readNetwork(filename):
    """
    Read the social network input file

    Requires:filename is string with the name of the social network file
    Ensures: a list containing lists that each contain the parameters of a single
    element of the given social network
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

def generateEdges(network):
    """
    Generate the edges that represent each contact between 2 elements of the social network

    Requires: network is a list containing lists that contain the parameters of a single
    element of the given social network
    Ensures: a list containing all edges needed to represent all the contacts between all elements of
    the given social network
    """

    edges = []
    
    for person in network:
        src = person
        for contactID in person.getDirect():
            for contact in network:
                if contactID == contact.getIdNb():
                    dest = contact
                    edge = Edge(src, dest)

            if edge not in edges:
                edges.append(edge)

    return edges

def generateGraph(network, edges):
    """
    Generate a Graph object where the nodes are the elements of the social network
    and the edges depict all direct contacts that each element has with other elements

    Requires: network is a list containing lists that contain the parameters of a single
    element of the given social network and edges is a list containing all edges necessary
    to represent the social network accurately.
    Ensures: A new Graph object
    """

    g = Graph()

    for person in network:
        g.addNode(person)

    for edge in edges:
        g.addEdge(edge)

    

network = readNetwork("socialNetwork.txt")
edges = generateEdges(network)
graph = generateGraph(network, edges)
print(graph)






















































































