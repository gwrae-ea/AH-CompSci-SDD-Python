class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.startDate = startDate  #String
        self.startTime = startTime  #String
        self.venue = venue          #String
        self.reminder = reminder    #Boolean
        self.participants = [""]*20 #Array of String
        self.index = 0              #Integer

    def updateDate(self, eventDate):
        self.startDate  = eventDate

    def getDate(self):
        return self.startDate

    def addParticipant(self, name):
        self.participants[self.index] = name
        self.index = self.index + 1
