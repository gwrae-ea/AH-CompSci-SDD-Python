class Event:
    def __init__(self, startDate, startTime, venue, reminder):
        self.startDate = str(startDate)  #String
        self.startTime = str(startTime)  #String
        self.venue = str(venue)          #String
        self.reminder = reminder if isinstance(reminder, bool) else str(reminder).strip().lower() in ("true", "1", "yes", "y")    #Boolean (don't use bool(reminder): bool("False") is True)
        self.participants = [""]*20 #Array of String
        self.index = int(0)              #Integer

    def updateDate(self, eventDate):
        self.startDate  = str(eventDate)

    def getDate(self):
        return self.startDate

    def getVenue(self):
        return self.venue

    def addParticipant(self, name):
        self.participants[self.index] = str(name)
        self.index = self.index + 1

# Pseudocode review:
# Check that the UML and English pseudocode show the same constructor and methods.

# Code review:
# Check that the Python class contains Event(), getVenue(), updateDate(), getDate() and addParticipant().

# Test the constructor and getter methods with a first object.
item1 = Event("13/04/18", "0900", "Main Office", True)
print("Constructor/getVenue test 1:", item1.getVenue())
print("getDate test 1:", item1.getDate())

# Test updateDate() by checking the date before and after the change.
item1.updateDate("13/04/22")
print("getDate test 2:", item1.getDate())

# Test addParticipant() with several names and check the array positions and index.
item1.addParticipant("Erica Knowles")
item1.addParticipant("Norman Osborne")
item1.addParticipant("Fred Savage")
print("addParticipant test 1:", item1.participants[0])
print("addParticipant test 2:", item1.participants[1])
print("addParticipant test 3:", item1.participants[2])
print("Participant index:", item1.index)

# Test constructor independence with a second object.
item2 = Event("20/06/18", "1400", "Assembly Hall", False)
print("Constructor/getVenue test 2:", item2.getVenue())
print("getDate test 3:", item2.getDate())
