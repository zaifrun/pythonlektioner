""" Denne indeholder eksempel kode fra lektion 4 - bruger input og while"""


"""
navn = input("Hvad er dit navn:")
print("Hej "+navn +"!")

alder = int(input("Hvad er din alder, "+navn+"?"))

if alder<18:
    print("Du er meget ung!")
elif alder>90:
    print("Du er meget gammel")

"""

counter = 1
while counter<11:
    print(counter)
    counter+=1


print("Når du er færdig med at indtaste ingredienser, skriv quit")
mere = True
ingredienser = []
while mere:
    ingredient = input("Hvad vil du have på din pizza?")
    if ingredient == "quit":
        mere = False
    else:
        ingredienser.append(ingredient)
print("Du har valgt følgende ingredienser til din pizza")
for ingredient in ingredienser:
    print(ingredient)

