import json
import streamlit as st

st.title("Vacation Finder")

with open('vacationdata.json', 'r') as file:
    vacation_data = json.load(file)
    
def filter_destinations(data, types, climates, distances):
    matching_places =[]
    if "Location" in data and isinstance(data["Location"], list):
        for place in data["Location"]:
            place_type = place.get("Type")
            place_temp = place.get("Temperature")
            place_dist = place.get("Distance")
            
            type_match = True if not types else (place_type in types)
            climate_match = True if not climates else (place_temp in climates)
            distance_match = True if not distances else (place_dist in distances)
            
            if type_match and climate_match and distance_match:
                matching_places.append(place)
    
    return matching_places

def ask_preference():
    st.write("Let's find your perfect vacation destination!")
    st.write("Please pick your preferences:)")

    type_choices = st.multiselect(
        "What type of vacation are you looking for?",
        ["City", "Beach", "Mountain"]
    )
    
    climate_choices = st.multiselect(
        "What climate are you looking for?",
        ["Warm", "Cold"]
    )
    
    distance_choices = st.multiselect(
        "Do you prefer a near or far destination (starting from Berlin)?",
        ["Far", "Near"]
    )

    if st.button("Find Destinations"):
        matching_places = filter_destinations(
            vacation_data,
            type_choices,
            climate_choices,
            distance_choices
        )    
            
        if matching_places:
            st.write("Here are your Destinations, have fun!:")
            for place in matching_places:
                country = place.get("Country", "Unknown Country")
                st.write(f"**{place['Name']}, {country}** - a {place['Temperature'].lower()}  {place['Type'].lower()} destination ({place['Distance'].lower()} from Berlin).")
                if "Description" in place:
                    st.write(place["Description"])
        else:
            st.write("Sorry, no matching destinations found:(")
                
ask_preference()