parking_lots = ["Lot A", "Lot B", "Lot C", "Lot D"]
a, b, c, d = parking_lots

lot = input("Enter your parking lot A, B, C, or D: ")
zone = input("Enter your zone as a number: ")

lot_Zone = lot + zone
print("Your zone lot is: " + lot_Zone)

import random
parked_cars = random.sample(range(0, 500), 1) #This gives a simulated a number of parked cars
parked_cars2 = random.sample(range(0, 500), 1)

if parked_cars < parked_cars2:
    print ("The number of parked cars currently is:", parked_cars, "for lot:", lot, "and is the lot with the lowest amount of cars parked at the moment.")
elif parked_cars > parked_cars2:
    print ("The number of parked cars in a different lot are", parked_cars2, "compared to", parked_cars, "Would you like to go to that lot?")
    new_route = input("Type Y for yes and N for no: ")
    if new_route == 'Y' or new_route == 'y':
        print ("Your new route is the one with shortest numbers of cars parked!")
    elif new_route == 'n' or new_route == 'N':
        print ("Your route will continue on to the same parking lot.")
    else:
        print ("Wrong input")