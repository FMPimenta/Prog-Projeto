def directContacts (Direct):
    '''
    Creates a set which stores the id's of everyone who is in direct social contact
    with an element from a social network

    Requires: Contacts is a string defining the id's of the elements in direct social
              contact with a element from a social network
              
    Ensures: A new set with the id's of everyone in direct social contact with a element
             from a social network
    '''

    strip_contacts = Direct.strip("<>")
    contact_list = strip_contacts.split(", ")
    direct_contacts = set()

    #Adding everyone who is in direct social contact with the current Person instance 
    for contact in contact_list:
        direct_contacts.add(contact)

    return direct_contacts

def allContacts (person, network):
    '''
    Creates a set which stores the id's of everyone who is in direct or indirect social
    contact with the given Person.

    Requires: person is a Person type object, socialnetwork is a list wich contains all Person objects
                   in a social network
                   
    Ensures: A new set with the id's of everyone in direct or indirect social contact with
                  the Person object
    '''

    all_contacts = set()

    #Adding the direct contacts to the set
    for id in self.getDirect():
        all_contacts.add(id)

    #Adding the indirect contacts to the set
    i = 0
    while i < len(all_contacts):
        #Finding the Person object which the id of one of the contacts
        for person in network:
            if person.getIdNb() == all_contacts[i]:
                for id in person.getDirect():
                    all_contacts.add(id)
                    
        i++    

    return all_contacts


