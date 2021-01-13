#LabOneA

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------
#maxCap             maximum capacity of a room
#numberOfPeople     Number of people attending room
#overLimit          number of people over the limit

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------

#initialize variables
maxCap = 0
numberOfPeople = 0
overLimit = 0

#getting max room cap.
maxCap = float(input(print("What is the maximum capacity of the room?")))

#getting number of people attending
numberOfPeople = float(input(print("How many people are attending the room?")))

if maxCap > numberOfPeople:
    print("Meeting cannot be held as planned due to the fire regulations")

    overLimit = numberOfPeople - maxCap

    print("To carry on with the event, ", overLimit, "people must be excluded to meet fire regulations")
    