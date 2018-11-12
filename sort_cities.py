# Maxine Liu
# 10/22/2018
# COSC 1
# creates files cities_alpha.txt, cities_population.txt, and cities_latitude.txt.

from quicksort import *
from list_of_cities import *

# creates file cities_alpha.txt where city objects are ranked by instance variables self.name in the City class.

alphabetical = open("cities_alpha.txt", "w")

# sorting by city name alphabetically

City.__le__ = City.compare_name
quicksort(list_all_cities)

# deposit city objects in text with a new life for each city

for city in list_all_cities:
    alphabetical.write(str(city)+"\n")

alphabetical.close()

# creates file cities_population.txt where city objects are ranked by instance variables self.pop in the City class.

population = open("cities_population.txt", "w")

# sorting by city population in decreasing order.

City.__le__ = City.compare_population
quicksort(list_all_cities)

# deposit city objects in text with a new life for each city
for city in list_all_cities:
    population.write(str(city)+"\n")

population.close()

# creates file cities_latitude.txt where city objects are ranked by instance variables self.lat in the City class.

latitude = open("cities_latitude.txt", "w")

# sorting by city population in decreasing order.

City.__le__ = City.compare_latitude
quicksort(list_all_cities)

# deposit city objects in text with a new life for each city
for city in list_all_cities:
    latitude.write(str(city)+"\n")

latitude.close()