#MidTerm
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY-------------------------------------------------------
#records            --------------- record counter
#answer             --------------- user input
#start              --------------- start while loop?

#FUNCTIONS------------------------------------------------------------------
#intro message
def intro():
    print("Welcome to the Volkswagen/Audi Group Online Dealership!")
    print("Would you like to search for a car? (Y/N)")

#menu
def menu():
    #space
    print(" ")
    #print menu
    print("Please select a number:")
    print("1.  Show Volkswagen inventory")
    print("2.  Show Audi inventory")
    print("3.  Show BMW inventory")
    print("4.  Show Porsche inventory")
    print("5.  Show Skoda inventory")
    print("6.  Show Bentley inventory")


#BASE PROGRAM CODE----------------------------------------------------------
records = 0
answer = ""
start = ""


#import csv file
import csv

with open("cars.csv") as csvfile:

    file =  csv.reader(csvfile)

    #variables
    condition = []
    brand = []
    year = []
    miles = []
    model = []
    price = []

    for rec in file:
        #adds one to records
        records += 1

        #define variables
        condition.append(rec[0])
        brand.append(rec[1])
        year.append(rec[2])
        miles.append(rec[3])
        model.append(rec[4])
        price.append(int(rec[5]))



#intro message
intro()

#user input to decide to start while loop
start = input()

#while loop 
while start == "Y" or start == "y":
    #asks if they want used or new
    print("Please select a number:")
    print("1.  New Vehicles")
    print("2.  Used Vehicles")

    #user input
    answer = input()

    #if statement if user picks 1(new vehicles)
    if answer == "1":
    
        answer = 0
    
        #brand menu
        menu()

        #user input
        answer = input()
    
        #column titles
        print("{0:10}{1:10}{2:10}{3:10}{4:10}".format("Brand", "Year", "Miles", "Model", "Price(USD)"))

        for a in range(0, records):

            #lists new VW vehicles
            if condition[a] == "New" and brand[a] == "VW" and answer == "1":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            #lists new audi vehicles
            elif condition[a] == "New" and brand[a] == "Audi" and answer == "2":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            #lists new bmw vehicles
            elif condition[a] == "New" and brand[a] == "BMW" and answer == "3":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            #lists new bmw vehicles
            elif condition[a] == "New" and brand[a] == "Porsche" and answer == "4":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            elif condition[a] == "New" and brand[a] == "Skoda" and answer == "5":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            elif condition[a] == "New" and brand[a] == "Bentley" and answer == "6":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))


    #if statement if user picks 2(used vehicles)
    if answer == "2":
        
        #resets answer
        answer = 0
    
        #brand menu
        menu()

        #user input
        answer = input()
    
        #column titles
        print("{0:10}{1:10}{2:10}{3:10}{4:10}".format("Brand", "Year", "Miles", "Model", "Price(USD)"))

        for a in range(0, records):

            #lists used VW vehicles
            if condition[a] == "Used" and brand[a] == "VW" and answer == "1":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            #lists used audi vehicles
            elif condition[a] == "Used" and brand[a] == "Audi" and answer == "2":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            #lists used bmw vehicles
            elif condition[a] == "Used" and brand[a] == "BMW" and answer == "3":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            #lists used bmw vehicles
            elif condition[a] == "Used" and brand[a] == "Porsche" and answer == "4":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            #lists used skoda vehicles
            elif condition[a] == "Used" and brand[a] == "Skoda" and answer == "5":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

            #lists used bentley vehicles
            elif condition[a] == "Used" and brand[a] == "Bentley" and answer == "6":
                #prints brand year miles model and price
                print("{0:10}{1:10}{2:10}{3:10}{4:5}".format(brand[a], year[a], miles[a], model[a], price[a]))

    #asks user if they would like to continue looking for a vehicle
    print("Would you like to search for another vehicle? (Y/N)")

    #user input
    start = input()
#goodbye message
print("Thank you for using VW/Audi Group Online Dealership!")









