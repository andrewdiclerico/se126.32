#FinalProject
#Andrew DiClerico

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for any

#VARIABLE DICTIONARY--------------
#records            -------------- keeps track of how many times ran
#loop               -------------- decision to stay in loop or exit
#selection          -------------- how many cars selected
#ifChoice           -------------- decision on second vehicle
#carSelectionOne    -------------- first car menu number selection
#carSelectOne       -------------- make and model of first car
#carSelectionTwo    -------------- second car menu number selection
#carSelectTwo       -------------- make and model of second car
#totalPrice         -------------- total price of cars and shipping
#shipSelect         -------------- shipping menu number selection
#orderNumber        -------------- order specific number

#FUNCTIONS------------------------
def carOne(carSelectionOne):

    #asks user what car they would like to choose
    print("Which car would you like (Input Corresponding Number)")

    #user inputs choice
    carSelectionOne = input()

    #returns user choice
    return carSelectionOne

def carTwo(carSelectionTwo):

    #asks user what cat they would like to choose
    print("Which car would you like (Input Corresponding Number)")

    #user inputs choice
    carSelectionTwo = input()

    #returns user choice
    return carSelectionTwo

def exit():

    #prints exit message
    print("Thank you for using the Vintage European Car Dealership!")

#BASE PROGRAM CODE----------------
records = 0
loop = ""
selection = 0
ifChoice = ""
carSelectionOne = 0
carSelectOne = ""
carSelectionTwo = 0
carSelectTwo = ""
totalPrice = 0
shipSelect = ""
orderNumber = 0

#import csv file
import csv

with open("Final.csv") as csvfile:

    file =  csv.reader(csvfile)

    #variables
    available = []
    year = []
    make = []
    model = []
    mileage = []
    condition = []
    price = []


    for rec in file:
        
        records = records + 1

        #define variables
        available.append(rec[0])
        year.append(rec[1])
        make.append(rec[2])
        model.append(rec[3])
        mileage.append(rec[4])
        condition.append(rec[5])    
        price.append(int(rec[6]))

#welcome message
print("Welcome to the Vintage European Car Dealership!")

#asks user if they would like to look for a vehicle
print("Would you like to search for a vehicle? (Y/N)")

#user's answer
loop = input()

while loop == "y" or loop == "Y" :

    #resets car selection counter
    selection = 0

    #adds one to car selection counter
    selection = selection + 1

    #notifies user of 2 car per order limit
    print("There is a two car per order limit.")

    #print menu titles
    print("{0:5}     {1:15}{2:15}{3:15}{4:15}{5:15}{6:15}{7:15}".format("Number", "Available", "Year", "Make", "Model", "Mileage", "Condition", "Price"))

    #prints first menu
    for a in range(0, records):
        print("{0:5}     {1:15}{2:15}{3:15}{4:15}{5:15}{6:15}{7:15}".format(a + 1, available[a], year[a], make[a], model[a], mileage[a], condition[a], price[a]))

    #uses function to ask user for choice and returns
    carSelectionOne = carOne(carSelectionOne)

    #if user chooses 1 lamborghini countach
    if carSelectionOne == "1":

        #tells the user they have chosen a car and price has been added to total
        print("The Lamborghini Countach is $",price[0])
        print("$",price[0], "has been added to total.")

        #stores first chosen car
        carSelectOne = (make[0], model[0])

        #add car price to total
        totalPrice = totalPrice + price[0]

        #mark car as unavailable
        available[0] = "no"

    #elif user chooses 2 lancia delta
    elif carSelectionOne == "2":

        #tells the user they have chosen a car and price has been added to total
        print("The Lancia Delta is $",price[1])
        print("$",price[1], "has been added to total")

        #stores first chosen car
        carSelectOne = (make[1], model[1])

        #add car price to total
        totalPrice = totalPrice + price[1]

        #mark car as unavailable
        available[1] = "no"

    #elif user chooses 3 porsche 911 carrera
    elif carSelectionOne == "3":

        #tells the user they have chosen a car and price has been added to total
        print("The Porsche 911 Carrera is $",price[2])
        print("$",price[2], "has been added to the total")

        #stores first chosen car
        carSelectOne = (make[2], model[2])

        #add car price to total
        totalPrice = totalPrice + price[2]
        
        #mark car as unavailable
        available[2] = "no"

    #elif user chooses 4 ford sierra
    elif carSelectionOne == "4":

        #tells the user they have chosen a car and price has been added to total
        print("The Ford Sierra is $",price[3])
        print("$",price[3], "has been added to the total")

        #stores first chosen car
        carSelectOne = (make[3], model[3])

        #add car price to total
        totalPrice = totalPrice + price[3]
        
        #mark car as unavailable
        available[3] = "no"

    #elif user chooses 5 bmw 323 alpina c1
    elif carSelectionOne == "5":

        #tells the user they have chosen a car and price has been added to total
        print("The BMW 323 Alpina C1 is $",price[4])
        print("$",price[4], "has been added to the total")

        #stores first chosen car
        carSelectOne = (make[4], model[4])

        #add car price to total
        totalPrice = totalPrice + price[4]
        
        #mark car as unavailable
        available[4] = "no"

    #elif user chooses 6 bmw m5
    elif carSelectionOne == "6":

        #tells the user they have chosen a car and price has been added to total
        print("The BMW M5 is $",price[5])
        print("$",price[5], "has been added to the total")

        #stores first chosen car
        carSelectOne = (make[5], model[5])

        #add car price to total
        totalPrice = totalPrice + price[5]
        
        #mark car as unavailable
        available[5] = "no"

    #elif user chooses 7 bmw 850i
    elif carSelectionOne == "7":

        #tells the user they have chosen a car and price has been added to total
        print("The BMW 850i is $",price[6])
        print("$",price[6], "has been added to the total")

        #stores first chosen car
        carSelectOne = (make[6], model[6])

        #add car price to total
        totalPrice = totalPrice + price[6]
        
        #mark car as unavailable
        available[6] = "no"

    #elif user chooses 8 vw golf
    elif carSelectionOne == "8":

        #tells the user they have chosen a car and price has been added to total
        print("The VW Golf is $",price[7])
        print("$",price[7], "has been added to the total")

        #stores first chosen car
        carSelectOne = (make[7], model[7])

        #add car price to total
        totalPrice = totalPrice + price[7]
        
        #mark car as unavailable
        available[7] = "no"

    #ask user if they would like to select another vehicle
    print("Would you like to select another vehicle? (Y/N)")

    #user answer
    ifChoice = input()

    if ifChoice == "Y" or ifChoice == "y":

        #add one to counter
        selection = selection + 1

        #print menu titles
        print("{0:5}     {1:15}{2:15}{3:15}{4:15}{5:15}{6:15}{7:15}".format("Number", "Available", "Year", "Make", "Model", "Mileage", "Condition", "Price"))

        #prints second menu
        for f in range(0, records):
            print("{0:5}     {1:15}{2:15}{3:15}{4:15}{5:15}{6:15}{7:15}".format(f + 1, available[f], year[f], make[f], model[f], mileage[f], condition[f], price[f]))

        #uses function to ask user choice and returns choice
        carSelectionTwo = carTwo(carSelectTwo)

        #if user chooses 1 lamborghini countach
        if carSelectionTwo == "1":

            #tells the user they have chosen a car and price has been added to total
            print("The Lamborghini Countach is $",price[0])
            print("$",price[0], "has been added to the total")

            #stores first chosen car
            carSelectTwo = (make[0], model[0])

            #add car price to total
            totalPrice = totalPrice + price[0]
        
            #mark car as unavailable
            available[0] = "no"    

        #elif user chooses 2 lancia delta
        elif carSelectionTwo == "2":

            #tells the user they have chosen a car and price has been added to total
            print("The Lancia Delta is $",price[1])
            print("$",price[1], "has been added to the total")

            #stores first chosen car
            carSelectTwo = (make[1], model[1])

            #add car price to total
            totalPrice = totalPrice + price[1]
        
            #mark car as unavailable
            available[1] = "no"    

        #elif user chooses 3 porsche 911 carrera
        elif carSelectionTwo == "3":

            #tells the user they have chosen a car and price has been added to total
            print("The Porsche 911 Carrera is $",price[2])
            print("$",price[2], "has been added to the total")

            #stores first chosen car
            carSelectTwo = (make[2], model[2])

            #add car price to total
            totalPrice = totalPrice + price[2]
        
            #mark car as unavailable
            available[2] = "no"    

        #elif user chooses 4 ford sierra
        elif carSelectionTwo == "4":

            #tells the user they have chosen a car and price has been added to total
            print("The Ford Sierra is $",price[3])
            print("$",price[3], "has been added to the total")

            #stores first chosen car
            carSelectTwo = (make[3], model[3])

            #add car price to total
            totalPrice = totalPrice + price[3]
        
            #mark car as unavailable
            available[3] = "no"    

        #elif user chooses 5 bmw 323 alpina c1
        elif carSelectionTwo == "5":

            #tells the user they have chosen a car and price has been added to total
            print("The BMW 323 Alpina C1 is $",price[4])
            print("$",price[4], "has been added to the total")

            #stores first chosen car
            carSelectTwo = (make[4], model[4])

            #add car price to total
            totalPrice = totalPrice + price[4]
        
            #mark car as unavailable
            available[4] = "no"    

        #elif user chooses 6 bmw m5
        elif carSelectionTwo == "6":

            #tells the user they have chosen a car and price has been added to total
            print("The BMW M5 is $",price[5])
            print("$",price[5], "has been added to the total")

            #stores first chosen car
            carSelectTwo = (make[5], model[5])

            #add car price to total
            totalPrice = totalPrice + price[5]
        
            #mark car as unavailable
            available[5] = "no"    

        #elif user chooses 7 bmw 850i
        elif carSelectionTwo == "7":

            #tells the user they have chosen a car and price has been added to total
            print("The BMW 850i is $",price[6])
            print("$",price[6], "has been added to the total")

            #stores first chosen car
            carSelectTwo = (make[6], model[6])

            #add car price to total
            totalPrice = totalPrice + price[6]
        
            #mark car as unavailable
            available[6] = "no"    

        #elif user chooses 8 vw golf
        elif carSelectionTwo == "8":

            #tells the user they have chosen a car and price has been added to total
            print("The VW Golf is $",price[7])
            print("$",price[7], "has been added to the total")

            #stores first chosen car
            carSelectTwo = (make[7], model[7])

            #add car price to total
            totalPrice = totalPrice + price[7]
        
            #mark car as unavailable
            available[7] = "no"    

    #prints first vehicle choice
    print("Vehicle One: ")
    print(carSelectOne)

    #prints second vehicle choice if there is one
    print("Vehicle Two:          (If selected)")
    print(carSelectTwo)

    #shipping type
    sType = ["Flatbed (1)", "Double Flatbed (2)", "Enclosed Trailor (2)", "Pick-Up"]

    #shipping eta
    sEta = ["24h", "24h", "24h", "0h"]

    #shipping price
    sPrice = [2000, 4000, 8000, 0]

    

    #if user selected one vehicle
    if selection == 1:
        
        #print shipping options and column titles
        print("Shipping options for one car: ")
        print("{0:5}     {1:25}{2:15}{3:15}".format("Number", "Type", "ETA", "Price"))

        #print all shipping options
        for j in range(0, 4):
            print("{0:5}     {1:25}{2:15}{3:15}".format(j + 1, sType[j], sEta[j], sPrice[j]))

        print("Which shipping option would you like? (Input Corresponding Number)")

        #shipping selection
        shipSelect = input()

        #if statement for shipping one | flatbed 1
        if shipSelect == "1":

            #print selection and price
            print("You chose ", sType[0])
            print(sType[0], "is $",sPrice[0])

            #add price to total
            totalPrice = totalPrice + sPrice[0]

        #elif statement for shipping two | flatbed 2
        elif shipSelect == "2":

            #print selection and price
            print("You chose ", sType[1])
            print(sType[1], "is $",sPrice[1])

            #add price to total
            totalPrice = totalPrice + sPrice[1]

        #elif statement for shipping three | enclosed trailor
        elif shipSelect == "3":

            #print selection and price
            print("You chose ", sType[2])
            print(sType[2], "is $",sPrice[2])

            #add price to total
            totalPrice = totalPrice + sPrice[2]

        #elif statement for shipping four | pickup
        elif shipSelect == "4":

            #print selection and price
            print("You chose ", sType[3])
            print(sType[3], "is $",sPrice[3])

            #add price to total
            totalPrice = totalPrice + sPrice[3]


    #elif user selected two vehicles
    elif selection == 2:

        #print shipping options and column titles
        print("Shipping options for two cars: ")
        print("{0:5}     {1:20}{2:15}{3:15}".format("Number", "Type", "ETA", "Price"))

        #first option not available
        sType[0] = "none"
        sEta[0] = "none"
        sPrice[0] = "none"

        #print all shipping options
        for s in range(0, 4):
            print("{0:5}     {1:20}{2:15}{3:15}".format(s + 1, sType[s], sEta[s], sPrice[s]))

        #users shipping selection
        shipSelect = input()

             #if statement for shipping one | flatbed 1
        if shipSelect == "1":
            print("Not Available")

        #elif statement for shipping two | flatbed 2
        elif shipSelect == "2":

            #print selection and price
            print("You chose ", sType[1])
            print(sType[1], "is $",sPrice[1])

            #add price to total
            totalPrice = totalPrice + sPrice[1]

        #elif statement for shipping three | enclosed trailor
        elif shipSelect == "3":

            #print selection and price
            print("You chose ", sType[2])
            print(sType[2], "is $",sPrice[2])

            #add price to total
            totalPrice = totalPrice + sPrice[2]

        #elif statement for shipping four | pickup
        elif shipSelect == "4":   

            #print selection and price
            print("You chose ", sType[3])
            print(sType[3], "is $",sPrice[3])

            #add price to total
            totalPrice = totalPrice + sPrice[3]

    #calculate order number
    orderNumber = totalPrice * 30

    #print order number
    print("Your order number is: ",orderNumber)

    #print total price
    print("Your total is $",totalPrice)

    #asks user if they would like to make another order
    print("Would you like to make another order? (Y/N)")

    #user answer
    loop = input()

#display exit message
exit()
