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
#underLimit         number of people that can also come before hitting the limit
#answer             users input

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------

#initialize variables
maxCap = 0.0
numberOfPeople = 0.0
overLimit = 0.0
underLimit = 0.0
answer = "y"


if answer == "y":

    #getting max room cap
    print("What is the maximum capacity of the room?")
    maxCap = int(input())

    #getting the number of people attending
    print("How many people will be attending?")
    numberOfPeople = int(input())

    #starting if statement
    if numberOfPeople > maxCap:
        #message says there are too many people
        print("Meeting cannot be held as planned due to the fire regulations")

        #calculates how many over limit
        overLimit = numberOfPeople - maxCap

        #displays how many people must leave to meet regulation
        print("To carry on with the event,", overLimit, "people must be excluded to meet fire regulations")
    
    else:
        #message displays fire regulations are met
        print("The meeting meets fire regulations")
        
        #calculates how many more people can attend before hitting max
        underLimit = maxCap - numberOfPeople

        #displays how many more people can attend 
        print(underLimit, "more people can attend before hitting max capacity")
    
    #asks if user wants to enter another room
    print("Would you like to enter another room? (y/n)")

    #users answer
    answer = input()

    #if answer is not valid re-ask question
    while answer != "y" and answer != "Y" and answer != "N" and answer != "n":
        print("Would you like to enter another room? (Please type 'y' or 'n')")

        #users answer
        answer = input()
        
    print("Thanks for using my program!")






