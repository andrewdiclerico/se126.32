#lab6A
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for any

#VARIABLE DICTIONARY--------------
#answer             -------------- users answer
#seatsA             -------------- contains all 'a' seats
#seatsB             -------------- contains all 'b' seats
#seatsC             -------------- contains all 'c' seats
#seatsD             -------------- contains all 'd' seats
#seat               -------------- users seat choice
#row                -------------- users row choice
#
#FUNCTIONS------------------------



#BASE PROGRAM CODE----------------
answer = ""


seatsA = ["A", "A", "A", "A", "A", "A", "A" ]
seatsB = ["B", "B", "B", "B", "B", "B", "B" ]
seatsC = ["C", "C", "C", "C", "C", "C", "C" ]
seatsD = ["D", "D", "D", "D", "D", "D", "D" ]

#asks user if they would like to choose a seat
print("Would you like to choose a seat? (Y/N)")

answer = input()

while answer == "Y" or answer == "y":
    
    print("ROW\tSEAT\tSEAT\tSEAT\tSEAT")

    #display lists to console
    for i in range(0, 7):

        print("{0}\t{1}\t{2}\t{3}\t{4}".format(i + 1, seatsA[i], seatsB[i], seatsC[i], seatsD[i]))


    #ask user for row number
    row = int(input("Enter the ROW you wish to sit in: "))
    #row - 1 + index of list the seat confirmation needs to be placed in: x

    seat = input("Enter the SEAT you wish to sit in: ")
    #seat = which list we need to replace the value in

    print("You want to sit in: {0}{1}".format(row, seat))

    if seat == "A" or seat == "a":
        seatsA[row - 1] = "X"
        print("ROW\tSEAT\tSEAT\tSEAT\tSEAT")
        for i in range(0, 7):

            print("{0}\t{1}\t{2}\t{3}\t{4}".format(i + 1, seatsA[i], seatsB[i], seatsC[i], seatsD[i]))

    elif seat == "B" or seat == "b":
        seatsB[row - 1] = "X"
        print("ROW\tSEAT\tSEAT\tSEAT\tSEAT")
        for i in range(0, 7):

            print("{0}\t{1}\t{2}\t{3}\t{4}".format(i + 1, seatsA[i], seatsB[i], seatsC[i], seatsD[i]))

    elif seat == "C" or seat == "c":
        seatsC[row - 1] = "X"
        print("ROW\tSEAT\tSEAT\tSEAT\tSEAT")
        for i in range(0, 7):

            print("{0}\t{1}\t{2}\t{3}\t{4}".format(i + 1, seatsA[i], seatsB[i], seatsC[i], seatsD[i]))

    elif seat == "D" or seat == "d":
        seatsD[row - 1] = "X"
        print("ROW\tSEAT\tSEAT\tSEAT\tSEAT")
        for i in range(0, 7):

            print("{0}\t{1}\t{2}\t{3}\t{4}".format(i + 1, seatsA[i], seatsB[i], seatsC[i], seatsD[i]))

    print("Would you like to select another seat? (Y/N)")

    answer = input()
    
print("Thanks for selecting a seat/s")