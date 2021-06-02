class compareHeaders:

    def __init__(self, fileName):

        '''
        This method reads the header, which contains the time, the day and the company name
        of a .txt file.

        Requires: fileName is a str of the name of a .txt file containing the time, the
        day and the company name following the format specified in the project sheet.

        Ensures: This method will create objects for each information collected.
        '''
        
        self._fileName = fileName

        fileIn = open(fileName, 'r')

        fileIn.readline()

        time = fileIn.readline().strip().replace("\n", "").split('h')
        self._hour = time[0]
        self._minutes = time[1]

        fileIn.readline()

        date = fileIn.readline().strip().replace("\n", "").split('-')
        self._day = int(date[0])
        self._month = int(date[1])
        self._year = int(date[2])

        fileIn.readline()

        self._company = fileIn.readline().strip().replace("\n", "")

        self._scope = fileIn.readline().strip().replace("\n", "")
        self._scope = self._scope.replace(":","")
        
        fileIn.close()
 
    
    def getFileName(self):

        '''
        This method returns the name of the file.
        '''
        
        return self._fileName
    
    def setFileName(self, newFileName):
        
        '''
        Attribute fileName is set to newFileName.

        Requires: newFileName is a str.
        Ensures: self._fileName == newFileName.
        '''
        self._fileName = newFileName    

    def getHour(self):

        '''
        This method returns the hour when orders are received.
        '''

        return self._hour
    
    def setHour(self, newHour):
        
        '''
        Attribute hour is set to newHour.

        Requires: newHour is a str.
        Ensures: self._hour == newHour. 
        '''
        self._hour = newHour

    def getMinutes(self):

        '''
        This method returns the minutes when orders are received.
        '''

        return self._minutes
    
    def setMinutes(self, newMinutes):
        
        '''
        Attribute minutes is set to newMinutes.

        Requires: newMinutes is a str.
        Ensures: self._minutes == newMinutes. 
        '''
        self._minutes = newMinutes
        
    def getDay(self):

        '''
        This method returns the day on which orders are received. 
        '''

        return self._day

    def setDay(self, newDay):
        
        '''
        Attribute day is set to newDay.

        Requires: newDay is a str.
        Ensures: self._day == newDay.

        '''

        self._Day = newDay

    def getMonth(self):

        '''
        This method returns the month on which orders are received.
        '''

        return self._month

    def setMonth(self, newMonth):
        
        '''
        Attribute month is set to newMonth.

        Requires: newMonth is a str.
        Ensures: month == newMonth.

        '''

        self._month = newMonth

    def getYear(self):

        '''
        This method returns the year on which orders are received 
        '''

        return self._year

    def setYear(self, newYear):
        
        '''
        Attribute year is set to newYear.

        Requires: newYear is a str.
        Ensures: self._year == newYear.

        '''

        self._year = newYear

    def getCompany(self):

        '''
        This method returns the company name. 
        '''
        
        return self._company

    def setCompany(self, newCompany):

        '''
        Attribute company is set to newCompany.

        Requires: newCompany is a str.
        Ensures: self._company == newCompany.
        '''

        self._Company = newCompany
    
    def getScope(self):

        '''
        This method returns the type of content the file holds.
        '''

        return self._scope

    def setScope(self, newScope):
        
        '''
        Attribute scope is set to newScope.

        Requires: newScope is a str.
        Ensures: self._scope == newScope.
        '''

        self._scope = newScope

    def __str__(self):

        '''
        This method returns in string representation the time, the day, the company 
        and the scope.
        '''

        return 'Hours: ' + str(self.getHour()) + ', Minutes: ' + str(self.getMinutes()) + ', Day: ' + str(self.getDay()) + ', Month: ' + str(self.getMonth()) + \
            ', Year: ' + str(self.getYear()) + ', Company: ' + str(self.getCompany()) + ', Scope: ' + str(self.getScope())


    def __eq__(self, otherHeader):
        '''
        This method will compare the header of the drones file and the header 
        of the parcels file.
        
        Requires: otherHeader is a Header type object.
        
        Ensures: If the headers are equal, nothing will happen, if the headers are different, 
        an exception will be raised.
        '''

      
        if self.getHour() != otherHeader.getHour() or self.getMinutes() != otherHeader.getMinutes() or  self.getDay() != otherHeader.getDay() \
            or self.getMonth() != otherHeader.getMonth() or self.getYear() != otherHeader.getYear() or self.getCompany() != otherHeader.getCompany():
            raise Exception ('Input error: inconsistent files '+ self.getFileName() +' and '+ otherHeader.getFileName() +'.')

    def checkHeader (self):
        
        '''
        This method will compare the the file name with the content of its header.

        Ensures: If the content of the header matches the file name, nothing will happen, otherwise an exception will be raised.
        '''

        #checking if the content matches with the file name

        filetxt2 = self.getScope().lower()+ str(self.getHour()) + 'h' + str(self.getMinutes()) + '_'+ str(self.getYear()) + 'y' + \
        str(self.getMonth()) + 'm' + str(self.getDay()) +'.txt'
        
        if filetxt2 != self.getFileName():
            raise Exception ('Input error: name and header inconsistent in file '+self.getFileName()+'.')


