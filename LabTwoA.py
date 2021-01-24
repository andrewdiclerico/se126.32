#LabTwoA

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------
#total_records --------------- total records processed
#over_limit    --------------- number of people over limit
#difference    --------------- difference between over_limit and total_records

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------

import csv

total_records = 0
over_limit = 0
difference = 0

with open("lab2a (1).csv") as csvfile:

    file = csv.reader(csvfile)
       
    print("{0:20}\t\t{1:7}\t{2:3}\t{3:5}".format("Room Name", "Room Max", "People Registered", "  Over"))

    for rec in file:
        room_name = rec[0]

        room_max = rec[1]

        People_reg = rec[2]

        total_records = total_records + 1

        if People_reg > room_max:

            difference = int(People_reg) - int(room_max)

            print("{0:20}\t\t{1:7}\t\t{2:7}\t\t\t{3:5}".format(room_name, room_max, People_reg, difference))

            over_limit = over_limit + 1


print("Processed ", total_records, "records.")
print("There are ", over_limit, "rooms over the limit.")
