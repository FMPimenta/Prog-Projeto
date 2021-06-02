# 2019-2020 Programação 2 (LTI)
# Grupo 1
# 54973 Francisco Pimenta
# 55477 Oleksandra Butyrska

class Person:
   
    def __init__(self, personList):
        """
        Creates a Person object.

        Requires: personList is a list.
        Ensures: A new Person object is created.
        """

        self._name = personList[0] 
        self._IdNb = personList[1]
        self._Age = int(personList[2])
        self._Direct = personList[5] 
        self._Fitness = int(personList[3])
        self._Immune = personList[4]
        

    def getName(self):
        """
        Name of Person.
        
        Ensures: name is str.
        """
        return self._name
    

    def getIdNb(self):
        """
        IdNb of Person.

        Ensures: IdNb is str.
        """
        return self._IdNb


    def getAge(self):
        """
        Age of Person.

        Ensures: Age is int.
        """
        return self._Age


    def getDirect(self):
        """
        Elements with whom the Person had direct social contact.

        Ensures: Direct is list.
        """
        return self._Direct
    

    def getFitness(self):
        """
        Fitness level of Person.

        Ensures: int from 1 to 5.
        """
        return self._Fitness
    

    def getImmune(self):
        """
        Wether the Person is immune or not.

        Ensures: 'Yes' if is immune, and 'No' if it is not.
        """
        return self._Immune

    

    def setName(self, Name):
        """
        Set the name of Person.

        Requires: Name is str.
        """
        self._name = Name
        

    def setIdNb(self, IdNb):
        """
        Set the IdNb of Person.

        Requires: IdNb is str.
        """
        self._IdNb = IdNb


    def setAge(self, Age):
        """
        Set the Age of Person.

        Requires: Age is int.
        """
        self._Age = Age


    def setDirect(self, Direct):
        """
        Set the elements with whom the Person had direct social contact.

        Requires: Direct is set.
        """
        self._Direct = Direct
        

    def setFitness(self, Fitness):
        """
        Set the fitness level of Person.

        Requires: Fitness is a number from 1 to 5.
        """
        self._Fitness = Fitness
        

    def setImmune(self, Immune):
        """
        Set the Person as immune or not immune.

        Requires: str of 'Yes' or 'No'.
        """
        self._Immune = Immune

    def stringToPerson(name, network):
        """
        Converts a string with a name to the corresponding Person object from
        the Network
        
        Requires: name is str
        Ensures: The corresponding person object from the social network
        """

        for person in network:
            if person.getName() == name:
                return person

        raise Exception ()
    

    def __str__(self):
        """
        Returns the current Person instance name attribute
        
        Ensures: the current Person instance name attribute
        """

        return self.getName()
    
    def __eq__(self, other):
        """
        Compares the name attribute of the current Person instance with another
        Person type object name attribute
        
        Requires: other is Person.
        Ensures: If current Person object instance name attribute is equal to
        other Person object name attribute returns True, otherwise returns
        False
        """
        
        return self.getName() == other.getName()

    def __lt__ (self, other):
        '''
        Compares the weight of 2 Edge type objects

        Requires: other is a Person type object
        Ensures: If the current Person instance fitness attribute is less than
        the other Person type object fitness attribute returns True, otherwise
        returns False 
        '''

        return self.getFitness() < other.getFitness()
















    



























    
    
