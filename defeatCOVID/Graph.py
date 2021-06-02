# 2019-2020 Programação 2 (LTI)
# Grupo 1
# 54973 Francisco Pimenta
# 55477 Oleksandra Butyrska

class Graph:
    
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its direct contacts
    
    def __init__(self):
        '''
        Creates a Graph object

        Ensures: A new Graph object
        '''
        
        self._nodes = []
        self._edges = {}
        
        
    def addNode(self, node):
        '''
        Adds a node to the Graph

        Requires: node is a string
        Ensures: If its not on the nodes attribute, the node is added to the
        nodes attributes and to the edges dictionary with an empty list as
        a value
        '''
        
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []
            
            
    def addEdge(self, edge):
        '''
        Add an edge to the Graph

        Requires: edge is a Edge type object
        Ensures: If its source and destination nodes are not in the nodes
        attribute of the current Graph instance raises an exception.
        Otherwise: adds the given edge (src attribute as key and dest attribute
        as a value) to the Graph
        '''
        
        src = edge.getSourceName()
        dest = edge.getDestinationName()
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        if dest not in self._edges[src]:
            self._edges[src].append(dest)

    def addReverseEdge(self, edge):
        '''
        Add the reverse of an edge to the Graph

        Requires: edge is a Edge type object
        Ensures: Adds the reverse (edge's src attribute as value and dest
        attribute as key) edge to the Graph object
        '''
        
        src = edge.getSourceName()
        dest = edge.getDestinationName()
        if src not in self._edges[dest]:
            self._edges[dest].append(src)

    def childrenOf(self, node): ## all the Direct contacts
        '''
        Returns every node that is a child of the given node

        Requires: node is a string that is in the nodes attribute
        Ensures: a list with every node that is a child of the given node name
        '''
        
        return self._edges[node]
    
    
    def hasNode(self, node):
        '''
        Checks if given node name is in the nodes attributes

        Requires: node must be a string
        Ensures: True if node is in the nodes attribute list
        '''
        
        return node in self._nodes
    
    def generateGraph(network, edges):
        """
        Generate a Graph object where the nodes are the elements of the social
        network and the edges depict all direct contacts that each element
        has with other elements

        Requires: network is a list containing lists that contain the parameters
        of a single element of the given social network and edges is a list
        containing all edges necessary to represent the social network
        accurately.
        Ensures: A new Graph object
        """

        g = Graph()

        for person in network:
            g.addNode(person.getName())

        for edge in edges:
            g.addEdge(edge)
            g.addReverseEdge(edge)

        return g


    def __str__(self):
        '''
        Returns all Graph's edges in string form
        '''
        
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src + '->'\
                + dest + '\n'
        return result

    def __eq__(self, other):
        '''
        Compares the nodes and edges attribute of the current Graph instance with another
        Graph type object nodes and edges attributes
        
        Requires: other is Graph
        Ensures: If current Graph instance node and edge attributes are equal to
        other Graph object instance node and edge attribute, returns True otherwise
        returns False
        '''

        return self._nodes == other._nodes and self._edges == other._edges
        





