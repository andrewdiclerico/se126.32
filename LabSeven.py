#lab7
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for any

#VARIABLE DICTIONARY--------------
#searchAns   ------- user answer if they want to search
#num         ------- number chosen from menu
#menuAns     ------- same as num
#fName       ------- first name
#id          ------- id code
#lName       ------- number for last name menu
#houseName   ------- number for house name/allegiance


#FUNCTIONS------------------------
def menu(num):
    print("    Search Menu  --  Please make a selection (1-5)")
    print("1.  Search by FIRST NAME")
    print("2.  Search by ID CODE")
    print("3.  Search by LAST NAME")
    print("4.  Search by ALLEGIANCE")
    print("5.  EXIT")

    num = int(input())
   
    return num

def goodbye():
    print("Thank you for searching!")
    print("Goodbye!")

from os import system, name

from time import sleep

def clear():
    if name =='nt':
        _ = system('cls')

#BASE PROGRAM CODE----------------
records = 0
searchAns = ""
num = 0
menuAns = 0
fName = ""
id = ""
lName = 0
houseName = 0

#import csv file
import csv

with open("GOT_bubble_sort_7.csv") as csvfile:

    file =  csv.reader(csvfile)

    #variables
    idCode = []
    lastName = []
    firstName = []
    age = []
    allegiance = []
    

    for rec in file:
        
        records = records + 1

        #define variables
        idCode.append(rec[0])
        lastName.append(rec[1])
        firstName.append(rec[2])
        age.append(rec[3])
        allegiance.append(rec[4])

print("Would you like to make a search? (Y/N)")

searchAns = input()

while searchAns == "y" or searchAns == "Y":
    menuAns = menu(num)
    print("You selected", menuAns)
    
    #search by first name
    if menuAns == 1:
        print("Please enter first name: ")

        fName = input()

        #print column names
        print("{0:15}{1:15}{2:15}{3:10}{4:10}".format("Id Code", "Last Name", "First Name", "Age", "Allegiance"))


        #for loop
        for a in range(0, records):
            #if statement to print all info for Gendry
            if firstName[a] == "Gendry" and fName == "Gendry":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Missandei
            elif firstName[a] == "Missandei" and fName == "Missandei":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Varys
            elif firstName[a] == "Varys" and fName == "Varys":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for John
            elif firstName[a] == "John" and fName == "John":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))
  
            #if statement to print all info for Robin
            elif firstName[a] == "Robin" and fName == "Robin":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))
  
            #if statement to print all info for Robert
            elif firstName[a] == "Robert" and fName == "Robert":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Tormund
            elif firstName[a] == "Tormund" and fName == "Tormund":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))
    
            #if statement to print all info for Jaime
            elif firstName[a] == "Jaime" and fName == "Jaime":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))
  
            #if statement to print all info for Cersei
            elif firstName[a] == "Cersei" and fName == "Cersei":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))
  
            #if statement to print all info for Myrcella
            elif firstName[a] == "Myrcella" and fName == "Myrcella":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))
  
            #if statement to print all info for Tommen
            elif firstName[a] == "Tommen" and fName == "Tommen":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Joffrey
            elif firstName[a] == "Joffrey" and fName == "Joffrey":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Tyrion
            elif firstName[a] == "Tyrion" and fName == "Tyrion":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Joreh
            elif firstName[a] == "Jorah" and fName == "Joreh":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Davos
            elif firstName[a] == "Davos" and fName == "Davos":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Jon
            elif firstName[a] == "Jon" and fName == "Jon":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Robb
            elif firstName[a] == "Robb" and fName == "Robb":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))
  
            #if statement to print all info for Brandon
            elif firstName[a] == "Brandon" and fName == "Brandon":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Arya
            elif firstName[a] == "Arya" and fName == "Arya":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Sansa
            elif firstName[a] == "Sansa" and fName == "Sansa":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Eddard
            elif firstName[a] == "Eddard" and fName == "Eddard":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Viserys
            elif firstName[a] == "Viserys" and fName == "Viserys":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Daenerys
            elif firstName[a] == "Daenerys" and fName == "Daenerys":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Lysa
            elif firstName[a] == "Lysa" and fName == "Lysa":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

            #if statement to print all info for Catelyn
            elif firstName[a] == "Catelyn" and fName == "Catelyn":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[a], lastName[a], firstName[a], age[a], allegiance[a]))

    #search by id code
    elif menuAns == 2:
        #ask user for id code
        print("Please enter your Id Code: ")
        
        id = input()

        #print column names
        print("{0:15}{1:15}{2:15}{3:10}{4:10}".format("Id Code", "Last Name", "First Name", "Age", "Allegiance"))

        for f in range(0, records):
            #if statement to print all info for battleAxe
            if idCode[f] == "battleAxe" and id == "battleAxe":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for butterfly01
            if idCode[f] == "butterfly01" and id == "butterfly01":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for spider
            if idCode[f] == "spider" and id == "spider":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for coins4eyes
            if idCode[f] == "coins4eyes" and id == "coins4eyes":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for sweetBaby
            if idCode[f] == "sweetBaby" and id == "sweetBaby":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for stagKing
            if idCode[f] == "stagKing" and id == "stagKing":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for kingWildling
            if idCode[f] == "kingWildling" and id == "kingWildling":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for goldenHand
            if idCode[f] == "goldenHand" and id == "goldenHand":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for lioness
            if idCode[f] == "lioness" and id == "lioness":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for theFairest
            if idCode[f] == "theFairest" and id == "theFairest":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for theFallen
            if idCode[f] == "theFallen" and id == "theFallen":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for theSwollen
            if idCode[f] == "theSwollen" and id == "theSwollen":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for littleLionMan
            if idCode[f] == "littleLionMan" and id == "littleLionMan":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for greyFriend
            if idCode[f] == "greyFriend" and id == "greyFriend":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for onionKnight
            if idCode[f] == "onionKnight" and id == "onionKnight":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for ghost
            if idCode[f] == "ghost" and id == "ghost":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for theWolf
            if idCode[f] == "theWolf" and id == "theWolf":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for raven3
            if idCode[f] == "raven3" and id == "raven3":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for girl
            if idCode[f] == "girl" and id == "girl":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for littleDove
            if idCode[f] == "littleDove" and id == "littleDove":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for father
            if idCode[f] == "father" and id == "father":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for goldenCrown
            if idCode[f] == "goldenCrown" and id == "goldenCrown":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for khaleesi
            if idCode[f] == "khaleesi" and id == "khaleesi":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for flightlessBird
            if idCode[f] == "flightlessBird" and id == "flightlessBird":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

            #if statement to print all info for mother
            if idCode[f] == "mother" and id == "mother":
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[f], lastName[f], firstName[f], age[f], allegiance[f]))

    #search by last name
    elif menuAns == 3:
        print("Please select a number:      (1 - 11)")
        print("1.  Arryn")
        print("2.  Baratheon")
        print("3.  Gianstbane")
        print("4.  Lannister")
        print("5.  Mormont")
        print("6.  Seaworth")
        print("7.  Snow")
        print("8.  Stark")
        print("9.  Targaryen")
        print("10. Tully")
        print("11. Other")

        #user decision
        lName = int(input())

        #print column names
        print("{0:15}{1:15}{2:15}{3:10}{4:10}".format("Id Code", "Last Name", "First Name", "Age", "Allegiance"))

        for j in range(0, records):
            #print all info for last name Arryn
            if lastName[j] == "Arryn" and lName == 1:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Baratheon
            elif lastName[j] == "Baratheon" and lName == 2:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Gianstbane
            elif lastName[j] == "Gianstbane" and lName == 3:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Lannister
            if lastName[j] == "Lannister" and lName == 4:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Mormont
            if lastName[j] == "Mormont" and lName == 5:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Seaworth
            if lastName[j] == "Seaworth" and lName == 6:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Snow
            if lastName[j] == "Snow" and lName == 7:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Stark
            if lastName[j] == "Stark" and lName == 8:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Targaryen
            if lastName[j] == "Targaryen" and lName == 9:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for last name Tully
            if lastName[j] == "Tully" and lName == 10:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

            #print all info for no last name
            if lastName[j] == "" and lName == 11:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[j], lastName[j], firstName[j], age[j], allegiance[j]))

    #search by allegiance
    elif menuAns == 4:
        
        print("Please select a number:      (1 - 4)")
        print("1.  House Stark")
        print("2.  House Targaryen")
        print("3.  House Baratheon of King's Landing")
        print("4.  House Baelish")

        houseName = int(input())

        #print column names
        print("{0:15}{1:15}{2:15}{3:10}{4:10}".format("Id Code", "Last Name", "First Name", "Age", "Allegiance"))

        for m in range(0, records):
            #print all info for last name House Stark
            if allegiance[m] == "House Stark" and houseName == 1:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[m], lastName[m], firstName[m], age[m], allegiance[m]))

            #print all info for last name House Targaryen
            elif allegiance[m] == "House Targaryen" and houseName == 2:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[m], lastName[m], firstName[m], age[m], allegiance[m]))

            #print all info for last name House Baratheon of Kings Landing
            elif allegiance[m] == "House Baratheon of Kings Landing" and houseName == 3:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[m], lastName[m], firstName[m], age[m], allegiance[m]))

            #print all info for last name House Baelish
            elif allegiance[m] == "House Baelish" and houseName == 4:
                print("{0:15}{1:15}{2:15}{3:10}{4:10}".format(idCode[m], lastName[m], firstName[m], age[m], allegiance[m]))


    #asks user if they would like to make another search
    print("Would you like to make another search? (Y/N)")

    #user input
    searchAns = input()

    sleep(3)

    clear()



#goodbye function
goodbye()

