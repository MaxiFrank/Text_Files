# Maxine Liu
# 10/22/2018
# COSC 1
# City class and 5 methods within the class

# construct the sort class that takes in self and 6 additional formal parameters.

class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        # string
        self.cc = country_code
        # string
        self.name = name
        # string
        self.region = region
        # integer
        self.pop = population
        # float
        self.lat = latitude
        # float
        self.log = longitude

    # string method that takes in self as parameter and will be called to produced text files.

    def __str__(self):
        return self.name + "," + str(self.pop) + "," + str(self.lat) + "," + str(self.log)

    # method that will help compare city objects in alphabetical order and produce the cities_alpha.txt file.

    def compare_name(self, other):
        return self.name.lower() <= other.name.lower()

    # method that will help compare city objects by population and produce the cities_population.txt file.

    def compare_population(self, other):
        return self.pop >= other.pop

    # method that will help compare city objects by latitude and produce the cities_latitude.txt file.

    def compare_latitude(self, other):
        return self.lat <= other.lat



