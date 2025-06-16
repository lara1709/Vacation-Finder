import json
import streamlit as st

st.title("Vacation Finder")
st.write("Find your perfect vacation!")
st.write("Pick your preferences:")

with open('vacationdata.json', 'r') as file:
    vacation_data = json.load(file)
    
def ask_preference():
    st.write("Let's find your perfect vacation destination!")
    st.write("Please pick your preferences:)")

    type_choice = st.radio(
        "What type of vacation are you looking for?",
        ("City", "Beach", "Mountain")
    )
    
    climate_choice = st.radio(
        "What climate are you looking for?",
        ("Warm", "Cold")
    )
    
    distance_choice = st.radio(
        "Do you prefer a near or far destination (starting from Berlin)?",
        ("Far", "Near")
    )

    if st.button("Find Destinations"):
        matching_places = []
        for place in vacation_data["Location"]:
            if (place["Type"] == type_choice and
                place["Temperature"] == climate_choice and
                place["Distance"] == distance_choice):
                matching_places.append(place)
            
        if matching_places:
            st.write("Here are your Destinations, have fun!:")
            for place in matching_places:
                st.write(f"- {place['Name']} ({place['Type']}, {place['Temperature']} climate, {place['Distance']} from Berlin)")
        else:
            st.write("Sorry, no matching destinations found:(")
                
ask_preference()

#this is a comment to test the git commit 
