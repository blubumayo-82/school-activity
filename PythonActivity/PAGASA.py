wind_speed = 165
storm_id = input("The storm id is   ")

if storm_id.startswith("BAGYONG"):
    storm_name = storm_id[8:12]

    if wind_speed > 220:
        category = "Super Typhoon"
    elif 118 < wind_speed <= 220:
        category = "Typhoon"
    elif wind_speed <= 118:
        category = "Severe Tropical Storm"

    print("WARNING: " + storm_id + " is classified as a " + category + " with winds of " + str(wind_speed) + " kph!")

else:
    print("Invalid Storm ID Format")

