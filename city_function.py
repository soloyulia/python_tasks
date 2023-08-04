def country_city(country,city,population=0):
    if population:
        full_name = f"{country}, {city}, {population}"
    else:
        full_name = f"{country}, {city}"
    return full_name.title()