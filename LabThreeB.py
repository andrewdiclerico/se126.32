#LabThreeeB
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------
#counter - record counter
#cantReg - cannot register because of age counter
#nonReg  - old enough but did not register counter
#nonVote - registered but did not vote counter
#vote    - voted counter

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------
counter = 0
cantReg = 0
nonReg = 0
nonVote = 0
Vote = 0

#import csv file
import csv

with open("voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)

    #print names for each column
    print("{0:5}\t{1:5}\t{2:5}\t{3:5}".format("ID Number", "Age", "Registered", "Voted"))

    for rec in file:

        #define variables
        IdNumber = rec[0]
        Age = rec[1]
        Registered = rec[2]
        Voted = rec[3]

        #print data from list
        print("{0:5}\t\t{1:5}\t{2:5}\t\t{3:5}".format(IdNumber, Age, Registered, Voted))

        #calculate if old enough to register
        if int(Age) < 18:
            #not old enough to vote, +1 to the cantReg counter
            cantReg = cantReg + 1
        elif int(Age) >= 18:
            #when old enough to register, calculate if the person has registered
            if Registered == "N":
                #if old enough to register but hasnt, +1 to the nonReg counter
                nonReg = nonReg + 1
            elif Registered == "Y":
                #when person has registered, calculate if the person has voted
                if Voted == "N":
                    #if person has registered but did not vote, +1 to the nonVote counter
                    nonVote = nonVote + 1
                elif Voted == "Y":
                    #if the person has voted, +1 to the vote counter
                    Vote = Vote + 1

        #+1 to the record counter
        counter = counter + 1

#print final outputs of voter info
print("Number of individuals not eligible to register: ", cantReg)
print("Number of individuals who are old enough to vote but have not registered: ", nonReg)
print("number of individuals who are eligible to vote but did not vote: ", nonVote)
print("Number of individuals who did vote", Vote)
print("Number of records processed", counter)