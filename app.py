import json
 
with open('vacationdata.json', 'r') as file:
    vacation_data = json.load(file)

def ask_preference():
    print("Let's find your perfect vacation destination!")
    print("Please pick your preferences:)")

    print("\nWhat type of vacation are you looking for?")
    print("1. City")
    print("2. Beach")
    print("3. Mountain")
    type_choice = input("Enter 1, 2, or 3: ")

    print("\nWhat climate are you looking for?")
    print("1. Warm")
    print("2.Cold")
    climate_choice = input("Enter 1 or 2: ")

    print("\nDo you prefer a near or far destination(starting from Berlin)?")
    print("1. Far")
    print("2. Near")
    distance_choice = input("Enter 1 or 2: ")
    
    print("\nThank you:)")
    
    type_map = {"1": "City", "2": "Beach", "3": "Mountain"}
    climate_map = {"1": "Warm", "2": "Cold"}
    distance_map = {"1": "Far", "2": "Near"}
    
    chosen_type = type_map.get(type_choice)
    chosen_climate = climate_map.get(climate_choice)
    chosen_distance = distance_map.get(distance_choice)
    
    matching_places = []
    for place in vacation_data["Location"]:
        if (place["Type"] == chosen_type and
         place["Temperature"] == chosen_climate and
         place["Distance"] == chosen_distance):
            matching_places.append(place["Name"])
            
    if matching_places:
        print("\nHere are your Destnations, have fun!:")
        for name in matching_places:
            print(f"-{name}")
    else:
        print("\nSorry, no matching destinations found:(")
        
        
ask_preference()
