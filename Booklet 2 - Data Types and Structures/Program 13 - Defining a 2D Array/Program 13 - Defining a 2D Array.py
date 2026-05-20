"""
Program 13 - Defining a 2D Array

Design
- The program models a fixed game grid with known dimensions (6 rows, 9 columns).
- A 2D array is created first, then individual cells are updated by coordinate.
- One extra row and one extra column are included in storage so the displayed grid can use
	human-friendly numbering (1..6 and 1..9) while keeping index logic predictable.
- Row and column header lists are prepared to label the final printed table.
- Numpy and pandas are used only to format output clearly as a table.

SQA-RL
DECLARE rows <- 6
DECLARE cols <- 9
DECLARE game : ARRAY[0:rows, 0:cols] OF STRING

FOR r FROM 0 TO rows
	FOR c FROM 0 TO cols
		SET game[r,c] <- " "
	NEXT c
NEXT r

SET game[3,7] <- "P"
SET game[2,3] <- "E"
SET game[5,2] <- "E"

DECLARE rowHeaders : ARRAY[1:rows] OF STRING
DECLARE colHeaders : ARRAY[1:cols] OF STRING
SET rowHeaders <- ["1","2","3","4","5","6"]
SET colHeaders <- ["1","2","3","4","5","6","7","8","9"]

SET dispGame <- CONVERT_TO_NUMPY_ARRAY(game)
SET dispGame <- CONVERT_TO_DATAFRAME(
	dispGame[1..rows, 1..cols],
	colHeaders,
	rowHeaders
)
SET COLUMN_NAME(dispGame) <- "Game"
OUTPUT dispGame
"""

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
