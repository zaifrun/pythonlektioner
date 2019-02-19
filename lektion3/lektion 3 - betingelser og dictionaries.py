""" Denne indeholder eksempel kode fra lektion 3 - betingelse og dictionaries"""

print("lektion 3 - betingelse og dictionaries")


#forskel på = og ==
print ("######## forskel på = og == ############")
car = "Fiat"

print(car == "fiat")
print(car == "Fiat")

if car == "Fiat":
    print("Det er en Fiat")
else:
    print("Det er ikke en Fiat")


# nummeriske sammenligninger
print(" ###### numeriske sammenligninger ###########3")
alder = 41
print ("alder under 50: " + str(alder<50))
print ("alder over 45 : " + str(alder>45))
print (alder!=40)
print (alder>40 and alder<50)
print (alder>40 or alder > 60)

tirsdag = True

if tirsdag:
    print("Det er tirsdag")
else:
    print("Det er ikke tirsdag")

print ("########### if-elif-else ##############")
dag = 2

if dag == 1:
    print("mandag")
elif dag == 2:
    print("tirdag")
elif dag == 3:
    print("onsdag")
elif dag == 4:
    print("tordag")
elif dag == 5:
    print("fredag")
elif dag == 6:
    print("lørdag")
elif dag == 7:
    print("søndag")
else:
    print("ukendt dag")
#kunne ovenstående måske laves smartere?

# betingelser i forbindelse med lister.

navne = []

#kunne if sætningen nedenfor laves på andre måder?
if navne:
    print(navne)
else:
    print("beklager, din liste er tom")


#dictionaries

print("############# dictionaries - ordbøger ########")

player = { "color" : "green" , "point" : 5}
print(player)

print("farven er : "+ player["color"])
print("antal point : "+str(player["point"]))

######## hvad hvis man slår forkerte ting op? ########
#print("farven er : " + player["Color"])

#Hvis man vil være sikker, så kan man bruge get
#print("farven er : " + player.get("Color","udefineret farve"))

#så en ordbog består af keys og values (nøgler og værdier) på dansk

#vi kan tilføje til en dictionary
player["lives"] = 6

#vi kan også ændre værdier
player["color"] = "blue"

print(player)

# vi kan også fjerne key/values

del player["lives"]
print(player)

print("######## for løkker med dictionaries ##########")
#brug af for-løkker med dictionaries

for key, value in player.items():
    print (key + " = " + str(value))


# vi kan også få en liste kun med keys eller kun med values
print("Keys   : " + str(player.keys()))
print("Values : " + str(player.values()))

print("########### Duplicate keys ##########")
# hvad nu hvis der er flere keys som har samme værdi?
navne = { "martin" : "knudsen",
          "martin" : "jensen"}
print(navne["martin"])

# Nesting
print("############### Nesting af lister og dictioaries ###################")

print(" eksempel på en liste i en dictonary")

pizza1 = { "type" : "hawaii",
          "ingredienser" : ["ananas", "ost","skinke","tomat"]}

print("ingredienser i "+pizza1["type"] + " pizza:")
for ingredient in pizza1["ingredienser"]:
    print(ingredient)