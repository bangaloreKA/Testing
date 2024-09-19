import streamlit as st
import requests
from datetime import datetime
import json
import os
from vedastro import GeoLocation, Time, Calculate, ZodiacName, Tools, PlanetName, HouseName

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

# Initialize session state for calculations
if 'lunar_day_info' not in st.session_state:
    st.session_state['lunar_day_info'] = None
if 'lord_of_house' not in st.session_state:
    st.session_state['lord_of_house'] = None

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
    table {
        width: 100%;
        border-collapse: collapse;
    }
    table, th, td {
        border: 1px solid #ddd;
        padding: 8px;
    }
    th {
        background-color: #4CAF50;
        color: white;
        text-align: center;
    }
    td {
        text-align: center;
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

# User login/registration
st.write("## Login or Register")
name = st.text_input("Name", user["name"])
gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(user["gender"]))
min_date = datetime(1950, 1, 1)
max_date = datetime(2030, 12, 31)
DateofBirth = st.date_input("Date of Birth", value=datetime.strptime(user["DateofBirth"], "%d/%m/%Y"), min_value=min_date, max_value=max_date)
DateofBirth_str = DateofBirth.strftime("%d/%m/%Y")

# Time of Birth input after Date of Birth
default_time_str = user.get("TimeofBirth", "23:40") if user.get("TimeofBirth") else "23:40"
TimeofBirth = st.time_input("Time of Birth", value=datetime.strptime(default_time_str, "%H:%M").time())
user["TimeofBirth"] = TimeofBirth.strftime('%H:%M')

# Update user data
user["name"] = name
user["gender"] = gender
user["DateofBirth"] = DateofBirth_str

# Place input with suggestions
place = st.text_input("Place", user["place"])
if place:
    data = get_place_suggestions(place)
    suggestions = [result['formatted'] for result in data['results']]
    selected_place = st.selectbox("Select a place:", suggestions, index=suggestions.index(user["place"]) if user["place"] in suggestions else 0)

    if selected_place:
        # Find the selected place data
        selected_place_data = next(item for item in data['results'] if item['formatted'] == selected_place)
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

# Save the updated user data
if selected_user_key is None:
    user_key = f"{name}_{DateofBirth_str}"
    user_data[user_key] = user
else:
    user_data[selected_user_key] = user

save_user_data(user_data)

if not all([name, gender, place, longitude, latitude, gmt, user["TimeofBirth"], user["DateofBirth"]]):
    st.error("Please fill in all the fields to proceed.")
else:
    if st.button("Calculate Geolocation and Birth Time"):
        try:
            TOBDOBGMT = f"{user['TimeofBirth']} {user['DateofBirth']} {user['gmt']}"
            geolocation = GeoLocation(selected_place, longitude, latitude)
            birth_time = Time(TOBDOBGMT, geolocation)

            # Calculate zodiac data for all zodiac signs
            zodiac_signs = {
                'Aries': ZodiacName.Aries,
                'Taurus': ZodiacName.Taurus,
                'Gemini': ZodiacName.Gemini,
                'Cancer': ZodiacName.Cancer,
                'Leo': ZodiacName.Leo,
                'Virgo': ZodiacName.Virgo,
                'Libra': ZodiacName.Libra,
                'Scorpio': ZodiacName.Scorpio,
                'Sagittarius': ZodiacName.Sagittarius,
                'Capricorn': ZodiacName.Capricorn,
                'Aquarius': ZodiacName.Aquarius,
                'Pisces': ZodiacName.Pisces
            }

            planets_in_sign = {}
            house_from_sign = {}

            for zodiac_name, zodiac in zodiac_signs.items():
                planets_in_sign[zodiac_name] = Calculate.PlanetsInSign(zodiac, birth_time)
                house_from_sign[zodiac_name] = Calculate.HouseFromSignName(zodiac, birth_time)

            # Convert the results to a readable format
            readable_planets_in_sign = {zodiac: [str(planet) for planet in planets] if planets else ["No planets found"]
                                        for zodiac, planets in planets_in_sign.items()}

            readable_house_from_sign = {zodiac: str(house) if house else "House name not found"
                                        for zodiac, house in house_from_sign.items()}

            # Display calculated data in a table
            st.write("### Calculated Zodiac Data")

            table_html = "<table><tr><th>Zodiac Sign</th><th>Planets in Sign</th><th>House from Sign Name</th></tr>"
            for zodiac_name in zodiac_signs.keys():
                table_html += f"<tr><td>{zodiac_name}</td><td>{', '.join(readable_planets_in_sign[zodiac_name])}</td><td>{readable_house_from_sign[zodiac_name]}</td></tr>"
            table_html += "</table>"

            st.write(table_html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")
