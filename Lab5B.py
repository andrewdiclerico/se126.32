#lab5B
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for any

#VARIABLE DICTIONARY--------------
#records            --------------
#answer             -------------- user decision
#dOfb               -------------- date of birth being searched for (user input)
#tracker            -------------- tracks how many searches
#FUNCTIONS------------------------



#BASE PROGRAM CODE----------------
records = 0
answer = ""
dOfB = ""
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


    #asks for date of birth
    print("Ex. 00/00/0000")
    print("Please enter date of birth: ")

    #user input
    dOfB = input()

    #for loop
    for a in range(0, records):
        #if statement to print all info for 01/01/2000
        if dateOfBirth[a] == "01/01/2000" and dOfB == "01/01/2000":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 02/03/2010
        elif dateOfBirth[a] == "02/03/2010" and dOfB == "02/03/2010":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 03/25/1999
        elif dateOfBirth[a] == "03/25/1999" and dOfB == "03/25/1999":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 04/12/2002
        elif dateOfBirth[a] == "04/12/2002" and dOfB == "04/12/2002":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 01/15/1998
        elif dateOfBirth[a] == "01/15/1998" and dOfB == "01/15/1998":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 03/17/1999
        elif dateOfBirth[a] == "03/17/1999" and dOfB == "03/17/1999":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 10/10/1997
        elif dateOfBirth[a] == "10/10/1997" and dOfB == "10/10/1997":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 08/23/2000
        elif dateOfBirth[a] == "08/23/2000" and dOfB == "08/23/2000":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 09/07/1997
        elif dateOfBirth[a] == "09/07/1997" and dOfB == "09/07/1997":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 04/06/1999
        elif dateOfBirth[a] == "04/06/1999" and dOfB == "04/06/1999":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 07/09/2001
        elif dateOfBirth[a] == "07/09/2001" and dOfB == "07/09/2001":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 11/17/2005
        elif dateOfBirth[a] == "11/17/2005" and dOfB == "11/17/2005":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 01/23/1999
        elif dateOfBirth[a] == "01/23/1999" and dOfB == "01/23/1999":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 06/06/1006
        elif dateOfBirth[a] == "06/06/1006" and dOfB == "06/06/1006":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 04/20/2003
        elif dateOfBirth[a] == "04/20/2003" and dOfB == "04/20/2003":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 10/12/1998
        elif dateOfBirth[a] == "10/12/1998" and dOfB == "10/12/1998":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 07/05/2000
        elif dateOfBirth[a] == "07/05/2000" and dOfB == "07/05/2000":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 09/17/1997
        elif dateOfBirth[a] == "09/17/1997" and dOfB == "09/17/1997":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 03/25/2000
        elif dateOfBirth[a] == "03/25/2000" and dOfB == "03/25/2000":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 12/12/1998
        elif dateOfBirth[a] == "12/12/1998" and dOfB == "12/12/1998":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 07/15/2000
        elif dateOfBirth[a] == "07/15/2000" and dOfB == "07/15/2000":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 10/22/1997
        elif dateOfBirth[a] == "10/22/1997" and dOfB == "10/22/1997":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statment to print all info for 05/05/1001
        elif dateOfBirth[a] == "05/05/1001" and dOfB == "05/05/1001":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 09/27/2002
        elif dateOfBirth[a] == "09/27/2002" and dOfB == "09/27/2002":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 07/19/2002
        elif dateOfBirth[a] == "07/19/2002" and dOfB == "07/19/2002":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

        #elif statement to print all info for 10/12/2002
        elif dateOfBirth[a] == "10/12/2002" and dOfB == "10/12/2002":
            print("{0:10}{1:10}{2:10}".format(lastName[a], firstName[a], dateOfBirth[a]))

    #shows number of times user has made a search
    print("Search #", tracker)

    #asks if user would like to search again
    print("Would you like to search again? (Y/N) ")

    #user decision
    answer = input()

#goodbye message
print("Thanks for searching! Goodbye!")