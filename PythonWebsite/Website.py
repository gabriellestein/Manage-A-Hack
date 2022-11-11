parking_lots = ["Lot A", "Lot B", "Lot C", "Lot D"]
a, b, c, d = parking_lots

lot = input("Enter your parking lot A, B, C, or D: ")
zone = input("Enter your zone as a number: ")

lot_Zone = lot + zone
print("Your zone lot is: " + lot_Zone)

if lot == 'a' or lot == 'A':
    lot = 1
elif lot == 'b' or lot == 'B':
    lot = 2
elif lot == 'c' or lot == 'C':
    lot = 3
elif lot == 'd' or lot == 'D':
    lot = 4

import random
parked_cars = random.sample(range(0, 500), 1)

print ("The number of parked cars currently is:", parked_cars)

