#lab5A
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for any

#VARIABLE DICTIONARY--------------
#records            --------------
#answer             -------------- user decision
#lname              -------------- last name being searched for (user input)
#tracker            -------------- tracks how many searches
#FUNCTIONS------------------------



#BASE PROGRAM CODE----------------
records = 0
answer = ""
lname = ""
tracker = 0

#import csv file
import csv

with open("lab5_updated.csv") as csvfile:

    file =  csv.reader(csvfile)

    #variables
    lastName = []
    firstName = []
    dateOfBirth = []
    

    for rec in file:
        
        records = records + 1

        #define variables
        lastName.append(rec[0])
        firstName.append(rec[1])
        dateOfBirth.append(rec[2])

print("Would you like to make a search? (Y/N)")

answer = input()

while answer == "Y" or answer == "y":
    #adds one to tracker
    tracker = tracker + 1


    #asks for last name
    print("Please enter last name: ")

    #user input
    lname = input()

    #for loop
    for a in range(0, records):
        #if lname = gallo all names with last name gallo are displayed
        if lastName[a] == "Gallo" and lname == "Gallo":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = givens all names with the last name givens are displayed
        elif lastName[a] == "Givens" and lname == "Givens":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = haywood all names with the last name haywood are displayed
        elif lastName[a] == "Haywood" and lname == "Haywood":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = hong all names with the last name hong are displayed
        elif lastName[a] == "Hong" and lname == "Hong":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = Hunt all names with the last name hunt are displayed
        elif lastName[a] == "Hunt" and lname == "Hunt":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = jennings all names with the last name jennings are displayed
        elif lastName[a] == "Jennings" and lname == "Jennings":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = jim all names with the last name jim are displayed
        elif lastName[a] == "Jim" and lname == "Jim":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = johnson all names with the last name johnson are displayed
        elif lastName[a] == "Johnson" and lname == "Johnson":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = Jones all names with the last name jones are displayed
        elif lastName[a] == "Jones" and lname == "Jones":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = Lawson all names with the last name lawson are displayed
        elif lastName[a] == "Lawson" and lname == "Lawson":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = lopez all names with the last name lopez are displayed
        elif lastName[a] == "Lopez" and lname == "Lopez":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = mcclure all names with the last name mcclure are displayed
        elif lastName[a] == "McClure" and lname == "McClure":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = mcdaniel all names with the last name mcdaniel are displayed
        elif lastName[a] == "McDaniel" and lname == "McDaniel":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = moore all names with the last name moore are displayed
        elif lastName[a] == "Moore" and lname == "Moore":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = oneil all names with the last name oneil are displayed
        elif lastName[a] == "Oneil" and lname == "Oneil":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = parker all names with the last name parker are displayed
        elif lastName[a] == "Parker" and lname == "Parker":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = richardson all names with the last name richardson are displayed
        elif lastName[a] == "Rachardson" and lname == "Richardson":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = salas all names with the last name salas are displayed
        elif lastName[a] == "Salas" and lname == "Salas":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = scott all names with the last name scott are displayed
        elif lastName[a] == "Scott" and lname == "Scott":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = sexton all names with the last name sexton are displayed
        elif lastName[a] == "Sexton" and lname == "Sexton":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = starr all names with the last name starr are displayed
        elif lastName[a] == "Starr" and lname == "Starr":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = stephens all names with the last name stephens are displayed
        elif lastName[a] == "Stephens" and lname == "Stephens":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = stevenson all names with the last name stevenson are displayed
        elif lastName[a] == "Stevenson" and lname == "Stevenson":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = sumlin all names with the last name sumlin are displayed
        elif lastName[a] == "Sumlin" and lname == "Sumlin":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif lname = vess all names with the last name vess are displayed
        elif lastName[a] == "Vess" and lname == "Vess":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #else statement all names with the last name williams are displayed
        else:
            if lastName[a] == "Williams" and lname == "Williams":
                print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

    #shows number of times user has made a search
    print("Search #", tracker)

    #asks to enter another name
    print("Would you like to enter another name? (Y/N) ")

    #user decision
    answer = input()

#goodbye message
print("Thanks for searching! Goodbye!")