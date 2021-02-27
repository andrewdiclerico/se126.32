#lab6A
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for any

#VARIABLE DICTIONARY--------------
#records            --------------
#answer             -------------- user decision
#tracker            -------------- tracks how many searches
#menuAnswer         -------------- user decision for menu
#FUNCTIONS------------------------
def menu():
    print("Choose a last name: ")
    print("1.  Gallo")
    print("2.  Givens")
    print("3.  Haywood")
    print("4.  Hong")
    print("5.  Hunt")
    print("6.  Jennings")
    print("7.  Jim")
    print("8.  Johnson")
    print("9.  Jones")
    print("10.  Lawson")
    print("11.  Lopez")
    print("12.  McClure")
    print("13.  McDaniel")
    print("14.  Moore")
    print("15.  Oneil")
    print("16.  Parker")
    print("17.  Richardson")
    print("18.  Salas")
    print("19.  Scott")
    print("20.  Sexton")
    print("21.  Starr")
    print("22.  Stephens")
    print("23.  Stevonson")
    print("24.  Sumlin")
    print("25.  Vess")
    print("26.  Williams")

#BASE PROGRAM CODE----------------
records = 0
answer = ""
tracker = 0
menuAnswer = 0

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

    menu()

    #user input
    menuAnswer = input()


    #for loop
    for a in range(0, records):
        #if statement to print all info for Gallo
        if lastName[a] == "Gallo" and menuAnswer == "1":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Givens
        elif lastName[a] == "Givens" and menuAnswer == "2":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Haywood
        elif lastName[a] == "Haywood" and menuAnswer == "3":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Hong
        elif lastName[a] == "Hong" and menuAnswer == "4":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Hunt
        elif lastName[a] == "Hunt" and menuAnswer == "5":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Jennings
        elif lastName[a] == "Jennings" and menuAnswer == "6":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Jim
        elif lastName[a] == "Jim" and menuAnswer == "7":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Johnson
        elif lastName[a] == "Johnson" and menuAnswer == "8":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Jones
        elif lastName[a] == "Jones" and menuAnswer == "9":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Lawson
        elif lastName[a] == "Lawson" and menuAnswer == "10":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Lopez
        elif lastName[a] == "Lopez" and menuAnswer == "11":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for McClure
        elif lastName[a] == "McClure" and menuAnswer == "12":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for McDaniel
        elif lastName[a] == "McDaniel" and menuAnswer == "13":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Moore
        elif lastName[a] == "Moore" and menuAnswer == "14":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Oneil
        elif lastName[a] == "Oneil" and menuAnswer == "15":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Parker
        elif lastName[a] == "Parker" and menuAnswer == "16":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Richardson
        elif lastName[a] == "Richardson" and menuAnswer == "17":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Salas
        elif lastName[a] == "Salas" and menuAnswer == "18":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Scott
        elif lastName[a] == "Scott" and menuAnswer == "19":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Sexton
        elif lastName[a] == "Sexton" and menuAnswer == "20":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Starr
        elif lastName[a] == "Starr" and menuAnswer == "21":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Stephens
        elif lastName[a] == "Stephens" and menuAnswer == "22":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statment to print all info for Stevenson
        elif lastName[a] == "Stevenson" and menuAnswer == "23":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Sumlin
        elif lastName[a] == "Sumlin" and menuAnswer == "24":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Vess
        elif lastName[a] == "Vess" and menuAnswer == "25":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for Williams
        elif lastName[a] == "Williams" and menuAnswer == "26":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #else if nothing is found
        else:
            print("No information found")
            
    #shows number of times user has made a search
    print("Search #", tracker)

    #asks if user would like to search again
    print("Would you like to search again? (Y/N) ")

    #user decision
    answer = input()

#goodbye message
print("Thanks for searching! Goodbye!")

