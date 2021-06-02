#2019-2020 Programação 2 (LTI)
#Grupo 45
#54971 Pedro Quintão
#54973 Francisco Pimenta
import datetime

class Drone():
    '''
    Drones
    '''

    def __init__(self, droneLine):
        '''
        Creates a drone object with the attributes defined in the line

        Requires: droneLine must be a line from the drone input file in list form
        Ensures: A new Drone object is created
        '''

        date = droneLine[6].split("-")
        hour = droneLine[7].split(":")
        
        self._name = droneLine[0]
        self._zone = droneLine[1]
        self._weight = int(droneLine[2])
        self._maxDistance = int(droneLine[3])
        self._accumulatedDistance = float(droneLine[4])
        self._autonomy = float(droneLine[5])
        self._availableYear = int(date[0]) 
        self._availableMonth = int(date[1])
        self._availableDay = int(date[2])
        self._availableHour = int(hour[0])
        self._availableMinute = int(hour[1])
    
    def getName(self):
        '''
        Name of the drone.
        '''

        return self._name

    def setName(self, newName):
        '''
        Requires: newName is str.
        Ensures: self._name == newName.
        '''

        self._name = newName
        
    def getZone(self):
        '''
        Zone that the drone can deliver.
        '''

        return self._zone

    def setZone(self, newZone):
        '''
        Requires: newZone is a str.
        Ensures: self._zone == newZone.
        '''

        self._zone = newZone
    
    def getWeight(self):
        '''
        Maximum package weight that the drone can carry.
        '''

        return self._weight

    def setWeight(self, newWeight):
        '''
        Requires: newWeight is a int.
        Ensures: self._weight == newWeight.
        '''

        self._weight = newWeight
    
    def getMaxDistance(self):
        '''
        Maximum distance that the drone can be from the base.
        '''

        return self._maxDistance

    def setMaxDistance(self, newDistance):
        '''
        Requires: newDistance is a int.
        Ensures: self._maxDistance == newDistance.
        '''

        self._maxDistance = newDistance
    
    def getAccumulatedDistance(self):
        '''
        Distance that the drone as flown so far.
        '''

        return self._accumulatedDistance

    def setAccumulatedDistance(self, newDistance):
        '''
        Requires: newDistance is a int.
        Ensures: self._accumulated == newDistance.
        '''

        self._accumulatedDistance = newDistance

    def getAutonomy(self):
        '''
        Distance that the drone can fly before having to return to base.
        '''

        return self._autonomy

    def setAutonomy(self, newAutonomy):
        '''
        Requires: newAutonomy is int.
        Ensures: self._autonomy == newAutonomy.
        '''

        self._autonomy = newAutonomy

    def getAvailableYear(self):
        '''
        Year that the drone will be available to deliver a new parcel.
        '''

        return self._availableYear

    def setAvailableYear(self, newYear):
        '''
        Requires: newYear is a int.
        Ensures: self._availableYear == newYear.
        '''

        self._availableYear = newYear

    def getAvailableMonth(self):
        '''
        Month that the drone will be available to deliver a new parcel.
        '''

        return self._availableMonth

    def setAvailableMonth(self, newMonth):
        '''
        Requires: newMonth is a int.
        Ensures: self._availableMonth == newMonth.
        '''

        self._availableMonth = newMonth

    def getAvailableDay(self):
        '''
        Day that the drone will be available to deliver a new parcel.
        '''

        return self._availableDay

    def setAvailableDay(self, newDay):
        '''
        Requires: newDay is a int.
        Ensures: self._availableDay == newDay.
        '''

        self._availableDay = newDay

    def getAvailableHour(self):
        '''
        Hour that the drone will be available to deliver new parcel.
        '''

        return self._availableHour

    def setAvailableHour(self, newHour):
        '''
        Requires: newHour is a int.
        Ensures: self._availableHour == newHour.
        '''

        self._availableHour = newHour

    def getAvailableMinute(self):
        '''
        Minute that the drone will be available to deliver a new parcel.
        '''

        return self._availableMinute

    def setAvailableMinute(self, newMinute):
        '''
        Requires: newMinute is a int.
        Ensures: self._availableMinute == newMinute.
        '''

        self._availableMinute = newMinute

    def getAvailableTime(self):
        '''
        Date that the drone will be available in a datetime format. 
        '''

        return datetime.datetime(self.getAvailableYear(), self.getAvailableMonth(), self.getAvailableDay(), \
                                 self.getAvailableHour(), self.getAvailableMinute())

    def __str__(self):
        '''
        This method returns in string representation the name, the zone, the weight,
        the maximum distance, the accumulated distance, the autonomy, the available date and the available hour.        
        '''

        return "Name: " + str(self.getName()) + ", " "Zone: " + str(self.getZone()) + ", " + \
        "Weight: " + str(self.getWeight()) + ", " + "Maximum Distance: " + str(self.getMaxDistance()) + ", " + \
        "Accumulated Distance: " + str(self.getAccumulatedDistance()) + ", " + "Autonomy: " + str(self.getAutonomy()) + ", " + \
        "Available Date: " + str(self.getAvailableYear()) + "-" + str(self.getAvailableMonth()) + "-" + str(self.getAvailableDay()) ", " + "Available Hour: " + str(self.getAvailableHour())
