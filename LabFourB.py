#LabFourB
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------
#records          ----------- keeps track of amount of records
#counter          ----------- counts how many times loop has gone for
#avg              ----------- average of age
#houseStark       ----------- amount of people in the alliegance
#houseBaratheon   ----------- amount of people in the alliegance
#houseTully       ----------- amount of people in the alliegance
#nightsWatch      ----------- amount of people in the alliegance
#houseLannister   ----------- amount of people in the alliegance
#houseTargaryen   ----------- amount of people in the alliegance
#answer           ----------- user input


#FUNCTIONS------------------------------------------------------------------
def goodbye():
    print("4.  EXIT")

def goodbyeMessage():
    print("Goodbye!")
#BASE PROGRAM CODE----------------------------------------------------------

answer = ""
records = 0
counter = 0
avg = 0
houseStark = 0
houseBaratheon = 0
houseTully = 0
nightsWatch = 0
houseLannister = 0
houseTargaryen = 0

#import csv file
import csv

with open("lab4A_GOT_NEW.csv") as csvfile:

    file =  csv.reader(csvfile)

    firstName = []
    lastName = []
    age = []
    nickName = []
    houseAllegiance = []

    #print names for each column
    #print("{0:5}\t{1:11}\t{2:5}\t{3:20}\t{4:6}".format("First Name", "Last Name", "Age", "Nickname", "House Allegiance"))

    for rec in file:
        #adds one to records
        records += 1

        #define variables
        firstName.append(rec[0])
        lastName.append(rec[1])
        age.append(int(rec[2]))
        nickName.append(rec[3])
        houseAllegiance.append(rec[4])

        #printing list
        #print("{0:10}\t{1:11}\t{2:5}\t{3:20}\t{4:10}".format(rec[0], rec[1], rec[2], rec[3], rec[4]))

#newline
print(" ")
#print menu
print("Please select a number:")
print("1.  Print all First, Last, and nicknames")
print("2.  Print Last names with House Allegiance and Motto")
print("3.  Print full records")


#user input
answer = input()

#if statement for if user picks 1
if answer == "1":
    #prints title of columns
    print("{0:10}\t{1:11}\t{2:20}".format("First Name", "Last Name", "Nickname"))

    #for loop to print firstname lastname and nickname for each record
    for x in range(0, records):
        
        print("{0:10}\t{1:11}\t{2:20}".format(firstName[x], lastName[x], nickName[x]))

#elif statement if user picks 2
elif answer == "2":

    #prints titles for columns
    print("{0:10}\t{1:15}\t{2:20}".format("Last Name", "House Allegiance", "Motto"))

    #prints last names with house allegiance and motto
    for a in range(0, records):


        #prints last names with house stark and motto
        if houseAllegiance[a] == "House Stark":
             print("{0:16}{1:15}\t\t{2:10}".format(lastName[a], houseAllegiance[a], "Winter is Coming"))

        #prints last names with house baratheon and motto
        elif houseAllegiance[a] == "House Baratheon":
             print("{0:16}{1:15}\t\t{2:10}".format(lastName[a], houseAllegiance[a], "Ours is the fury."))

        #prints last names with house tully and motto
        elif houseAllegiance[a] == "House Tully":
             print("{0:16}{1:15}\t\t{2:10}".format(lastName[a], houseAllegiance[a], "Family. Duty. Honor."))

        #prints last names with night watch and motto
        elif houseAllegiance == "Night's Watch":
            print("{0:16}{1:15}\t\t{2:10}".format(lastName[a], houseAllegiance[a], "And now my watch begins."))
        
        #prints last names with house lannister and motto
        elif houseAllegiance[a] == "House Lannister":
             print("{0:16}{1:15}\t\t{2:10}".format(lastName[a], houseAllegiance[a], "Hear me roar!"))

        #prints last names with house Targaryen and motto
        else:
             print("{0:16}{1:15}\t\t{2:10}".format(lastName[a], houseAllegiance[a], "Fire & Blood"))

#elif statement if user picks 3
elif answer == "3":

    #titles for each column
    print("{0:10}\t{1:11}\t\t{2:5}\t{3:20}\t{4:10}".format("First Name", "Last Name", "Age", "Nickname", "House Allegiance"))

    #for loop to print all records
    for o in range(0, records):
        print("{0:10}\t{1:11}\t{2:10}\t{3:20}\t{4:10}".format(firstName[o], lastName[o], age[o], nickName[o], houseAllegiance[o]))

#elif statement if 4 is chosen
elif answer == "4":
    #goodbye message function
    goodbyeMessage()
    
    




