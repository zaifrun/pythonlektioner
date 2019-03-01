""" Denne indeholder eksempel kode fra lektion 4 - bruger input og while"""


navn = input("Hvad er dit navn: ")
print("Hej "+navn +"!")

alder = int(input("Hvad er din alder, "+navn+"? "))

if alder<18:
    print("Du er meget ung!")
elif alder>80:
    print("Du er meget gammel")
else:
    print("Du er hverken ung eller gammel")


counter = 1
print("########### Et eksempel på en while løkke #########")
while counter<11:
    print(counter)
    counter+=1


##########Vi kan også "gå ud af en løkke" vha af break
print("########## break fra en løkkke #############")
counter = 12
while counter<20:
    if counter>15:
        break
    print(counter)
    counter+=1



print("Når du er færdig med at indtaste ingredienser, skriv 'q'")
mere = True
ingredienser = []
while mere:
    ingredient = input("Hvad vil du have på din pizza? ")
    if ingredient == "q":
        mere = False  # kunne vi have gjort noget andet her?
    else:
        ingredienser.append(ingredient)
print("Du har valgt følgende ingredienser til din pizza:")
for ingredient in ingredienser:
    print(ingredient)

