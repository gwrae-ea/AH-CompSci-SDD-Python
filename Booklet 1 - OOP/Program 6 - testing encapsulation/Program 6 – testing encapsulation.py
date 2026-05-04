class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.__startDate = startDate  #String
        self.__startTime = startTime  #String
        self.__venue = venue          #String
        self.__reminder = reminder    #Boolean
        self.__participants = [""]*20 #Array of String
        self.__index = 0              #Integer

    def updateDate(self, eventDate):
        self.startDate  = eventDate

    def getDate(self):
        return self.startDate

    def addParticipant(self, name):
        self.participants[self.index] = name
        self.index = self.index + 1

#Test for the CONSTRUCTOR method
item1 = Event("13/04/18", "0900", "Main Office", True)
print (item1.venue)
