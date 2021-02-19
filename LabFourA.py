#LabFourA
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
#houseTargaryen   -----------amount of people in the alliegance

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------

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
    print("{0:5}\t{1:11}\t{2:5}\t{3:20}\t{4:6}".format("First Name", "Last Name", "Age", "Nickname", "House Allegiance"))

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
        print("{0:10}\t{1:11}\t{2:5}\t{3:20}\t{4:10}".format(rec[0], rec[1], rec[2], rec[3], rec[4]))

#newline
print(" ")

#prints column title
print("{0:5}\t{1:11}\t{2:5}\t{3:20}\t{4:6}\t{5:6}".format("First Name", "Last Name", "Age", "Nickname", "House Allegiance", "Motto"))

#for loop to get each house's motto
for i in range(0, records):
    

    #prints with house stark motto
    if houseAllegiance[i] == "House Stark":
        print("{0:16}{1:8}{2:10}\t{3:20}\t{4:10}\t\t{5:15}".format(firstName[i], lastName[i], age[i], nickName[i], houseAllegiance[i], "Winter is Coming"))

    #prints with house baratheon motto
    elif houseAllegiance[i] == "House Baratheon":
        print("{0:16}{1:8}{2:10}\t{3:20}\t{4:10}\t\t{5:15}".format(firstName[i], lastName[i], age[i], nickName[i], houseAllegiance[i], "Ours is the fury."))

    #prints with house tully motto
    elif houseAllegiance[i] == "House Tully":
        print("{0:16}{1:8}{2:10}\t{3:20}\t{4:10}\t\t{5:15}".format(firstName[i], lastName[i], age[i], nickName[i], houseAllegiance[i], "Family. Duty. Honor."))

    #prints with night watch motto
    elif houseAllegiance[i] == "Night's Watch":
        print("{0:16}{1:8}{2:10}\t{3:20}\t{4:10}\t\t{5:15}".format(firstName[i], lastName[i], age[i], nickName[i], houseAllegiance[i], "And now my watch begins."))

    #prints with house lannister motto
    elif houseAllegiance[i] == "House Lannister":
        print("{0:16}{1:8}{2:10}\t{3:20}\t{4:10}\t\t{5:15}".format(firstName[i], lastName[i], age[i], nickName[i], houseAllegiance[i], "Hear me roar!"))

    #prints with house Targaryen
    else:
        print("{0:16}{1:8}{2:10}\t{3:20}\t{4:10}\t\t{5:15}".format(firstName[i], lastName[i], age[i], nickName[i], houseAllegiance[i], "Fire & Blood"))

#for loop to calculate average age and get amount of people on list
for x in range(0, records):
    avg = avg + age[x]
    counter = counter + 1

#empty line
print(" ")

#prints average age
avg = avg / counter
print("The average age is:", "{0:.0f}".format(avg))

#prints number of people on list
print("There are", counter, "people on the list")

#for loop to keep track of how many people in each house allegiance
for f in range(0, records):
        
    #adds one to house stark
    if houseAllegiance[f] == "House Stark":
        houseStark = houseStark + 1

    #adds one to house baratheon
    elif houseAllegiance[f] == "House Baratheon":
        houseBaratheon = houseBaratheon + 1

    #adds one to house tully
    elif houseAllegiance[f] == "House Tully":
        houseTully = houseTully + 1

    #adds one to nights watch
    elif houseAllegiance[f] == "Night's Watch":
        nightsWatch = nightsWatch + 1

    #adds one to house lannister
    elif houseAllegiance[f] == "House Lannister":
        houseLannister = houseLannister + 1

    #adds one to house targaryen
    else:
        houseTargaryen = houseTargaryen + 1
    
#prints the amount of people in each house
print("Tallies for House Stark:", houseStark)
print("Tallies for House Baratheon:", houseBaratheon)
print("Tallies for House Tully:", houseTully)
print("Tallies for Night's Watch:", nightsWatch)
print("Tallies for House Lannister:", houseLannister)
print("Tallies for House Taragaryen:", houseTargaryen)