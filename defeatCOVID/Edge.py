# 2019-2020 Programação 2 (LTI)
# Grupo 1
# 54973 Francisco Pimenta
# 55477 Oleksandra Butyrska

from Person import Person
from copy import deepcopy


class Edge:
    
    def __init__(self, src, dest):
        """
        Creates a Edge object

        Requires: src and dest are Person type objects
        Ensures: A new Edge object is created
        """

        self._src = src
        self._dest = dest
        self._srcName = src.getName()
        self._destName = dest.getName()
        #Hours until src Person object infects dest Person objects
        self._weight = round((dest.getFitness() * (1 / src.getAge())) * 24)
        
        
    def getSource(self):
        '''
        Source Person object of the edge
        '''
        
        return self._src
    
    def setSource(self, newSrc):
        '''
        Attribute src is set to newSrc

        Requires: newSrc is a Person type object
        Ensures: self._src = newSrc
        '''

        self._src = newSrc
        
    
    def getDestination(self):
        '''
        Destination Person of the edge
        '''
        
        return self._dest

    def setDestination(self, newDest):
        '''
        Attribute dest is set to newDest

        Requires: newDest is a Person type object
        Ensures: self._dest = newDest
        '''

        self._dest = newDest

    def getWeight(self):
        '''
        Number of hours until the Person object in the src attribute
        infects the Person object in the dest attribute
        '''

        return self._weight

    def setWeight(self, newWeight):
        '''
        Attribute weight is set to newWeight

        Requires: newWeight is a int
        Ensures: self._weight = newWeight
        '''

        self._weight = newWeight

    def getSourceName(self):
        '''
        Name of source Person object of the edge
        '''
        
        return self._srcName
    
    def setSourceName(self, newName):
        '''
        Attribute srcName is set to newName

        Requires: newName is a string
        Ensures: self._srcName = newName
        '''

        self._srcName = newName

    def getDestinationName(self):
        '''
        Name of destination Person object of the edge
        '''
        
        return self._destName
    
    def setDestinationName(self, newName):
        '''
        Attribute destName is set to newName

        Requires: newName is a string
        Ensures: self._destName = newName
        '''

        self._destName = newName

    def generateEdges(network):
        """
        Generate the edges that represent each contact between 2 elements of the
        social network

        Requires: network is a list containing lists that contain the parameters
        of a single element of the given social network
        Ensures: a list containing all edges needed to represent all the
        contacts between all elements of the given social network
        """

        edges = []

        #tries to find the element of the social network with a given ID
        for src in network:
            for contactID in src.getDirect():
                for contact in network:
                    #if a match is found creates a Edge type object
                    if contactID == contact.getIdNb():
                        dest = contact
                        edge = Edge(src, dest)

                #checks if the created edge isnt already in the edges list
                if edge not in edges:
                    edges.append(edge)

        return edges
    
    
    def __str__(self):
        '''
        Returns the edge in string representation 
        '''
        
        return self._srcName + '->' + self._destName

    def __lt__(self, other):
        '''
        Compares the weight of 2 Edge type objects

        Requires: other is a Edge type object
        Ensures: If the current Edge instance weight attribute is less than the
        other Edge type object weight attribute returns True, otherwise returns
        False
        '''
        
        return self.getWeight() < other.getWeight()

    def __eq__(self, other):
        '''
        Compares the current Edge instance source and destination with another
        edge's source and destinaton
        
        Requires: other is a Edge type object
        Ensures: If the edges have the same source, destination returns true
        otherwise returns false
        '''

        return self.getSource() == other.getSource() and self.getDestination() \
        == other.getDestination() and self.getWeight() == other.getWeight()








    
