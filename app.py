import json
 
with open('vacationdata.json', 'r') as file:
    vacation_data = json.load(file)

def ask_preference():
    print("Let's find your perfect vacation destination!")
    print("Please pick your preferences:)")

    print("What type of vacation are you looking for?")
    print("1. City")
    print("2. Beach")
    print("3. Mountain")
    type_choice = input("Enter 1, 2, or 3: ")

    print("What climate are you lokking for?")
    print("1. Warm")
    print("2.Cold")
    climate_choice = input("Enter 1 or 2: ")

    print("Do you prefer a near or far destination(starting from Berlin)?")
    print("1. Far")
    print("2. Near")
    distance_choice = input("Enter 1 or 2: ")

    
