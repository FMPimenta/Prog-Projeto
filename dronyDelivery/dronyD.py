#2019-2020 Programação 2 (LTI)
#Grupo 45
#54971 Pedro Quintão
#54973 Francisco Pimenta

from Drone import Drone
from Parcels import Parcels
from compareHeaders import compareHeaders
import copy
import sys

def readDronesFile(fileName):
    """
    Converts a given file listing drones into a collection.
    
    Requires: fileName is str, the name of a .txt file listing drones,
    following the format specified in the project sheet.

    Ensures: A list of Drone type objects that represent each drone specified in the input file.
    """

    outputDronesList = []
    
    fileIn = open(fileName, 'r')

    #This while's purpose is to discard the first 7 lines that correspond to the header of the file.
    i = 0 
    while i < 7:
        fileIn.readline()
        i += 1

    #Appends each attribute of the drone separetely into the outputDronesList.    
    for line in fileIn:
        drones = line.replace(",","")
        dronesclean = drones.split() 
        outputDronesList.append(Drone(dronesclean))
        
    fileIn.close()

    return outputDronesList

def readParcelsFile(fileName):
    """
    Converts a given file listing parcels into a collection.
    
    Requires: fileName is str, the name of a .txt file listing parcels,
    following the format specified in the project sheet.

    Ensures: A list of Parcel type objects that represent each parcel specified in the input file.
    """
    
    outputParcelsList = []
      
    fileIn = open(fileName, 'r')

    #This while's purpose is to discard the first 7 lines that correspond to the header of the file.
    i = 0 
    while i < 7:
        fileIn.readline()
        i += 1

    #Appends each attribute of the parcel into the outputParcelsList.
    for line in fileIn:
        parcels = line.replace("," , "")
        parcelsclean = parcels.split()
        
        #Placing first name and surname in the same element
        parcelsclean[0] = parcelsclean[0]+" "+parcelsclean.pop(1)
        
        outputParcelsList.append(Parcels(parcelsclean))

    fileIn.close()

    return outputParcelsList

def updateDrone(drone, parcel):
    '''
    This function updates the time the drone is available to make a new delivery
    after completing the delivery he was associated with previously. The drone time
    will be compared to the customer order time, where the final time used will be
    the later time between these two. If the order cannot be delivered until 20:00,
    it will be passed to the next day.
    
    Requires: drone must be a Drone type object and parcel must be a Parcels type object
    
    Ensures: Sets the time that the drone is available to make a new delivery to when
    the drone is done with the previous parcel.
    '''

    #Choosing which date to use (the date when the drone will become available or
    #the date that the client asked the parcel to be delivered
    deliveryhour = drone.getAvailableHour()
    deliveryminutes = drone.getAvailableMinute()
    
    if parcel.getYear() > drone.getAvailableYear():
        drone.setAvailableYear(parcel.getYear())
        drone.setAvailableMonth(parcel.getMonth())
        drone.setAvailableDay(parcel.getDay())
        deliveryhour = parcel.getHour()
        deliveryminutes = parcel.getMinutes()
    elif parcel.getYear() == drone.getAvailableYear():
        if parcel.getMonth() > drone.getAvailableMonth():
            drone.setAvailableMonth(parcel.getMonth())
            drone.setAvailableDay(parcel.getDay())
            deliveryhour = parcel.getHour()
            deliveryminutes = parcel.getMinutes()
        elif parcel.getMonth() == drone.getAvailableMonth() :
            if parcel.getDay() > drone.getAvailableDay():
                drone.setAvailableDay(parcel.getDay())
                deliveryhour = parcel.getHour()
                deliveryminutes = parcel.getMinutes()
            elif parcel.getDay() == drone.getAvailableDay():
                if int(parcel.getHour()) > drone.getAvailableHour():
                    deliveryhour = parcel.getHour()
                    deliveryminutes = parcel.getMinutes()
                elif int(parcel.getHour()) == drone.getAvailableHour():
                    if int(parcel.getMinutes()) > drone.getAvailableMinute():
                        deliveryhour = parcel.getHour()
                        deliveryminutes = parcel.getMinutes()
    
    newDroneAvailableHour = int(deliveryhour) + parcel.getDeliveryTimeHours()
    newDroneAvailableMinutes = int(deliveryminutes) + parcel.getDeliveryTimeMinutes()
    daysToAdvance = 0

    #Fixing if time is, ex: 19:70, which is not an appropriate format.
    if int(newDroneAvailableMinutes) >= 60:
        newDroneAvailableMinutes = newDroneAvailableMinutes - 60
        newDroneAvailableHour = newDroneAvailableHour + 1

    #If the order passes to the next day.
    if int(newDroneAvailableHour) == 20 and int(newDroneAvailableMinutes) > 0 or int(newDroneAvailableHour) > 20:
        newDroneAvailableHour  = 8 + int(parcel.getDeliveryTimeHours())
        newDroneAvailableMinutes = parcel.getDeliveryTimeMinutes()
        daysToAdvance += 1
        deliveryhour = str(newDroneAvailableHour)
        deliveryhour = str(newDroneAvailableHour)
        deliveryminutes = "00"

    #After fixing all the exceptions that might have come up it sets the new value
    drone.setAvailableHour(newDroneAvailableHour)
    drone.setAvailableMinute(newDroneAvailableMinutes)
    drone.setAvailableDay(drone.getAvailableDay() + daysToAdvance)

    #If the order passes to the next month or year
    if drone.getAvailableDay() > 30:
        drone.setAvailableDay(drone.getAvailableDay() - 30)
        drone.setAvailableMonth(drone.getAvailableMonth() + 1)
        if drone.getAvailableMonth() > 12 :
            drone.setAvailableYear(drone.getAvailableYear() + 1)

    #Updating the autonomy
    currentAutonomy = drone.getAutonomy() * 1000
    totalDistance = parcel.getDistance() * 2
    updatedAutonomy = currentAutonomy - totalDistance
    updatedAutonomy = updatedAutonomy / 1000
    drone.setAutonomy(updatedAutonomy)

    #Updating the distance traveled
    currentDistance = drone.getAccumulatedDistance()
    currentDistance *= 1000
    updatedDistance = totalDistance + currentDistance
    updatedDistance = updatedDistance / 1000
    drone.setAccumulatedDistance(updatedDistance)

    return(str(deliveryhour) + ":" + str(deliveryminutes))
        
def assign(dronesList, parcelsList):
    '''
    Assigns each drone from the given drone list and assgins them to parcels in the given parcel list
    and then reorders the updated drone list to follow the parameters given in the project sheet

    Requires: dronesList is a list of Drone type objects that represent the drones,
    parcelsList is a list of Parcels type objects that represent the parcels to deliver.
    Ensures: 2 lists the first being the list that holds the parcels and assigned drones
    and the second being the list where the updated drones have been sorted as to follow the
    parameters in the project sheet.
    '''

    rosterList = []
    outputList = []
    
    for parcel in parcelsList:
        #This variable will hold the name of the drones who are able to deliver the current parcel
        candidates = []
        for drone in dronesList:
            
            #This if compares the drones parameters to certain parameters of the parcel and if they
            #match as instructed in the project sheet that drone's parameters will be added to the candidates list
            if parcel.getZone() == drone.getZone() and parcel.getDistance() * 2 <= (drone.getAutonomy() * 1000) and parcel.getWeight() <= drone.getWeight() and parcel.getDistance() <= drone.getMaxDistance():
                candidates.append(drone)

        #If the list of drones that are able to deliver a certain parcel is empty
        #(no drones are able to deliver) the cancelled string will be appended to the candidates list        
        if len(candidates) == 0:
            rosterList.append([parcel, "cancelled"])
        else:   
            #This for loop chooses the best drone to deliver the parcel according to the parameters
            #specified in the project sheet 
            bestDrone = candidates[0]
            for drone in candidates:
                if drone != bestDrone:
                    if bestDrone.getAvailableTime() > drone.getAvailableTime():
                        bestDrone = drone
                    elif bestDrone.getAvailableTime() == drone.getAvailableTime():
                        if bestDrone.getAutonomy() < drone.getAutonomy():
                            bestDrone = drone
                        elif bestDrone.getAutonomy() == drone.getAutonomy():
                            if bestDrone.getAccumulatedDistance() > drone.getAccumulatedDistance():
                                bestDrone = drone
                            elif bestDrone.getAccumulatedDistance() == drone.getAccumulatedDistance():                                
                                if bestDrone.getName() > drone.getName():
                                    bestDrone = drone

            deliveryhour = updateDrone(bestDrone, parcel)
            rosterList.append([parcel, bestDrone, deliveryhour])                        
            #Updates drones atributes and outputs the hour that the drone started the delivery to be used
            #as input to the function that will write the timetable file

    #Sorts the list has specified in the project sheet
    dronesList.sort(key=lambda k: (k.getAvailableTime(), -k.getAutonomy(), k.getName()))
    outputList.append(rosterList)
    outputList.append(dronesList)
    
    return outputList

def writeFile1 (roster, title):
        
    '''
    This method will be responsible for creating the text file containing all the
    updated drones.

    Requires: "roster" should be a list containing all the drones with their
    updated information and "fileName" must be the str of the initial drones input file.

    Ensures: A text file is created containing all updated drones.
    '''
    fileName = compareHeaders(title)
    
    hour = int(fileName.getHour()) 
    minutes = int(fileName.getMinutes()) 
    year = fileName.getYear()
    month = fileName.getMonth()
    day = fileName.getDay()

    minutes = minutes + 30 

    if minutes >= 60:
        hour = hour+1
        minutes = minutes-60
    if minutes < 10:
        minutes = '0' + str(minutes)
    if hour >= 24:
        hour = hour - 24
        day = day + 1
    if day > 30:
        day = day-30
        month = month+1
    if month >12:
        month = month-12
        year = year+1

    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = hour
    hour = str(hour)
    minutes = str(minutes)
    year = str(year)
    month = str(month)
    day = str(day)
        
    
    #making the file name
    filetitle = fileName.getScope().lower()+hour+'h'+minutes+'_'+year+'y'+month+'m'+day+'.txt'

    
    #content of the file
    #creating the header
    f= open(filetitle, 'w+')

    f.write('Time:')
    f.write('\n')
    f.write(hour+'h'+minutes)
    f.write('\n')
    f.write('Day:')
    f.write('\n')
    f.write(day+'-'+month+'-'+year)
    f.write('\n')
    f.write('Company:')
    f.write('\n')
    f.write('iXicoZe')
    f.write('\n')
    f.write('Drones:')
    f.write('\n')

    #drones
    for d in roster:
        deepcopy = copy.deepcopy(d)
        if deepcopy.getAvailableMonth() < 10:
            deepcopy.setAvailableMonth('0' + str(deepcopy.getAvailableMonth()))
        if deepcopy.getAvailableDay() < 10:
            deepcopy.setAvailableDay('0' + str(deepcopy.getAvailableDay()))
        if int(deepcopy.getAvailableHour()) < 10:
            deepcopy.setAvailableHour('0' + str(deepcopy.getAvailableHour()))
        if int(deepcopy.getAvailableMinute()) < 10:
            deepcopy.setAvailableMinute('0' + str(deepcopy.getAvailableMinute()))
        
        line = d.getName() + ', ' + d.getZone() + ', ' + str(d.getWeight()) + ', ' + str(d.getMaxDistance()) + ', ' + str(d.getAccumulatedDistance()) + ', '+ str(d.getAutonomy()) +', ' + str(d.getAvailableYear()) + '-' + str(deepcopy.getAvailableMonth()) + '-' + str(deepcopy.getAvailableDay()) + ', ' + str(deepcopy.getAvailableHour()) + ':' + str(deepcopy.getAvailableMinute())

        f.write(line)
        f.write('\n')

    f.close()
    
def writeFile2 (roster, title):
    '''
    This method will be responsible for creating the text file containing the timetable.

    Requires: "roster" should be a list containing all assignments made between
    orders and drones and "title" should be the str of the initial input file parcels.

    Ensures: A text file containing the timetable is created.
    '''

    fileName = compareHeaders(title)
    
    #making the file name
    filetitle = 'timetable'+fileName.getHour()+'h'+fileName.getMinutes()+'_'+str(fileName.getYear())+'y'+str(fileName.getMonth())+'m'+str(fileName.getDay())+'.txt'

    #content of the file
    #creating the header        
    f= open(filetitle, 'w+')
    f.write('Time:')
    f.write('\n')
    f.write(str(fileName.getHour())+'h'+str(fileName.getMinutes()))
    f.write('\n')
    f.write('Day:')
    f.write('\n')
    f.write(str(fileName.getDay() )+'-'+str(fileName.getMonth())+'-'+str(fileName.getYear()))
    f.write('\n')
    f.write('Company:')
    f.write('\n')
    f.write('iXicoZe')
    f.write('\n')
    f.write('Timeline:')
    f.write('\n')
    
    #Will be used to sort the timetable lines after the ones taht have been cancelled
    organizedList = []

    #Correct the format for the dates in the timetable lines that have been cancelled
    month = fileName.getMonth()
    day = fileName.getDay()
    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)
    else:
        month = month
        day = day
        
    #Lines for the timetable for the parcels that have been cancelled
    for e in roster:
        parcel = e[0]
        drone = e[1]
        if drone == 'cancelled':
            line = str(parcel.getYear()) + '-' + str(month) + '-'+ str(day) + ', ' + str(parcel.getHour()) + ':' + str(parcel.getMinutes()) + ', ' + parcel.getName() + ', '+  'cancelled'
            f.write(line)
            f.write('\n')

    #Sorting the parcels that have not been cancelled
    for e in roster:
        if e[1] != 'cancelled':       
            organizedList.append(e)
            organizedList.sort(key=lambda k: (k[2], k[0].getName()))

    for e in organizedList:
        #Correct the format for the dates in the timetable lines that have not been cancelled
        if len(str(e[1].getAvailableMonth())) < 2:
            e[1].setAvailableMonth('0' + str(e[1].getAvailableMonth()))
        if len(str(e[1].getAvailableDay())) < 2:
            e[1].setAvailableDay('0' + str(e[1].getAvailableDay()))

        
        time = str(e[2])
        time = time.split(":")
        hour = time[0]
        minutes = time[1]

        #Making sure the hours and minutes are double digits
        if len(str(hour)) < 2:
            hour = '0' + str(hour)
        if len(str(minutes)) < 2:
            minutes = '0' + str(minutes)
        
        line = str(e[1].getAvailableYear()) + '-' + str(e[1].getAvailableMonth()) + '-' + str(e[1].getAvailableDay()) + ', ' + hour + ':' + minutes + ', ' + str(e[0].getName()) + ', ' + str(e[1].getName())
        f.write(line)
        f.write('\n')
    
    f.close()

    
#Receives the name of the input files
inputFileName1, inputFileName2 = sys.argv[1:]

#Creates the Header objects
headerd = compareHeaders(inputFileName1)
headerp = compareHeaders(inputFileName2)

#Checks if the title and header of both files are compatible
headerp.checkHeader()
headerd.checkHeader()

#Checks if the headers of each file are compatible
headerd == headerp

#Creates all the drone and parcel objects and assigns the drones to the parcels
drones = readDronesFile(inputFileName1)
parcels = readParcelsFile(inputFileName2)
output = assign(drones, parcels)

#Outputs the file that lists the updated drones
writeFile1(output[1], inputFileName1)
#Outputs the file that lists each parcel and their assigned drone
writeFile2(output[0] , inputFileName1)


