# Maxine Liu
# 10/22/2018
# COSC 1
# uses world_cities.txt to create file world_cities.txt.

from city import *

# open file in read only mode.

in_file = open("world_cities.txt", "r")

# create an empty list to hold items I will create in the nested for loop below.

list_all_cities = []

# create nested for loop to first split the text using a comma, the second loop strips individual words.

for line in in_file:
    split_line = line.split(",")

    for n in split_line:
        n.strip()

    # creates an object for each city
    this_city = City(split_line[0], split_line[1], split_line[2], int(split_line[3]),
                     float(split_line[4]), float(split_line[5]))

    # add the newly created city to the empty list
    list_all_cities.append(this_city)

# close file in read only mode
in_file.close()

# create a file with permission to write so that the new list of cities could be written
out_file = open("cities_out.txt", "w")

# deposit city objects in text with a new life for each city
for city in list_all_cities:
    out_file.write(str(city)+"\n")

out_file.close()
