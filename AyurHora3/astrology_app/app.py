# Version 1.1
# -------------------------------------------
# ---------------------------------------------

#
# import streamlit as st
# import requests
# from datetime import datetime
# import json
# import os
# from vedastro import GeoLocation, Time, HouseName
# from astro_calculations import calculate_lunar_day, calculate_lord_of_house  # Import functions
#
# # Function to get place suggestions and geolocation data
# def get_place_suggestions(query):
#     api_key = "bd404b3ded074574b8eb61888b718c62"
#     url = f"https://api.opencagedata.com/geocode/v1/json?q={query}&key={api_key}&limit=5"
#     response = requests.get(url)
#     return response.json()
#
# # Load user data from a JSON file
# def load_user_data(file_path='user_data.json'):
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as f:
#             return json.load(f)
#     return {}
#
# # Save user data to a JSON file
# def save_user_data(data, file_path='user_data.json'):
#     with open(file_path, 'w') as f:
#         json.dump(data, f, indent=4)
#
# # Clear user data from the JSON file
# def clear_user_data(file_path='user_data.json'):
#     if os.path.exists(file_path):
#         os.remove(file_path)
#
# # Initialize session state for calculations
# if 'lunar_day_info' not in st.session_state:
#     st.session_state['lunar_day_info'] = None
# if 'lord_of_house' not in st.session_state:
#     st.session_state['lord_of_house'] = None
#
# # Streamlit title and description
# st.title("Astrological Calculations")
# st.markdown("""
# <style>
#     .big-font {
#         font-size:30px !important;
#         color: #4CAF50;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#     }
# </style>
# """, unsafe_allow_html=True)
# st.write('<p class="big-font">Create Your Astrological Profile</p>', unsafe_allow_html=True)
#
# # Load existing user data
# user_data = load_user_data()
#
# # Columns for user selection and history management
# col1, col2, col3 = st.columns([2, 1, 1])
#
# with col1:
#     # Dropdown to select a user
#     user_options = ["New User"] + [f"{user_data[key]['name']} ({key.split('_')[1]})" for key in user_data.keys()]
#     selected_user = st.selectbox("Select User", user_options)
#
# if selected_user != "New User":
#     selected_user_key = [key for key in user_data.keys() if f"{user_data[key]['name']} ({key.split('_')[1]})" == selected_user][0]
#     user = user_data[selected_user_key]
# else:
#     selected_user_key = None
#     user = {
#         "name": "",
#         "gender": "Male",
#         "place": "Tokyo",
#         "longitude": "",
#         "latitude": "",
#         "gmt": "",
#         "TimeofBirth": "23:40",
#         "DateofBirth": "31/03/2011"
#     }
#
# with col2:
#     if st.button("Clear All History"):
#         clear_user_data()
#         st.success("All history has been cleared.")
#         st.experimental_rerun()
#
# with col3:
#     if selected_user != "New User" and st.button("Delete This Profile"):
#         if selected_user_key in user_data:
#             del user_data[selected_user_key]
#             save_user_data(user_data)
#             st.success(f"Profile for {selected_user} has been deleted.")
#             st.experimental_rerun()
#
# # User login/registration
# st.write("## Login or Register")
# name = st.text_input("Name", user["name"])
# gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(user["gender"]))
# min_date = datetime(1950, 1, 1)
# max_date = datetime(2030, 12, 31)
# DateofBirth = st.date_input("Date of Birth", value=datetime.strptime(user["DateofBirth"], "%d/%m/%Y"), min_value=min_date, max_value=max_date)
# DateofBirth_str = DateofBirth.strftime("%d/%m/%Y")
#
# # Time of Birth input after Date of Birth
# default_time_str = user.get("TimeofBirth", "23:40") if user.get("TimeofBirth") else "23:40"
# TimeofBirth = st.time_input("Time of Birth", value=datetime.strptime(default_time_str, "%H:%M").time())
# user["TimeofBirth"] = TimeofBirth.strftime('%H:%M')
#
# # Update user data
# user["name"] = name
# user["gender"] = gender
# user["DateofBirth"] = DateofBirth_str
#
# # Place input with suggestions
# place = st.text_input("Place", user["place"])
# if place:
#     data = get_place_suggestions(place)
#     suggestions = [result['formatted'] for result in data['results']]
#     selected_place = st.selectbox("Select a place:", suggestions, index=suggestions.index(user["place"]) if user["place"] in suggestions else 0)
#
#     if selected_place:
#         # Find the selected place data
#         selected_place_data = next(item for item in data['results'] if item['formatted'] == selected_place)
#         longitude = selected_place_data['geometry']['lng']
#         latitude = selected_place_data['geometry']['lat']
#         gmt = selected_place_data['annotations']['timezone']['offset_string']
#
#         # Update user data
#         user["place"] = selected_place
#         user["longitude"] = longitude
#         user["latitude"] = latitude
#         user["gmt"] = gmt
#
#         # Display selected place details
#         st.write(f"Selected Place: {selected_place}")
#         st.write(f"Longitude: {longitude}")
#         st.write(f"Latitude: {latitude}")
#         st.write(f"GMT: {gmt}")
#
#         # Convert input data to the required format
#         TOBDOBGMT = f"{user['TimeofBirth']} {user['DateofBirth']} {user['gmt']}"
#
#         # Save the updated user data
#         if selected_user_key is None:
#             user_key = f"{name}_{DateofBirth_str}"
#             user_data[user_key] = user
#         else:
#             user_data[selected_user_key] = user
#
#         save_user_data(user_data)
#
#         if not all([name, gender, place, longitude, latitude, gmt, user["TimeofBirth"], user["DateofBirth"]]):
#             st.error("Please fill in all the fields to proceed.")
#
#         else:
#             try:
#                 geolocation = GeoLocation(selected_place, longitude, latitude)
#                 birth_time = Time(TOBDOBGMT, geolocation)
#
#                 # Columns for displaying results below respective buttons
#                 col4, col5 = st.columns(2)
#
#                 with col4:
#                     if st.button("Calculate Lunar Day"):
#                         lunar_day_info = calculate_lunar_day(birth_time)
#                         st.session_state['lunar_day_info'] = lunar_day_info
#
#                     # Display the results below the button
#                     if st.session_state['lunar_day_info']:
#                         with st.expander("Lunar Day Calculation Result"):
#                             st.json(st.session_state['lunar_day_info'])
#
#                 with col5:
#                     if st.button("Calculate Lord of the 4th House"):
#                         lord_of_house = calculate_lord_of_house(birth_time, HouseName.House4)
#                         st.session_state['lord_of_house'] = lord_of_house
#
#                     # Display the results below the button
#                     if st.session_state['lord_of_house']:
#                         with st.expander("Lord of the 4th House"):
#                             st.write(st.session_state['lord_of_house'])
#
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")
#                 st.write("Debug Information:")
#                 st.write(f"TOBDOBGMT: {TOBDOBGMT}")
#                 st.write(f"GeoLocation: {geolocation}")
#                 st.write(f"Birth Time: {birth_time}")



# Version 1.2
# -------------------------------------------
# ---------------------------------------------

import streamlit as st
import requests
from vedastro import *
from datetime import datetime
import json
import os
from astro_calculations import *

# Function to get place suggestions and geolocation data
def get_place_suggestions(query):
    api_key = "bd404b3ded074574b8eb61888b718c62"
    url = f"https://api.opencagedata.com/geocode/v1/json?q={query}&key={api_key}&limit=5"
    response = requests.get(url)
    return response.json()

# Load user data from a JSON file
def load_user_data(file_path='user_data.json'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

# Save user data to a JSON file
def save_user_data(data, file_path='user_data.json'):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Clear user data from the JSON file
def clear_user_data(file_path='user_data.json'):
    if os.path.exists(file_path):
        os.remove(file_path)

# Streamlit title and description
st.title("Astrological Calculations")
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
        color: #4CAF50;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
</style>
""", unsafe_allow_html=True)
st.write('<p class="big-font">Create Your Astrological Profile</p>', unsafe_allow_html=True)

# Load existing user data
user_data = load_user_data()

# Columns for user selection and history management
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    # Dropdown to select a user
    user_options = ["New User"] + [f"{user_data[key]['name']} ({key.split('_')[1]})" for key in user_data.keys()]
    selected_user = st.selectbox("Select User", user_options)

if selected_user != "New User":
    selected_user_key = [key for key in user_data.keys() if f"{user_data[key]['name']} ({key.split('_')[1]})" == selected_user][0]
    user = user_data[selected_user_key]
else:
    selected_user_key = None
    user = {
        "name": "",
        "gender": "Male",
        "place": "Tokyo",
        "longitude": "",
        "latitude": "",
        "gmt": "",
        "TimeofBirth": "23:40",
        "DateofBirth": "31/03/2011"
    }

with col2:
    if st.button("Clear All History"):
        clear_user_data()
        st.success("All history has been cleared.")
        st.experimental_rerun()

with col3:
    if selected_user != "New User" and st.button("Delete This Profile"):
        if selected_user_key in user_data:
            del user_data[selected_user_key]
            save_user_data(user_data)
            st.success(f"Profile for {selected_user} has been deleted.")
            st.experimental_rerun()

# Input fields for new user or selected user
name = st.text_input("Name", user["name"])
gender = st.radio("Gender", ["Male", "Female"], index=["Male", "Female"].index(user["gender"]))
place = st.text_input("Place of Birth", user["place"])

# Get place suggestions
if place:
    suggestions = get_place_suggestions(place)
    if suggestions and 'results' in suggestions:
        place_options = [result['formatted'] for result in suggestions['results']]
        selected_place = st.selectbox("Select Place", place_options)
    else:
        st.warning("No suggestions found. Please check the place name.")

    # Process the selected place to get longitude, latitude, and GMT
    if selected_place:
        selected_place_data = next(result for result in suggestions['results'] if result['formatted'] == selected_place)
        longitude = selected_place_data['geometry']['lng']
        latitude = selected_place_data['geometry']['lat']
        gmt = selected_place_data['annotations']['timezone']['offset_string']

        # Update user data
        user["place"] = selected_place
        user["longitude"] = longitude
        user["latitude"] = latitude
        user["gmt"] = gmt

        # Display selected place details
        st.write(f"Selected Place: {selected_place}")
        st.write(f"Longitude: {longitude}")
        st.write(f"Latitude: {latitude}")
        st.write(f"GMT: {gmt}")

        # Convert input data to the required format
        TOBDOBGMT = f"{user['TimeofBirth']} {user['DateofBirth']} {user['gmt']}"

        # Save the updated user data
        if selected_user_key is None:
            DateofBirth_str = user["DateofBirth"]
            user_key = f"{name}_{DateofBirth_str}"
            user_data[user_key] = user
        else:
            DateofBirth_str = user["DateofBirth"]
            user_data[selected_user_key] = user

        save_user_data(user_data)

        if not all([name, gender, place, longitude, latitude, gmt, user["TimeofBirth"], user["DateofBirth"]]):
            st.error("Please fill in all the fields to proceed.")
        else:
            try:
                geolocation = GeoLocation(selected_place, longitude, latitude)
                birth_time = Time(TOBDOBGMT, geolocation)

                # Create dropdowns for each calculation result
                with st.expander("Lunar Day Calculation"):
                    if st.button("Calculate Lunar Day"):
                        st.session_state.lunar_day_info = calculate_lunar_day(birth_time)
                    if "lunar_day_info" in st.session_state and st.session_state.lunar_day_info:
                        st.json(st.session_state.lunar_day_info)

                with st.expander("Lord of the 4th House"):
                    if st.button("Calculate Lord of the 4th House"):
                        st.session_state.lord_of_house = calculate_lord_of_house(birth_time, HouseName.House4)
                    if "lord_of_house" in st.session_state and st.session_state.lord_of_house:
                        st.write(st.session_state.lord_of_house)

                with st.expander("Sun Malefic to Lagna"):
                    if st.button("Check if Sun is Malefic"):
                        st.session_state.is_sun_malefic = is_sun_malefic_to_lagna(birth_time)
                    if "is_sun_malefic" in st.session_state and st.session_state.is_sun_malefic:
                        st.write(st.session_state.is_sun_malefic)

                with st.expander("Yogakaraka to Lagna"):
                    if st.button("Check if Any Planet is Yogakaraka"):
                        st.session_state.is_yogakaraka = is_yogakaraka_to_lagna(birth_time)
                    if "is_yogakaraka" in st.session_state and st.session_state.is_yogakaraka:
                        st.write(st.session_state.is_yogakaraka)

                with st.expander("Speed of Sun"):
                    if st.button("Get Speed of Sun"):
                        st.session_state.sun_speed = get_sun_speed(birth_time)
                    if "sun_speed" in st.session_state and st.session_state.sun_speed:
                        st.write(st.session_state.sun_speed)

                with st.expander("Lord of Hora"):
                    if st.button("Get Lord of Hora"):
                        st.session_state.lord_of_hora = get_lord_of_hora(birth_time)
                    if "lord_of_hora" in st.session_state and st.session_state.lord_of_hora:
                        st.write(st.session_state.lord_of_hora)

                with st.expander("House 1 and 10 Longitudes"):
                    if st.button("Get Longitudes of House 1 and 10"):
                        st.session_state.house1_10_longitudes = get_house1_10_longitudes(birth_time)
                    if "house1_10_longitudes" in st.session_state and st.session_state.house1_10_longitudes:
                        st.write(st.session_state.house1_10_longitudes)

                with st.expander("LMT to UTC"):
                    if st.button("Convert LMT to UTC"):
                        st.session_state.utc_time = lmt_to_utc(birth_time)
                    if "utc_time" in st.session_state and st.session_state.utc_time:
                        st.write(st.session_state.utc_time)

                with st.expander("Gochara Obstructed"):
                    if st.button("Check if Gochara is Obstructed"):
                        st.session_state.gochara_obstructed = is_gochara_obstructed(birth_time)
                    if "gochara_obstructed" in st.session_state and st.session_state.gochara_obstructed:
                        st.write(st.session_state.gochara_obstructed)

                with st.expander("Mercury Malefic"):
                    if st.button("Check if Mercury is Malefic"):
                        st.session_state.is_mercury_malefic = is_mercury_malefic(birth_time)
                    if "is_mercury_malefic" in st.session_state and st.session_state.is_mercury_malefic:
                        st.write(st.session_state.is_mercury_malefic)

                with st.expander("Moon Benefic"):
                    if st.button("Check if Moon is Benefic"):
                        st.session_state.is_moon_benefic = is_moon_benefic(birth_time)
                    if "is_moon_benefic" in st.session_state and st.session_state.is_moon_benefic:
                        st.write(st.session_state.is_moon_benefic)

                with st.expander("Benefic Planets"):
                    if st.button("Get List of Benefic Planets"):
                        st.session_state.benefic_planets = benefic_planet_list(birth_time)
                    if "benefic_planets" in st.session_state and st.session_state.benefic_planets:
                        st.write(st.session_state.benefic_planets)

                with st.expander("Malefic Planets"):
                    if st.button("Get List of Malefic Planets"):
                        st.session_state.malefic_planets = malefic_planet_list(birth_time)
                    if "malefic_planets" in st.session_state and st.session_state.malefic_planets:
                        st.write(st.session_state.malefic_planets)

                with st.expander("Planets Aspecting House 1"):
                    if st.button("Get Planets Aspecting House 1"):
                        st.session_state.planets_aspecting_house1 = planets_aspecting_house(birth_time, HouseName.House1)
                    if "planets_aspecting_house1" in st.session_state and st.session_state.planets_aspecting_house1:
                        st.write(st.session_state.planets_aspecting_house1)

                with st.expander("Planets Ordered by Strength"):
                    if st.button("Get Planets Ordered by Strength"):
                        st.session_state.planets_ordered_by_strength = planets_ordered_by_strength(birth_time)
                    if "planets_ordered_by_strength" in st.session_state and st.session_state.planets_ordered_by_strength:
                        st.write(st.session_state.planets_ordered_by_strength)

                with st.expander("All Planet Strength"):
                    if st.button("Get All Planet Strength"):
                        st.session_state.all_planet_strength = all_planet_strength(birth_time)
                    if "all_planet_strength" in st.session_state and st.session_state.all_planet_strength:
                        st.write(st.session_state.all_planet_strength)

                with st.expander("Houses Ordered by Strength"):
                    if st.button("Get Houses Ordered by Strength"):
                        st.session_state.houses_ordered_by_strength = houses_ordered_by_strength(birth_time)
                    if "houses_ordered_by_strength" in st.session_state and st.session_state.houses_ordered_by_strength:
                        st.write(st.session_state.houses_ordered_by_strength)

                with st.expander("Sun Shadbala Pinda"):
                    if st.button("Get Sun Shadbala Pinda"):
                        st.session_state.sun_shadbala_pinda = sun_shadbala_pinda(birth_time)
                    if "sun_shadbala_pinda" in st.session_state and st.session_state.sun_shadbala_pinda:
                        st.write(st.session_state.sun_shadbala_pinda)

                with st.expander("Sun Drik Bala"):
                    if st.button("Get Sun Drik Bala"):
                        st.session_state.sun_drik_bala = sun_drik_bala(birth_time)
                    if "sun_drik_bala" in st.session_state and st.session_state.sun_drik_bala:
                        st.write(st.session_state.sun_drik_bala)

                with st.expander("Sun Chesta Bala"):
                    if st.button("Get Sun Chesta Bala"):
                        st.session_state.sun_chesta_bala = sun_chesta_bala(birth_time)
                    if "sun_chesta_bala" in st.session_state and st.session_state.sun_chesta_bala:
                        st.write(st.session_state.sun_chesta_bala)

                with st.expander("Epoch Interval"):
                    if st.button("Get Epoch Interval"):
                        st.session_state.epoch_interval = epoch_interval(birth_time)
                    if "epoch_interval" in st.session_state and st.session_state.epoch_interval:
                        st.write(st.session_state.epoch_interval)

                with st.expander("Sun Motion Name"):
                    if st.button("Get Sun Motion Name"):
                        st.session_state.sun_motion_name = sun_motion_name(birth_time)
                    if "sun_motion_name" in st.session_state and st.session_state.sun_motion_name:
                        st.write(st.session_state.sun_motion_name)

                with st.expander("Sun Saptavargaja Bala"):
                    if st.button("Get Sun Saptavargaja Bala"):
                        st.session_state.sun_saptavargaja_bala = sun_saptavargaja_bala(birth_time)
                    if "sun_saptavargaja_bala" in st.session_state and st.session_state.sun_saptavargaja_bala:
                        st.write(st.session_state.sun_saptavargaja_bala)

            except Exception as e:
                st.error(f"An error occurred: {e}")
