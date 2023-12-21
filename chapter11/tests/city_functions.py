def city_country(city , country, population=''):
    if population:
        full=f"{city} {country} population {population}"
    else :
        full=f"{city} {country}"

    return full