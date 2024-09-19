# Version 1.1
# -------------------------------------------
# ---------------------------------------------


# astro_calculations.py

# from vedastro import Calculate, GeoLocation, Time
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
#
# def calculate_lord_of_house(birth_time, house_name):
#     lord_of_house = Calculate.LordOfHouse(house_name, birth_time)
#     return str(lord_of_house)




# Version 1.2
# -------------------------------------------
# ---------------------------------------------
# astro_calculations.py
# astro_calculations.py

from vedastro import Calculate, GeoLocation, Time, PlanetName, HouseName

def calculate_lunar_day(birth_time):
    lunar_day = Calculate.LunarDay(birth_time)
    lunar_day_info = {
        "Name": lunar_day.GetTithiName(),
        "Paksha": lunar_day.GetPaksha(),
        "Date": f"{lunar_day.GetLunarDateNumber()}/30",
        "Day": f"{lunar_day.GetLunarDayNumber()}/15",
        "Phase": str(lunar_day.GetMoonPhase())  # Convert to string for JSON serialization
    }
    return lunar_day_info

def calculate_lord_of_house(birth_time, house_name):
    lord_of_house = Calculate.LordOfHouse(house_name, birth_time)
    return str(lord_of_house)

# Add additional calculation functions
def is_sun_malefic_to_lagna(birth_time):
    return Calculate.IsPlanetMaleficToLagna(PlanetName.Sun, birth_time)

# Update this function based on the correct method signature
def is_yogakaraka_to_lagna(birth_time):
    return Calculate.IsPlanetYogakarakaToLagna(birth_time)  # Correct this method if necessary

def get_sun_speed(birth_time):
    return Calculate.PlanetSpeed(PlanetName.Sun, birth_time)

# Remove or update this function if LordOfHora doesn't exist
def get_lord_of_hora(birth_time):
    return Calculate.LordOfHora(birth_time)

def get_house1_10_longitudes(birth_time):
    return Calculate.GetHouse1And10Longitudes(birth_time)

def lmt_to_utc(birth_time):
    return Calculate.LmtToUtc(birth_time)

def is_gochara_obstructed(birth_time):
    return Calculate.IsGocharaObstructed(birth_time)

def is_mercury_malefic(birth_time):
    return Calculate.IsMercuryMalefic(birth_time)

def is_moon_benefic(birth_time):
    return Calculate.IsMoonBenefic(birth_time)

def get_benefic_planets(birth_time):
    return Calculate.BeneficPlanetList(birth_time)

def get_malefic_planets(birth_time):
    return Calculate.MaleficPlanetList(birth_time)

def planets_aspecting_house1(birth_time):
    return Calculate.PlanetsAspectingHouse(HouseName.House1, birth_time)

def all_planets_ordered_by_strength(birth_time):
    return Calculate.AllPlanetOrderedByStrength(birth_time)

def all_planet_strength(birth_time):
    return Calculate.AllPlanetStrength(birth_time)

def all_houses_ordered_by_strength(birth_time):
    return Calculate.AllHousesOrderedByStrength(birth_time)

def sun_shadbala_pinda(birth_time):
    return Calculate.PlanetShadbalaPinda(PlanetName.Sun, birth_time)

def sun_drik_bala(birth_time):
    return Calculate.PlanetDrikBala(PlanetName.Sun, birth_time)

def sun_chesta_bala(birth_time):
    return Calculate.PlanetChestaBala(PlanetName.Sun, birth_time)

def epoch_interval(birth_time):
    return Calculate.EpochInterval(birth_time)

def sun_motion_name(birth_time):
    return Calculate.PlanetMotionName(PlanetName.Sun, birth_time)

def sun_saptavargaja_bala(birth_time):
    return Calculate.PlanetSaptavargajaBala(PlanetName.Sun, birth_time)
