import datetime
class Parcels:
    
    '''
    Parcels
    '''

    def __init__(self, parcelsLine):
        
        '''
        Creates a parcel object with the attributes defined in the line.

        Requires: parcelsLine must be a line in list format from the Parcel input file containing all the information for each parcel.
        Ensures: a new Parcel object is created.
        '''

        #Splitting the hour and minutes that the parcel is to be delivered
        parcelhour = parcelsLine[3].split(":")
        
        #Transforming the delivery time from minutes to hours and minutes
        if int(parcelsLine[6]) >= 60:
            deliveryhours = int(int(parcelsLine[6]) / 60)
            deliveryminutes = int(parcelsLine[6]) - (deliveryhours * 60)
        else:
            deliveryhours = 0
            deliveryminutes = int(parcelsLine[6])

        #Extracting the year , month and day
        date = parcelsLine[2].split("-")

        self._name = parcelsLine[0]
        self._zone = parcelsLine[1]
        self._year = int(date[0])
        self._month = int(date[1])
        self._day = int(date[2])
        self._hour = parcelhour[0]
        self._minutes = parcelhour[1]
        self._distance = int(parcelsLine[4])
        self._weight = int(parcelsLine[5])
        self._deliveryTimeHours = deliveryhours
        self._deliveryTimeMinutes = deliveryminutes
        
    def getName(self):

        '''
        This method returns the name of the client's who placed the order. 
        '''

        return self._name

    def setName(self , newName):

        '''
        Attribute name is set to newName.

        Requires: newName is a str.
        Ensures: self._name = newName.
        '''
    
        self._name = newName

    def getZone(self):

        '''
        This method returns the name of the zone where the order must be made.
        '''
        
        return self._zone

    def setZone(self , newZone):

        ''' 
        Attribute zone is set to newZone.

        Requires: newZone is a str.
        Ensures: self._zone == newZone.  
        '''

        self._zone = newZone

    def getYear(self):

        '''
        This method returns the year from which the order must be executed.
        '''

        return self._year

    def setYear(self , newYear):
        
        '''
        Attribute year is set to newYear.

        Requires: newYear is a str.
        Ensures: self._year == newYear.  
        '''

        self._year = newYear

    def getMonth(self):

        '''
        This method returns the month from which the order must be executed.
        '''
        
        return self._month

    def setMonth(self , newMonth):
        
        '''
        Attribute month is set to newMonth.

        Requires: newMonth is a str.
        Ensures: self._month == newMonth.  
        '''

        self._month = newMonth

    def getDay(self):

        '''
        This method returns the day from which the order must be executed.
        '''

        return self._day

    def setDay(self , newDay):
        
        '''
        Attribute day is set to newDay.

        Requires: newDay is a str.
        Ensures: self._day == newDay.  
        '''

        self._day = newDay

    def getHour(self):

        '''
        This method returns the time from which the order is to be executed.
        '''
        
        return self._hour

    def setHour(self, newHour):
        
        '''
        Attribute hour is set to newHour.

        Requires: newHour is a str.
        Ensures: self._hour == newHour.  
        '''

        self._hour= newHour

    def getMinutes(self):

        '''
        This method returns the minute from which the order is to be executed.
        '''
        
        return self._minutes

    def setMinutes(self, newMinute):
        
        '''
        Attribute minutes is set to newMinute.

        Requires: newMinute is a str.
        Ensures: self._minutes == newMinute.  
        '''

        self._minutes = newMinute

    def getDistance(self):

        '''
        This method returns the distance between the delivery location and the base of the drones in that area of the city.
        '''

        return self._distance

    def setDistance(self , newDistance):
        
        '''
        Attribute distance is set to newDistance.

        Requires: newDistance is a str.
        Ensures: self._distance == newDistance.  
        '''
        
        self._distance= newDistance

    def getWeight(self):

        '''
        This method returns the weight of the order that must be transported.
        '''
        return self._weight    

    def setWeight(self , newWeight):
        
        '''
        Attribute weight is set to newWeight.

        Requires: newWeight is a str
        Ensures: self._weight == newWeight.  
        '''
        
        self._weight = newWeight

    def getDeliveryTimeHours(self):

        '''
        This method returns the hours needed for transportation.
        '''

        return self._deliveryTimeHours

    def setDeliveryTimeHours(self, newDeliveryTimeHour):

        '''
        Attribute deliveryTimeHours is set to newDeliveryTimeHour.

        Requires: newDeliveryTime is a str 
        Ensures: self._deliveryTimeHours == newDeliveryTimeHour.  
        '''
        
        self._deliveryTimeHours = newDeliveryTimeHour

    def getDeliveryTimeMinutes(self):

        '''
        This method returns the minutes needed for transportation.
        '''
        
        return self._deliveryTimeMinutes

    def setDeliveryTimeMinutes(self, newDeliveryTimeMinutes):

        '''
        Attribute deliveryTimeMinutes is set to newDeliveryTimeMinutes.   

        Requires: newDeliveryTimeMinutes is a str 
        Ensures: self._deliveryTimeMinutes == newDeliveryTimeMinutes.  
        '''
        
        self._deliveryTimeMinutes = newDeliveryTimeMinutes

    def __str__(self):

        '''
        This method returns in string representation the name, the zone, the date, 
        the hour, the distance, the parcel weight and the delivery time. 
        '''

        return 'Name: ' + str(self.getName())+ ', Zone: ' + str(self.getZone()) + ', Date: ' + str(self.getYear()) + '-' + str(self.getMonth()) + '-' + \
        str(self.getDay()) + ', Hour: ' + str(self.getHour()) + ':' + str(self.getMinutes()) + ', Distance: ' + str(self.getDistance()) +  ', Parcel weight: ' + \
        str(self.getWeight()) + ', Delivery Time: ' + str(self.getDeliveryTimeHours())+":"+str(self.getDeliveryTimeMinutes())
