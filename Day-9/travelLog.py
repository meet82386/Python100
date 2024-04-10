travel_log = [
    {
        "country": "Republic of India",
        "visits": 5,
        "cities": ["Hampi", "Varanasi", "Jaisalmer", "Bhuj", "Coimbtore", "Leh", "Junagadh"]
    },
    {
        "country": "Kingdom of Saudi Arebia",
        "visits": 1,
        "cities": ["Riyadh", "Madina"]
    },
    {
        "country": "Japan",
        "visits": 6,
        "cities": ["Kyoto", "Tokyo", "Hokkaido"]
    },
]


def addLog(country, visits, cities):
    temp_dict = {
        "country": country,
        "visits": visits,
        "cities": cities
    }

    travel_log.append(temp_dict)


country_name = input("Enter the name of country: ")
visits = int(input("Enter number of visits: "))
cities = input("Enter cities visited saperated by space: ").split()

addLog(country_name, visits, cities)
print(travel_log)