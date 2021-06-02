# 2019-2020 Programação 2 (LTI)
# Grupo 1
# 54973 Francisco Pimenta
# 55477 Oleksandra Butyrska

class Node(object):
    def __init__(self, name):
        """
        Creates a Node object

        Requires: name is a string
        Ensures: A new Node object is created
        """
        
        self._name = name
        
    def getName(self):
        '''
        Name of the node.
        '''
        
        return self._name

    def setName(self, new_name):
        '''
        Attribute name is set to new_name
        
        Requires: name is a string
        Ensures: self._name == new_name
        '''

        self._name = new_name
        
    def __str__(self):
        '''
        Returns the name of the node
        '''
        
        return self.getName()

    def __eq__(self, other):
        '''
        Compares this node's name with another node's name

        Requires: other is a Node type object
        Ensures: If the nodes have the same name returns true otherwise returns false
        '''

        return True

class Edge(object):
    def __init__(self, src, dest):
        """
        Creates a Edge object

        Requires: src and dst are Node type objects
        Ensures: A new Edge object is created
        """
        
        self._src = src
        self._dest = dest
        
    def getSource(self):
        '''
        Source node of the edge
        '''
        
        return self._src

    def setSource(self, new_src):
        '''
        Attribute src is set to new_src

        Requires: new_src is a Node type object
        Ensures: self._src = new_src
        '''

        self._src = new_src
    
    def getDestination(self):
        '''
        Destination node of the edge
        '''
        
        return self._dest

    def setDestination(self, new_dest):
        '''
        Attribute dest is set to new_dest

        Requires: new_dest is a Node type object
        Ensures: self._dest = new_dest
        '''

        self._dest = new_dest
    
    def __str__(self):
        '''
        Returns the edge in string representation 
        '''
        
        return self._src.getName() + '->' + self._dest.getName()

    def __eq__(self, other):
        '''
        Compares this edge's source and destination with another edge's source
        and destinaton
        
        Requires: other is a Edge type object
        Ensures: If the edges have the same source and destination returns true otherwise returns false
        '''

        return self.getSource() == other.getSource() and self.getDestination() == other.getDestination()

class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each nodfe to a list of its children
    def __init__(self):
        '''
        Creates a Digraph object

        Ensures: A new Digraph object
        '''
        
        self._nodes = []
        self._edges = {}
        
    def addNode(self, node):
        '''
        Adds a node to the Digraph

        Requires: node is a Node type object
        Ensures: If its not on the nodes attribute, the node is added to the nodes attributes and to
        the edges dictionary with an empty list as a value
        '''
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []
            
    def addEdge(self, edge):
        '''
        Add an edge to the Digraph

        Requires: edge is a Edge type object
        Ensures: If its source and destination nodes are not in the nodes attribute of the current
        Diagraph instance raises an exception otherwise appends the edges's src atribute as a key and
        the dest attribute as a values of a element in the edges attribute
        '''
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src].append(dest)
        
    def childrenOf(self, node):
        '''
        Returns every node that is a child of the given node

        Requires: node is a Node type object in the nodes attribute
        Ensures: a list with every node that is a child of the given node
        '''
        
        return self._edges[node]
    
    def hasNode(self, node):
        '''
        Checks if given node is in the nodes attributes

        Requires: node must be a Node type object
        Ensures: True if node is in the nodes attribute list
        '''
        
        return node in self._nodes
    
    def __str__(self):
        '''
        Returns all digraph's edges in string form
        '''
        
        result = ''
        for src in self._nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
        return result

class Graph(Digraph):
    
    def addEdge(self, edge):
        '''
        Add an edge to the Graph

        Requires: edge is a Edge type object
        Ensures: Adds the given edge to the parent Digraph object and then adds
        the reverse edge to the same Digraph
        '''
        
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

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



def DFS(graph, start, end, path, shortest):
    """
    Finds the shortest path between two given nodes

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures: a shortest path from start to end in graph
    """
    path = path + [start]
    print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest



def search(graph, start, end):
    """
    Wrapper method for DFS

    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """
    return DFS(graph, start, end, [], None)



def testSP():
    nodes = []
    for name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = search(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', printPath(sp))

testSP()

    
    
