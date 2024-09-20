# Version 5.1  this gives the table and the kundali along with prediction of planet and House && Planet
# and Zodiac
# --------------------------------------------------------------------
# ---------------------------------------------------------------------
#


import streamlit as st
import requests
from datetime import datetime
import json
import os
from vedastro import GeoLocation, Time, Calculate, ZodiacName, Tools, PlanetName, HouseName

# Matching table
# matching_table = [
#     {"house": "House8", "planets": ["Ketu"], "disease": "Atisara", "remedy": "Indu shukra prityartha japa homa."},
#     {"house": "House5", "planets": ["Sun", "Mars"], "disease": "Atisara", "remedy": "Indu shukra prityartha japa homa."},
#     {"house": "House4", "planets": ["Moon", "Venus"], "disease": "Adhika shatru, more Chapalatva, Mandakayagni, Udararoga", "remedy": "chandrasana"}
# ]

matching_table = [
    {"house": "House8", "planets": ["Moon", "Venus"], "disease": "Atisara", "remedy": "Indu shukra "
                                                                                      "prityartha japa "
                                                                                      "homa.",
     "comment": "Moon, Benus in House 8"},
    {"house": "House8", "planets": ["Mars", "Venus"], "disease": "Atisara", "remedy": "Indu shukra "
                                                                                      "prityartha japa "
                                                                                      "homa.",
     "comment": "Mars, Venus in House 8"},
    {"house": "House8", "planets": ["Rahu", "Mercury"], "disease": "Atisara", "remedy": "Indu shukra "
                                                                                        "prityartha "
                                                                                        "japa homa.",
     "comment": "Rahu, Mercury in House 8"},
    {"house": "House7", "planets": ["Saturn", "Mars"], "disease": "Atisara", "remedy": "Indu shukra "
                                                                                       "prityartha japa homa.", "comment": "Saturn, Mars in House 7"},
    {"house": "House7", "planets": ["Moon"], "disease": "Adhika shatru, more Chapalatva, Mandakayagni, "
                                                        "Udararoga", "remedy": "chandopasana",
     "comment": "Moon in House 7"},
    {"house": "House8", "planets": ["Moon"], "disease": "Krumi roga, swalpa aayu", "remedy": "Karma to "
                                                                                             "do "
                                                                                             "Chandra "
                                                                                             "priti",
     "comment": "Moon in House 8"},
    {"house": "House6", "planets": ["Moon"], "disease": "Krumi", "remedy": "Karma to do Chandra priti",
     "comment": "Moon in House 6"},
    {"house": "House8", "planets": ["Saturn"], "disease": "Pandu, kshaya, different dukhas", "remedy":
        "Consult the Vaidya", "comment": "Saturn in House 8"},
    {"house": "House3", "planets": ["Jupiter"], "disease": "Agnimandya/ sahodara viyoga/ striviyuta",
     "remedy": "Bhuhaspati mantra japa\n- Pitavastra daana\n- Homa from ashvattha samit\n- Pushparaga "
               "mukti dharanadadhyodana naivedya\n \n", "comment": "Jupiter in House 3"},
    {"house": "House6", "planets": ["Jupiter"], "disease": "Agnimandya/ shandatva/ durbala, alasa, "
                                                           "striviyuta, shatru", "remedy": "Bhuhaspati mantra japa\n- Pitavastra daana\n- Homa from ashvattha samit\n- Pushparaga mukti dharanadadhyodana naivedya", "comment": "Jupiter in House 6"}
]

zodiac_table = [
    {"zodiac_sign": "Libra", "planets": ["Sun"], "disease": "Akshi roga, Jwara, Bandhana, Shiroroga, Kushta", "remedy": "आकृणेत mantrjapa", "comments": "Surya Mahadasha"},
    {"zodiac_sign": "Leo", "planets": ["Moon"], "disease": "Pandu", "remedy": "Chandra aradhana as told", "comments": "In navamsha kundali"},
    {"zodiac_sign": "Cancer", "planets": ["Mars"], "disease": "Raktapitta, jwara, daha, agnichaura "
                                                              "upadrava", "remedy": "“अिनमूधत mantra japa; homa with Tila-Ajya-Khadira samit, vidruma dharana", "comments": ""},
    {"zodiac_sign": "Gemini", "planets": ["Ketu"], "disease": "Raktapitta, jwara, daha, agnichaura "
                                                           "upadrava", "remedy": "“अिनमूधत mantra japa; homa with Tila-Ajya-Khadira samit, vidruma dharana", "comments": ""}

]
# User-provided data with Disease, Remedy, and Comments this is for the planets and zodiac
user_provided_data = [
    {"Zodiac Sign": "Libra", "Planets in Sign": "Sun", "Disease": "Akshi roga, Jwara, Bandhana, Shiroroga, Kushta", "Remedy": "आकृणेत mantrjapa", "Comments": "Surya Mahadasha"},
    {"Zodiac Sign": "Leo", "Planets in Sign": "Moon", "Disease": "Pandu", "Remedy": "Chandra aradhana as told", "Comments": "In navamsha kundali"},
    {"Zodiac Sign": "Pisces", "Planets in Sign": "Jupiter", "Disease": "Raktapitta, jwara, "
                                                                       "daha, agnichaura upadrava", "Remedy": "अिनमूधत mantra japa; homa with Tila-Ajya-Khadira samit, vidruma dharana","Comments": "In navamsha kundali"}
]

user_provided_data1 = [
    {"Zodiac Sign": "Libra", "Planets in Sign": "Sun", "Disease": "Akshi roga, Jwara, Bandhana, Shiroroga, Kushta", "Remedy": "आकृणेत mantrjapa", "Comments": "Surya Mahadasha"},
    {"Zodiac Sign": "Leo", "Planets in Sign": "Moon", "Disease": "Pandu", "Remedy": "Chandra aradhana as told", "Comments": "In navamsha kundali"},
    {"Zodiac Sign": "Pisces", "Planets in Sign": "Jupiter", "Disease": "sssss, jwara, "
                                                                       "daha, agnichaura upadrava", "Remedy": "अिनमूधत mantra japa; homa with Tila-Ajya-Khadira samit, vidruma dharana","Comments": "In navamsha kundali"}
]



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
    .kundali {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(4, 1fr);
        gap: 10px;
        margin-top: 20px;
    }
    .kundali div {
        border: 1px solid #ddd;
        padding: 10px;
        text-align: center;
        font-weight: bold;
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

            # Create Kundali chart in South Indian style
            st.write("### South Indian Style Kundali")

            kundali_signs = {
                'Pisces': ('row1', 'col1'),
                'Aries': ('row1', 'col2'),
                'Taurus': ('row1', 'col3'),
                'Gemini': ('row1', 'col4'),
                'Aquarius': ('row2', 'col1'),
                'Cancer': ('row2', 'col4'),
                'Capricorn': ('row3', 'col1'),
                'Leo': ('row3', 'col4'),
                'Sagittarius': ('row4', 'col1'),
                'Scorpio': ('row4', 'col2'),
                'Libra': ('row4', 'col3'),
                'Virgo': ('row4', 'col4')
            }

            kundali_html = '<div class="kundali">'
            for row in range(1, 5):
                for col in range(1, 5):
                    sign = None
                    for zodiac_name, (r, c) in kundali_signs.items():
                        if r == f'row{row}' and c == f'col{col}':
                            sign = zodiac_name
                            break
                    if sign:
                        planets = ', '.join(readable_planets_in_sign[sign])
                        house = readable_house_from_sign[sign]
                        kundali_html += f'<div class="row{row} col{col}">{sign}<br>Planets: {planets}<br>House: {house}</div>'
                    else:
                        kundali_html += f'<div class="row{row} col{col}"></div>'
            kundali_html += '</div>'

            st.write(kundali_html, unsafe_allow_html=True)

            # Match and display predictions
            st.write("### Predictions Based on Planets and House Matching")
            predictions = []
            for zodiac_name, planets in readable_planets_in_sign.items():
                house = readable_house_from_sign[zodiac_name]
                for entry in matching_table:
                    if house == entry["house"] and all(planet in planets for planet in entry["planets"]):
                        predictions.append((entry["disease"], entry["remedy"], entry["comment"]))

            if predictions:
                for disease, remedy,comment in predictions:
                    st.write(f"Match Found! \nDisease: {disease}, \nRemedy: {remedy}\n, \nComment: {comment}")
                    st.write("Match Found!")
                    st.write(f"Disease: {disease}")
                    st.write(f"Remedy: {remedy}")
                    st.write(f"Comment: {comment}")
            else:
                st.write("No matches found in the matching table.")



            # Match the user-provided data with the calculated zodiac data

            matched_data = []
            for data in user_provided_data:
                zodiac_sign = data["Zodiac Sign"]
                planet = data["Planets in Sign"]

                if zodiac_sign in readable_planets_in_sign and planet in readable_planets_in_sign[zodiac_sign]:
                    matched_data.append(data)

            if matched_data:
                st.write("### Matched User Data with Calculated Zodiac Data")
                matched_table_html = "<table><tr><th>Zodiac Sign</th><th>Planets in Sign</th><th>Disease</th><th>Remedy</th><th>Comments</th></tr>"
                for entry in matched_data:
                    matched_table_html += f"<tr><td>{entry['Zodiac Sign']}</td><td>{entry['Planets in Sign']}</td><td>{entry['Disease']}</td><td>{entry['Remedy']}</td><td>{entry['Comments']}</td></tr>"
                matched_table_html += "</table>"
                st.write(matched_table_html, unsafe_allow_html=True)
            else:
                st.write("No matching data found.")




            # Calculate Dasa for Now
            dasafornowList = Calculate.DasaForNow(birth_time)
            # Extract and print planet name from the second line of the output
            raw_lines = str(dasafornowList).split('\n')
            if len(raw_lines) > 1:
                # Extract the planet name using string parsing
                planet_line = raw_lines[1].strip()
                planet_name = planet_line.split(':')[0].replace('"', '').strip()
                st.write(f'#### Dasa for Now Planet Name: "{planet_name}"')
            # else:
                st.write('#### Dasa for Now Planet Name: "No planet name found"')

            if planet_name == "Mars":
                # Match the user-provided data with the calculated zodiac data
                matched_data = []
                for data in user_provided_data1:
                    zodiac_sign = data["Zodiac Sign"]
                    planet = data["Planets in Sign"]

                    if zodiac_sign in readable_planets_in_sign and planet in readable_planets_in_sign[zodiac_sign]:
                        matched_data.append(data)

                if matched_data:
                    st.write("### Matched User Data with Calculated Zodiac Data")
                    matched_table_html = "<table><tr><th>Zodiac Sign</th><th>Planets in Sign</th><th>Disease</th><th>Remedy</th><th>Comments</th></tr>"
                    for entry in matched_data:
                        matched_table_html += f"<tr><td>{entry['Zodiac Sign']}</td><td>{entry['Planets in Sign']}</td><td>{entry['Disease']}</td><td>{entry['Remedy']}</td><td>{entry['Comments']}</td></tr>"
                    matched_table_html += "</table>"
                    st.write(matched_table_html, unsafe_allow_html=True)
                else:
                    st.write("No matching data found.")
            else:
                st.write("Surya Maha Dasha Dosha is not there")



            # Calculate Dasa for Life
            allHouseDataList = Calculate.DasaForLife(birth_time)

            # Convert JObject to JSON string, then parse to Python dictionary
            allHouseDataList_str = allHouseDataList.ToString()
            allHouseDataList_dict = json.loads(allHouseDataList_str)

            # Function to format the Dasa data
            def format_dasa(dasa):
                if isinstance(dasa, dict):
                    output = []
                    for period, details in dasa.items():
                        output.append(f"{period}:")
                        for key, value in details.items():
                            if key == "SubDasas":
                                sub_output = format_dasa(value)
                                output.append(f"  {key}:")
                                for line in sub_output:
                                    output.append(f"    {line}")
                            else:
                                output.append(f"  {key}: {value}")
                    return output
                return []

            dasa_output_formatted = format_dasa(allHouseDataList_dict)
            dasa_output_str = "\n".join(dasa_output_formatted)

            # Display calculated data
            st.write("### Calculated Zodiac Data1")

            # st.write("#### Planets in Sign:")
            # st.write(planets_in_sign)
            #
            # st.write("#### House from Sign Name:")
            # st.write(house_from_sign)

            st.write("#### Dasa for Life:")
            st.text(dasa_output_str)

        except Exception as e:
            st.error(f"An error occurred: {e}")



        except Exception as e:
            st.error(f"An error occurred: {e}")
