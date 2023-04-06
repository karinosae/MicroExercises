#Dakari Project
#input planet name and return it's value
#Distance from Sun
'Mercury' == 57900000
'Venus' == 108200000
'Earth' == 149600000
'Mars' == 227900000
'Jupiter' == 778600000
'Saturn' == 1433500000
'Uranus' == 2872500000
'Neptune' == 4495100000



#To create our application, we want to read the distance from the sun for two planets, and then display the distance between the planets. We'll do this by using input to read the values, int to convert to integer, and then abs to convert the result into its absolute value.
first_planet_input = input("Enter the distance between the Sun and Planet 1 in: ")
second_planet_input = input("Enter the distance between the Sun and Planet 2 in: ")
print(first_planet_input)
print(second_planet_input)

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = abs(first_planet - second_planet)
print(distance_km)


