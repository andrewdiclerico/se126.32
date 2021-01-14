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

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------

#initialize variables
maxCap = 0
numberOfPeople = 0
overLimit = 0
underLimit = 0 
answer = ""

#getting max room cap.
print("What is the maximum capacity of the room?")

maxCap = float(input())

#getting number of people attending
print("How many people are attending the room?")

numberOfPeople = float(input())

#starting if statement 
#if max capacity is reached then message displays how many people must be excluded
if maxCap < numberOfPeople:
    print("Meeting cannot be held as planned due to the fire regulations")

    #calculates how many over limit
    overLimit = numberOfPeople - maxCap

    print("To carry on with the event, ", overLimit, "people must be excluded to meet fire regulations")
#if max capacity isnt reached then message displays how many more people can come
else :
    #calculates how many under limit
    underLimit = maxCap - numberOfPeople

    print("The meeting can be held and ", underLimit, "more people can come before the max is reached.")

#asks user if the would like to enter another room
print("Would you like to enter another room? (Y/N)")

#user's answer
answer = input()

#if user doesnt answer with y or n 
if answer != "y" or answer != "Y" or answer != "n" or answer != "N":
    print("Would you like to enter another room? (Please use 'Y' or 'N')")
    answer = input()

while answer == "y" or answer == "Y":
    #getting max room cap.
    print("What is the maximum capacity of the room?")

    maxCap = float(input())

    #getting number of people attending
    print("How many people are attending the room?")

    numberOfPeople = float(input())

    #starting if statement 
    #if max capacity is reached then message displays how many people must be excluded
    if maxCap < numberOfPeople:
        print("Meeting cannot be held as planned due to the fire regulations")

        #resets answer
        answer = ""

        #calculates how many over limit
        overLimit = numberOfPeople - maxCap
        print("Number of people that must leave to meet requirements:")
        print(overLimit)
       

    #if max capacity isnt reached then message displays how many more people can come
    else :
        #calculates how many under limit
        underLimit = maxCap - numberOfPeople

        #resets answer
        answer = ""

        print("The meeting can be held and ", underLimit, "more people can come before the max is reached.")

    #asks user if the would like to enter another room
    print("Would you like to enter another room? (Y/N)")

    #user's answer
    answer = input()

    #if user doesnt answer with y or n 
    if answer != "y" or answer != "Y" or answer != "n" or answer != "N":
        print("Would you like to enter another room? (Please use 'Y' or 'N')")
        answer = input()
