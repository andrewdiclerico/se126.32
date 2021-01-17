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
#answer             user decision
#difference         difference between people attending and max capacity

#initialize variables------------------------------------------------------
maxCap = 0
numberOfPeople = 0
overLimit = 0.0
underLimit = 0.0
answer = "y"
reg = 0


#FUNCTIONS------------------------------------------------------------------
def message():
    print("Would you like to enter another room? (Y/N)")
    #users answer
    answer = input()

    #if answer is not valid re-ask question
    while answer != "y" and answer != "Y" and answer != "N" and answer != "n":
        print("Would you like to enter another room? (Please type 'y' or 'n')")

        #users answer
        answer = input()
        return answer

    
#intro function
def intro():
    print("Welcome to the room capacity calculator")
 
#getting max capacity of room
def capacity():
    print("What is the maximum capacity of the room?")
    maxCap = int(input())
    return maxCap
    
#getting the amount of people attending
def attendees():
    print("How many people will be attending?")
    numberOfPeople = int(input())
    
    return numberOfPeople

#calculating the difference from capacity and attendees
def register():
    reg = capacity() - attendees() 
    return reg

#BASE PROGRAM CODE----------------------------------------------------------

intro()

while answer == "y":

    
    maxCap = capacity()

    numberOfPeople = attendees()


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
    message()


        
    print("Thank for using my program!")






