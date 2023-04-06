#Dakari Project
#input planet name and return it's value
#Distance from Sun 
#Mercury
#Venus
#Earth
#Mars
#Jupiter
#Saturn
#Uranus
#Neptune

Mercury = 57900000
Venus = 108200000
Earth = 149600000 
Mars = 227900000
Jupiter = 778600000
Saturn = 1433500000
Uranus = 2872500000
Neptune = 4495100000



#To create our application, we want to read the distance from the sun for two planets, and then display the distance between the planets. We'll do this by using input to read the values, int to convert to integer, and then abs to convert the result into its absolute value.
first_planet_input = input("Choose Planet 1: ")
second_planet_input= input("Choose Planet 2: ")
if first_planet_input=="Mercury":
        print(f"The Distance between the Sun Mercury and is {Mercury} KM")
elif first_planet_input=="Venus":
        print(f"The Distance bewtween the Sun and Venus is {Venus} KM")
elif first_planet_input=="Earth":
        print(f"The Distance bewtween the Sun and Earth is {Earth} KM")
elif first_planet_input=="Mars":
        print(f"The Distance bewtween the Sun and Mars is {Mars} KM")
elif first_planet_input=="Jupiter":
        print(f"The Distance bewtween the Sun and Jupiter is {Jupiter} KM")
elif first_planet_input=="Saturn":
        print(f"The Distance bewtween the Sun and Saturn is {Saturn} KM")
elif first_planet_input=="Uranus":
        print(f"The Distance bewtween the Sun and Uranus is {Uranus} KM")
elif first_planet_input=="Neptune":
        print(f"The Distance bewtween the Sun and Neptune is {Neptune} KM")
elif first_planet_input==['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']:
        print("First letter must be capital!")
else:
        print("THAT IS NOT A PLANET XP")


if second_planet_input=="Mercury":
        print(f"The Distance between the Sun Mercury and is {Mercury} KM")
elif second_planet_input=="Venus":
        print(f"The Distance bewtween the Sun and Venus is {Venus} KM")
elif second_planet_input=="Earth":
        print(f"The Distance bewtween the Sun and Earth is {Earth} KM")
elif second_planet_input=="Mars":
        print(f"The Distance bewtween the Sun and Mars is {Mars} KM")
elif second_planet_input=="Jupiter":
        print(f"The Distance bewtween the Sun and Jupiter is {Jupiter} KM")
elif second_planet_input=="Saturn":
        print(f"The Distance bewtween the Sun and Saturn is {Saturn} KM")
elif second_planet_input=="Uranus":
        print(f"The Distance bewtween the Sun and Uranus is {Uranus} KM")
elif second_planet_input=="Neptune":
        print(f"The Distance bewtween the Sun and Neptune is {Neptune} KM")
elif second_planet_input==['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']:
        print("First letter must be capital!")
else:
        print("THAT IS NOT A PLANET XP")


first_planet_int = input("Enter the distance between the Sun and Planet 1: ")
second_planet_int = input("Enter the distance between the Sun and Planet 2: ")

first_planet = int(first_planet_int)
second_planet = int(second_planet_int)

distance_km = abs(first_planet - second_planet)
print(f"The distance between Planet 1 and Planet 2 is: {distance_km} KM")


