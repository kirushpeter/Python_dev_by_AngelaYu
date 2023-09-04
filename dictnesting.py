

# nesting dictionaries inside a list

travel_log = [

    {
        "country": "France",
        "Cities_visited": ["Paris", "Lillie", "Dijon"],
        "Total_visits": 12
    },

    {
        "country": "Germany",
        "Cities_visited": ["Berlin", "Hamburge", "Stuttgart"],
        "Total_visits": 5
    }


]


# nesting a dictionary inside a dictonary.

'''
travell_logy = {

    "France":{"Cities visited": ["Paris", "Lille", "Dijon"],"total_visits": 12},  # key, value as a list.

    "Germany":{"cities_visited":["Berlin", "Harmburg", "Stuttgart"],"total_visits": 5}
}

'''
def add_new_country(country_visited, times_visited, cities_visited):

    new_country = {}

    new_country["country"] = country_visited

    new_country["cities"] = cities_visited

    new_country["visits"] = times_visited

    travel_log.append(new_country)


add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)

print(travel_log)


