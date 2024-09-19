from vedastro import *
import streamlit as st
from enum import Enum
import vedastro
Place="tokyo"
Country="Japan"
Longitude =float(139.8300000000000)
Latitude=float(35.65000000000000000)
geolocation = GeoLocation(Place,Longitude,Latitude)
TimeofBirth="23:40"
DateofBirth="31/03/2011"
GMT="+0900"
TOBDOBGMT=str(TimeofBirth+" "+DateofBirth+" "+GMT)

birth_time = Time(TOBDOBGMT, geolocation)
#
# allZodiacDataList = Calculate.PlanetsInSign(ZodiacName.Pisces, birth_time)
# Tools.Print(allZodiacDataList)

# YearOfCoincidence = int(vedastro.Calculate.Ayanamsa.Lahiri)
# Calculate.YearOfCoincidence = int(vedastro.Calculate.Ayanamsa.Lahiri)

# moon_constellation = Calculate.PlanetConstellation(PlanetName.Sun, birth_time)
# planet_longitude = Calculate.PlanetNirayanaLongitude(PlanetName.Sun, birth_time)
# print(f"Sun Constellation : {moon_constellation}")
# print(f"Nirayana Longitude : {planet_longitude}")
# print(f"\nRAMAN AYANAMSA : 397 AD")
# Calculate.YearOfCoincidence = int(Ayanamsa.Raman)



# lordofhouse = Calculate.LordOfHouse(HouseName.House4, birth_time)
# Tools.Print(lordofhouse)

# allPlanetDataList = Calculate.PlanetZodiacSign(PlanetName.Moon, birth_time)
# Tools.Print(allPlanetDataList)
#
# def calculate_all_planet_data(PlanetName.Sun, birth_time):
#     planet_data = Calculate.AllPlanetData(PlanetName.Sun, birth_time)
#     all_planet_info = {
#         "Name": planet_data.GetTithiName(),
#         "Paksha": planet_data.GetPaksha(),
#         "Date": f"{planet_data.GetLunarDateNumber()}/30",
#         "Day": f"{planet_data.GetLunarDayNumber()}/15",
#         "Phase": str(planet_data.GetMoonPhase())  # Convert to string for JSON serialization
#     }
#     return all_planet_info
#

#
# def calculate_lunar_day(birth_time):
#     lunar_day = Calculate.LunarDay(birth_time)
#     lunar_day_info = {
#         "Name": lunar_day.GetTithiName(),
#         "Paksha": lunar_day.GetPaksha(),
#         "Date": f"{lunar_day.GetLunarDateNumber()}/30",
#         "Day": f"{lunar_day.GetLunarDayNumber()}/15",
#         "Phase": str(lunar_day.GetMoonPhase())  # Convert to string for JSON serialization
#     }
#     return lunar_day_info
# with st.expander("All Planets Data"):
#     if st.button("Calculate All planets data"):
#         st.session_state.all_planet_info = calculate_all_planet_data(PlanetName.Sun, birth_time)
#     if "all_planet_info" in st.session_state and st.session_state.all_planet_info:
#         st.json(st.session_state.all_planet_info)
# help(birth_time)


# allZodiacDataList = Calculate.AllZodiacSignData(ZodiacName.Gemini, birth_time)
# Tools.Print(allZodiacDataList)

# allHouseDataList = Calculate.AllHouseData(HouseName.House4, birth_time)
# Tools.Print(allHouseDataList)

# allPlanetDataList = Calculate.AllPlanetData(PlanetName.Venus, birth_time)
# Tools.Print(allPlanetDataList)
# print("*******************************************")
# allPlanetDataList = Calculate.AllPlanetData(PlanetName.Sun, birth_time)
# Tools.Print(allPlanetDataList)
# print("*****************************************")
# allPlanetDataList = Calculate.AllPlanetData(PlanetName.Moon, birth_time)
# Tools.Print(allPlanetDataList)
# print("*****************************************")

# allHouseDataList = Calculate.AllHouseData(HouseName.House9, birth_time)
# Tools.Print(allHouseDataList)
#
# allHouseDataList = Calculate.PlanetHoraSigns(PlanetName.Sun, birth_time)
# Tools.Print(allHouseDataList)

allHouseDataList = Calculate.DasaForNow(birth_time)
Tools.Print(allHouseDataList)



# print(dir(vedastro.Calculate.DasaForNow))
# print(type(vedastro.Calculate.PlanetsInSign))
# help(vedastro.Calculate.PlanetZodiacSign)
# help(vedastro.Calculate.DasaForNow)
# print(dir(vedastro.ChartType.Hora))
# print(Calculate.DasaForNow.__doc__)

# help(BirthTimeInVedicDay)

# allPlanetDataList = Calculate.PlanetRelationshipWithSign(PlanetName.Sun,ZodiacName.Aries, birth_time)
# Tools.Print(allPlanetDataList)

# def get_panchaka(time: Time) -> PanchakaName:
#     return VedAstro.Calculate.Panchaka(time)

