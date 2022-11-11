print("Hello, World!")

parking_lots = ["Lot A", "Lot B", "Lot C", "Lot D"]
a, b, c, d = parking_lots

print (a, b, c, d)

def fruitFunc():
    x = "fantastic"
    print ("Python is " + x)

fruitFunc()



lot = input("Enter your lot a, b, c, or d: ")
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
