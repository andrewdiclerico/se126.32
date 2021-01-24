#LabTwoB

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------
#

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------
import csv

with open("lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    print("{0:5}\t{1:5}\t{2:5}\t{3:5}\t{4:5}\t{5:5}\t{6:5}\t{7:5}\t{8:5}".format("Type", "Brand", "CPU", "RAM", "1st Disk", "No HDD", "2nd Disk", "OS", "YR"))

    for rec in file:

        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        firstDisk = rec[4]
        noHdd = rec[5]
        secondDisk = rec[6]
        os = rec[7]
        #yr = rec[8]

        if type == "D":
            type = "Desktop"
        elif type == "L":
            type = "Laptop"

        if brand == "D":
            brand = "Dell"
        elif brand == "HP":
            brand = "HP"
        elif brand == "GW":
            brand = "Gateway"

        #if gpu == 


        print(type, brand, cpu)







