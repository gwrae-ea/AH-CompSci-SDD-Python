import numpy, pandas #numpy and pandas provide useful functions for the display and manipulation of 2-d Arrays

rows, cols = (6,9) #define the number of rows and columns in the 2-D Array
game = [[" " for i in range(cols+1)] for j in range(rows+1)] #Create the empty 2-D Array using a nested loop. Note the use of +1 to account for 0th element.

#used to set a specific element in an array
game[3][7] = "P"
game[2][3] = "E"
game[5][2] = "E"

#the following sections of code use numpy and pandas imported modules to ease display of 2-D Arrays.
rowHeaders = ["1","2","3","4","5","6"] #creates the row headers for the display
colHeaders = ["1","2","3","4","5","6","7","8","9"] # creates the column headers for the display
dispGame = numpy.array(game)
dispGame = pandas.DataFrame(dispGame[1:,1:], columns = colHeaders, index = rowHeaders)
dispGame.columns.name = "Game"

print (dispGame)
