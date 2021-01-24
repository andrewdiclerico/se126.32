#LabTwoB
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------
#counter       --------------count of how many computers
#type          --------------type of computer
#brand         --------------brand of computer
#cpu           --------------what kind of cpu
#ram           --------------ram size
#firstDisk     --------------space on first disk
#noHdd         --------------hdd?
#secondDisk    --------------second disk space
#os            --------------operating system
#yr            --------------year of production

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------

#starts counter at 0
counter = 0

#import csv file
import csv

with open("lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    #print names for each column
    print("{0:5}\t{1:5}\t{2:5}\t{3:5}\t{4:5}\t{5:5}\t{6:5}\t{7:5}\t{8:5}".format("Type", "Brand", "CPU", "RAM", "1st Disk", "No HDD", "2nd Disk", "OS", "YR"))

    for rec in file:

        #define variables
        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        firstDisk = rec[4]
        noHdd = rec[5]
        secondDisk = rec[6]
        os = rec[7]
        yr = rec[8]

        #if statement to decide if desktop or laptop
        if type == "D":
            type = "Desktop"
        elif type == "L":
            type = "Laptop"

        #if statement to determine if dell, hp or gateway
        if brand == "DL":
            brand = "Dell"
        elif brand == "HP":
            brand = "HP"
        elif brand == "GW":
            brand = "Gateway"

        #determines if computer has a second disk
        if noHdd == "1":
            secondDisk = ""
        elif noHdd == "2":
            secondDisk = secondDisk

        #+ 1 for the computer counter
        counter = counter + 1

        #print information from each column in the row
        print("{0:5}\t{1:5}\t{2:5}\t{3:5}\t{4:5}\t\t{5:5}\t{6:5}\t\t{7:5}\t{8:5}".format(type, brand, cpu, ram, firstDisk, noHdd, secondDisk, os, yr))

#print total number of computers
print("Number of computers: ", counter)





