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

    def addParticipant(self, name):
        self.participants[self.index] = str(name)
        self.index = self.index + 1

class WorkMeeting(Event):
    def __init__(self, startDate, startTime, venue, reminder, meetingTitle, mileage ):
        super().__init__(startDate, startTime, venue, reminder)
        self.meetingTitle = str(meetingTitle)      #String
        self.mileage = float(mileage)                #Real
        self.travelExpenses = float(0)               #Real

    def calculateTravelExpenses(self):
        self.travelExpenses = self.mileage * 1.5
    
    def getTravelExpenses(self):
        return self.travelExpenses

    def getDate(self):
        return ("The date of this Work Meeting is " + str(self.startDate))

class Personal(Event):
    def __init__(self, startDate, startTime, venue, reminder, eventType, description):
        super().__init__(startDate, startTime, venue, reminder)
        self.eventType = str(eventType)      # String
        self.description = str(description)  # String

    def setEventType(self, eventType):
        self.eventType = str(eventType)

    def setDescription(self, description):
        self.description = str(description)

    def getDescription(self):
        return self.description

# 1) instantiate objects of each class (top-level demo, runs without using __name__ guard)
e = Event("2026-04-23", "09:00", "Library", False)
w = WorkMeeting("2026-04-24", "10:00", "Office", True, "Budget Meeting", 12.0)
p = Personal("2026-04-25", "18:00", "Home", False, "Birthday", "Dinner with family")

# prepare list (array) of objects
events = [e, w, p]

# WorkMeeting overrides getDate(); all classes inherit addParticipant from Event
print("--- Call getDate() (shows override in WorkMeeting) and addParticipant (inherited) ---")
for obj in events:
    print("getDate():", obj.getDate())
    obj.addParticipant("Alice")
    print("  first participant stored:", obj.participants[0])

# Demonstrate that subclass-only methods/properties must be accessed carefully.
print("\n--- Attempt to call WorkMeeting-only method getTravelExpenses() on every item (runtime check) ---")
# calculate travel expenses for the WorkMeeting instance so it has a value
w.calculateTravelExpenses()
for obj in events:
    # This will succeed only for WorkMeeting; calling it on other instances will raise
    # AttributeError and crash the program — useful for demonstrating the difference.
    print("getTravelExpenses():", obj.getTravelExpenses())

print("\n--- Access Personal-specific properties/methods using isinstance (safe) ---")
for obj in events:   
    print("Personal eventType:", obj.eventType)
    print("Personal description:", obj.getDescription())
